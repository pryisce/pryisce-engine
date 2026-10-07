<div align="center">

# Pryisce Engine

### Measure. Diagnose. Optimize. Verify.

A Windows companion for PC games. It shows what is really happening while you play,
finds what is wrong, changes only what has a reason, and proves the difference.

[![Latest version](https://img.shields.io/github/v/release/pryisce/pryisce-engine?label=latest&color=FF2E97&style=for-the-badge)](https://github.com/pryisce/pryisce-engine/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/pryisce/pryisce-engine/total?color=A24DFF&style=for-the-badge)](https://github.com/pryisce/pryisce-engine/releases)
![Windows 10 and 11](https://img.shields.io/badge/Windows-10%20%7C%2011-1f1f2e?style=for-the-badge)

**[Download](https://github.com/pryisce/pryisce-engine/releases/latest)** &nbsp;·&nbsp; **[Patch notes](https://github.com/pryisce/pryisce-engine/releases)** &nbsp;·&nbsp; **[Is it safe?](#is-it-safe)**

![Pryisce Engine](docs/live.jpg)

</div>

## Every page, in one line

| | Page | What it does |
|---|---|---|
| | **Overview** | Everything about the game you are in on one screen, and the one issue worth looking at first. |
| | **Games** | Your installed games, each with its own profile. |
| **Measure** | **Live** | Ping to the real game server five times a second, and where on the route the time goes. |
| | **Frame Time** | Frame rate ten times a second, with the lows and every freeze. |
| | **Sensors** | Temperatures, clocks, power and fans, without installing a driver. |
| | **Background** | Which programs are taking performance from the game, and a way to pause them. |
| **Diagnose** | **Diagnostics** | Six troubleshooters that check the likely causes of a problem in order. |
| | **Fair Play** | "Was that lag me?" Pins a ping spike to your router, your provider or the server. |
| **Optimize** | **Advisor** | Suggests only what has a reason on your PC, with its impact and its risk. |
| | **Profiles** | Settings for how you play, applied when a game starts and undone when it closes. |
| | **Tweaks** | Eighty Windows and network tweaks, each explained and reversible. |
| | **Frame Generation** | Extra frames for Roblox. |
| | **Auto Clicker** | No speed cap, clicks on an even beat, auto key swap, and a tuner that finds your best settings. |
| | **BedWars** | Always sprint and anti stick drift. Appears only while you are in BedWars. |
| | **Crosshair** | Replaces Roblox's mouse pointer with a crosshair you pick, at the size you pick. |
| | **Tools** | A toolbox of one-off jobs: network checks, clean-up and more. |
| **Verify** | **Benchmark** | Timed runs before and after a change, side by side. |
| | **History** | Every session recorded, with a replay you can scrub through. |
| | **Snapshots** | The state of your PC before each change, so anything can be undone. |
| | **Settings** | In-game readout, hotkeys, sounds, and 24 colour palettes. |

<div align="center">

<table>
<tr>
<td width="50%"><img src="docs/auto-clicker.jpg" alt="Auto clicker"></td>
<td width="50%"><img src="docs/crosshair.jpg" alt="Crosshair"></td>
</tr>
<tr>
<td align="center"><sub>Auto clicker, auto key and the BedWars tuner</sub></td>
<td align="center"><sub>Crosshair in place of the Roblox pointer</sub></td>
</tr>
</table>

![24 colour palettes](docs/palettes.jpg)
<sub>The same design in 24 colour palettes</sub>

</div>

## Also in the box

- **Server globe.** On every Roblox join and teleport a 3D Earth turns to the data centre you are connecting to, and stays until you have loaded in.
- **A start-up screen worth watching.** The engine ignites on every launch, and shows the real download progress during an update.
- **Updates itself.** Close the app and open it again; that is the whole update.

## Install

1. Download `PryisceEngine-x.y.z.zip` from the [latest release](https://github.com/pryisce/pryisce-engine/releases/latest).
2. Unzip it anywhere and run `Pryisce.exe`.

Needs Windows 10 or 11 (64-bit) and the [.NET 10 Desktop Runtime](https://dotnet.microsoft.com/download/dotnet/10.0).

## Is it safe?

You should not have to take anyone's word for it, so here is what you can check yourself.

**Scan the download.** Every release is one zip file. Its fingerprint is below; look it up, or upload the zip yourself, on any scanner.

<!-- scan:start -->
| | |
|---|---|
| Version | `0.0.17` |
| File | `PryisceEngine-0.0.17.zip` |
| SHA-256 | `7B058BFB53F384A73602EC8D4B1B63988E8A317F6759CFBCECA31E56230FC7A6` |
| VirusTotal | [look up this file](https://www.virustotal.com/gui/file/7B058BFB53F384A73602EC8D4B1B63988E8A317F6759CFBCECA31E56230FC7A6) |
| Triage | [look up this file](https://tria.ge/s?q=7B058BFB53F384A73602EC8D4B1B63988E8A317F6759CFBCECA31E56230FC7A6) |
<!-- scan:end -->

**Scans already run** (7 October 2026, on `Pryisce.exe`, the program's launcher)

| Scanner | Result | Scanned | Report |
|---|---|---|---|
| VirusTotal | **0 of 71** security vendors flagged it | `Pryisce.exe` from version 0.0.16 | [open report](https://www.virustotal.com/gui/file/706a5b2969a77725f8e8f87b6a574f8c3a87f190dbfaf01b5f8b33104276e478) |
| Triage sandbox | **3 / 10** overall (static 3, behaviour 1 on Windows 10 and Windows 11), where 10 is known malware | `Pryisce.exe` from an earlier version | [open report](https://tria.ge/261007-ef13ea1zay) |

These cover the versions named, not every later one; each release is a new file. Use the fingerprint above to check the one you downloaded.

A brand-new, unsigned program that sends key presses (the auto clicker) can be flagged by a few scanners on behaviour alone. Read what a report actually says rather than only the number.

**What it does and does not do**

- No account, no telemetry, nothing collected about you.
- No code is injected into any game and no game memory is read.
- The auto clicker, always sprint and anti stick drift send ordinary keyboard and mouse input.
- The crosshair swaps three pointer pictures in Roblox's folder, keeps the originals, and puts them back when you detach it.
- Every tweak is saved in a snapshot first and can be undone.
- Updates are signed: a copy ignores any update or instruction that does not carry the publisher's signature.
- It goes online only to check GitHub for updates, to look up where a game server is, and to read public Roblox information (names, pictures, crosshair decals).

> [!WARNING]
> Auto clickers, input helpers and modified game files can be against a game's rules. Using those features online is your own decision and your own risk; an account can be actioned for it. The measuring, diagnosing and optimizing features do not touch the game.

---

<div align="center">
<sub>Pryisce Engine is not affiliated with Roblox Corporation or any game publisher.</sub>
</div>