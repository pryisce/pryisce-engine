#!/usr/bin/env python3
"""Keeps the Pryisce Engine Discord bot showing as online.

It holds one connection to Discord open and does nothing else: it asks for no message
content (intents 0) and never sends a message. Update announcements are posted separately,
by the publisher, when a new version goes out.

Needs the bot token in the environment variable DISCORD_TOKEN.
"""
import asyncio
import json
import os
import sys

import websockets

TOKEN = os.environ.get("DISCORD_TOKEN", "").strip()
STATUS = os.environ.get("BOT_STATUS", "for updates")
GATEWAY = "wss://gateway.discord.gg/?v=10&encoding=json"


async def connect_once():
    async with websockets.connect(GATEWAY, max_size=None) as ws:
        hello = json.loads(await ws.recv())
        every = hello["d"]["heartbeat_interval"] / 1000
        last = {"seq": None}

        await ws.send(json.dumps({
            "op": 2,
            "d": {
                "token": TOKEN,
                "intents": 0,
                "properties": {"os": "linux", "browser": "pryisce-engine", "device": "pryisce-engine"},
                "presence": {"status": "online", "afk": False, "since": None,
                             "activities": [{"name": STATUS, "type": 3}]},
            },
        }))

        async def heartbeat():
            while True:
                await asyncio.sleep(every)
                await ws.send(json.dumps({"op": 1, "d": last["seq"]}))

        beating = asyncio.create_task(heartbeat())
        try:
            async for raw in ws:
                message = json.loads(raw)
                if message.get("s") is not None:
                    last["seq"] = message["s"]
                op = message.get("op")
                if op == 0 and message.get("t") == "READY":
                    print("online", flush=True)
                elif op == 1:
                    await ws.send(json.dumps({"op": 1, "d": last["seq"]}))
                elif op in (7, 9):
                    return  # Discord asked for a fresh connection
        finally:
            beating.cancel()


async def main():
    if not TOKEN:
        sys.exit("DISCORD_TOKEN is not set")
    wait = 5
    while True:
        try:
            await connect_once()
            wait = 5
        except websockets.ConnectionClosed as closed:
            print(f"offline: connection closed ({closed.code})", flush=True)
            if closed.code == 4004:
                sys.exit("Discord refused the token. Put the right one in /etc/pryisce-bot.env")
        except Exception as error:  # no network for a moment, and the like
            print(f"offline: {error}", flush=True)
        await asyncio.sleep(wait)
        wait = min(wait * 2, 300)


if __name__ == "__main__":
    asyncio.run(main())