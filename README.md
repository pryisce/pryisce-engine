<div align="center">

# Pryisce Engine

**Measure. Diagnose. Optimize. Verify.**

A Windows companion for PC games that shows what is really happening while you play,
finds what is wrong, changes only what has a reason, and proves the difference.

[**Download the latest version**](https://github.com/pryisce/pryisce-engine/releases/latest) · [Patch notes](https://github.com/pryisce/pryisce-engine/releases)

![Live](docs/live.jpg)

</div>

## What it does

| | |
|---|---|
| **Measure** | Live ping to the real game server, frame rate and frame times, temperatures, clocks and power, and which background programs are costing you performance. |
| **Diagnose** | Every ping spike is given a place on the route and a likely cause. One hotkey answers "was that lag me?". Six troubleshooters check the usual suspects in order. |
| **Optimize** | An advisor that only suggests what has a reason on your PC, with its impact and its risk. Eighty tweaks, per-game profiles that undo themselves when the game closes, and frame generation for Roblox. |
| **Verify** | Before-and-after benchmarks, session replays, and a snapshot before every change so anything can be undone. |

### For Roblox

- **Server globe** – on every join and teleport, a 3D Earth turns to the data centre you are connecting to, with the location checked against your ping.
- **Auto clicker** – no speed cap, clicks on an even beat, and an auto key that swaps to a second item for one click and back. A tuner finds the best settings for your PC on a hit-register map.
- **Crosshair** – replaces Roblox's mouse pointer with a crosshair of your choice, at the size you pick.
- **BedWars page** – always sprint and anti stick drift, shown only while you are in BedWars.

<div align="center">

![Auto clicker](docs/auto-clicker.jpg)

![Crosshair](docs/crosshair.jpg)

</div>

## Install

1. Download `PryisceEngine-x.y.z.zip` from the [latest release](https://github.com/pryisce/pryisce-engine/releases/latest).
2. Unzip it anywhere and run `Pryisce.exe`.

Requires Windows 10 or 11 (64-bit) and the [.NET 10 Desktop Runtime](https://dotnet.microsoft.com/download/dotnet/10.0). Windows offers to install the runtime if it is missing.

## Updates

The app updates itself. It looks for a new version every time it starts and installs it before the window opens, so updating is just closing the app and opening it again. Every update is signed by the publisher; a copy ignores anything that is not.

What changed in each version is listed in the [patch notes](https://github.com/pryisce/pryisce-engine/releases).

## How it treats your game

- **No code is injected** into any game, and **no game memory is read**.
- Measurements come from Windows itself: network timing, the graphics pipeline, sensors, and the game's own log files.
- The auto clicker, always sprint and anti stick drift send ordinary keyboard and mouse input, the same as a hand on the device.
- The crosshair swaps three pointer pictures in Roblox's folder and keeps the originals, which are put back when you detach it.
- Every tweak is recorded in a snapshot first and can be undone.

> [!WARNING]
> Auto clickers, input helpers and modified game files can be against a game's rules. Using those features in online games is your own decision and your own risk; an account can be actioned for it. The measuring, diagnosing and optimizing features do not touch the game.

## Privacy

Pryisce Engine has no account and no telemetry. It contacts the internet to check for updates on GitHub, to look up where a game server is, and to read public Roblox information (experience names, pictures and crosshair decals).

---

<div align="center">
<sub>Pryisce Engine is not affiliated with Roblox Corporation or any game publisher.</sub>
</div>
