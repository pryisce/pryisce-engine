<div align="center">

# Pryisce Engine

A free Windows app for PC gamers, made mostly for Roblox. It shows your real ping and fps,
tells you what is causing lag, and has the tweaks and tools to fix it.

[![Latest version](https://img.shields.io/github/v/release/pryisce/pryisce-engine?label=latest&color=FF2E97&style=for-the-badge)](https://github.com/pryisce/pryisce-engine/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/pryisce/pryisce-engine/total?color=A24DFF&style=for-the-badge)](https://github.com/pryisce/pryisce-engine/releases)
![Windows 10 and 11](https://img.shields.io/badge/Windows-10%20%7C%2011-1f1f2e?style=for-the-badge)

**[Download](https://github.com/pryisce/pryisce-engine/releases/latest)** &nbsp;·&nbsp; **[Patch notes](https://github.com/pryisce/pryisce-engine/releases)** &nbsp;·&nbsp; **[Is it safe?](#is-it-safe)**

[![Watch the video on YouTube](docs/film-preview.gif)](https://youtu.be/MPpSFRBb1kM)

[![Watch the video on YouTube](https://img.shields.io/badge/Watch%20the%20video-YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://youtu.be/MPpSFRBb1kM)

</div>

## Ping, fps and temps

![Live](docs/live.jpg)

<table>
<tr>
<td width="50%"><img src="docs/frame-time.jpg" alt="Frame Time"></td>
<td width="50%"><img src="docs/sensors.jpg" alt="Sensors"></td>
</tr>
</table>

- **Live**: ping to the game server you are actually on, five times a second, and where on the route the delay is
- **Frame Time**: fps ten times a second, with the lows and every freeze
- **Sensors**: temperatures, clock speeds, power and fans, no driver needed
- **Background**: which programs are eating performance while you play, with a button to pause them

## Finding lag

![Diagnostics](docs/diagnostics.jpg)

- **Diagnostics**: six troubleshooters that go through the usual causes one by one
- **Fair Play**: tells you if a ping spike came from your router, your internet provider or the game server

## Tweaks

<table>
<tr>
<td width="50%"><img src="docs/tweaks.jpg" alt="Tweaks"></td>
<td width="50%"><img src="docs/profiles.jpg" alt="Profiles"></td>
</tr>
</table>

- **Advisor**: suggests tweaks that fit your PC and says how much each one helps and what the risk is
- **Tweaks**: eighty Windows and network tweaks, each one explained, each one can be undone
- **Profiles**: settings that switch on when a game starts and off when it closes
- **Frame Generation**: extra frames for Roblox
- **Tools**: one-off jobs like clearing caches

## Benchmark and undo

<table>
<tr>
<td width="50%"><img src="docs/benchmark.jpg" alt="Benchmark"></td>
<td width="50%"><img src="docs/snapshots.jpg" alt="Snapshots"></td>
</tr>
</table>

- **Benchmark**: timed runs before and after a tweak, next to each other
- **History**: every session is recorded and can be played back
- **Snapshots**: your PC's settings are saved before each change, so you can go back

## Roblox

![Server globe](docs/globe.jpg)

- **Server globe**: when you join or teleport, a 3D globe shows which data centre you are connecting to, until you have loaded in

<table>
<tr>
<td width="50%"><img src="docs/auto-clicker.jpg" alt="Auto Clicker"></td>
<td width="50%"><img src="docs/crosshair.jpg" alt="Crosshair"></td>
</tr>
</table>

- **Auto Clicker**: no speed cap, evenly timed clicks, auto key swap with an on/off key and an off key, and a BedWars tuner that finds your best settings
- **Crosshair**: swaps the Roblox mouse pointer for a crosshair you pick, at the size you pick
- **BedWars**: always sprint and anti stick drift
- **Discord**: shows Pryisce Engine on your Discord profile, with your own text, picture and buttons

## Settings

![24 colour palettes](docs/palettes.jpg)

- **Settings**: in-game overlay, hotkeys, sounds and 24 colour palettes
- **Overview** and **Games**: the game you are in on one screen, and your library with a profile per game
- **Updates**: close the app and open it again to get the newest version

## Install

1. Download `PryisceEngine-x.y.z.zip` from the [latest release](https://github.com/pryisce/pryisce-engine/releases/latest).
2. Unzip it anywhere and run `Pryisce.exe`.

Needs Windows 10 or 11 (64-bit) and the [.NET 10 Desktop Runtime](https://dotnet.microsoft.com/download/dotnet/10.0).

## Is it safe?

Scan reports you can open yourself:

| Scanner | Result | What was scanned | |
|---|---|---|---|
| **VirusTotal** | **0 of 71** security vendors flagged it | `Pryisce.exe`, version 0.0.16 | [**Open the report**](https://www.virustotal.com/gui/file/706a5b2969a77725f8e8f87b6a574f8c3a87f190dbfaf01b5f8b33104276e478) |
| **Triage sandbox** | **3 / 10** (static 3, behaviour 1), where 10 is known malware | `Pryisce.exe`, an earlier version | [**Open the report**](https://tria.ge/261007-ef13ea1zay) |

Scanned 7 October 2026. Each report is for the version it names; every release is a new file.

To check your own download, search this SHA-256 on [virustotal.com](https://www.virustotal.com/gui/home/search) or upload the zip there.

<!-- scan:start -->
| | |
|---|---|
| Latest release | `PryisceEngine-0.0.30.zip` |
| SHA-256 | `18978F628BD7AF4E4FA0B7AA7EF47B06C3D8CFDF542D4136CD47E24A48F6F913` |
<!-- scan:end -->

What the app does:

- No account, no telemetry, no data collected.
- Nothing is injected into a game and no game memory is read.
- The auto clicker, always sprint and anti stick drift send normal keyboard and mouse input.
- The crosshair replaces three pointer pictures in the Roblox folder, keeps the originals, and puts them back when you detach it.
- Every tweak is saved in a snapshot first and can be undone.
- Updates are signed, so a copy only accepts updates from the publisher.
- It goes online to check GitHub for updates, to look up where a game server is, and to read public Roblox info (names, pictures, crosshair decals).

> [!WARNING]
> Auto clickers, input helpers and changed game files can be against a game's rules. Using them online is at your own risk and can get an account banned. The ping, fps, diagnostics and tweak features do not touch the game.

---

<div align="center">
<sub>Pryisce Engine is not affiliated with Roblox Corporation or any game publisher.</sub>
</div>
