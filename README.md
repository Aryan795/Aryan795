<div align="center">

<img src="./assets/header.svg" alt="Aryan Pandey — self-hosted systems, embedded, home automation" width="100%" />

<a href="https://www.linkedin.com/in/aryan-pandey817">
  <img src="https://img.shields.io/badge/LinkedIn-58a6ff?style=flat-square&labelColor=010409" alt="LinkedIn" /></a>
<a href="mailto:aryanpandey817@gmail.com">
  <img src="https://img.shields.io/badge/Email-0d1117?style=flat-square&logo=gmail&logoColor=3fb950&labelColor=010409" alt="Email" /></a>
<a href="https://bench.homelabweb.space">
  <img src="https://img.shields.io/badge/Portfolio-0d1117?style=flat-square&logo=firefoxbrowser&logoColor=adbac7&labelColor=010409" alt="Portfolio" /></a>
<a href="https://github.com/Aryan795?tab=repositories">
  <img src="https://img.shields.io/badge/Repositories-0d1117?style=flat-square&logo=github&logoColor=adbac7&labelColor=010409" alt="Repositories" /></a>

</div>

---

## `$ whoami`

I build things that run on hardware I own. Most of my work orbits a home-automation and
self-hosting stack — a Proxmox host, a Raspberry Pi doing routing and DNS, a fleet of ESPHome
devices — plus the tools I needed along the way and couldn't find anywhere.

A few of those turned into protocol reverse-engineering projects. B.Tech CSE at Lovely
Professional University. I care about systems that keep running when nobody is watching them.

---

## `$ git log --author=Aryan795 --merged`

Contributions to **[Suwayomi-WebUI](https://github.com/Suwayomi/Suwayomi-WebUI)**, the web client
for a self-hosted manga server:

| PR | Change | State |
|---|---|---|
| [#1159](https://github.com/Suwayomi/Suwayomi-WebUI/pull/1159) | Fuzzy search across the library | ![merged](https://img.shields.io/badge/merged-8957e5?style=flat-square) |
| [#1160](https://github.com/Suwayomi/Suwayomi-WebUI/pull/1160) | Autocomplete in the search bar | ![merged](https://img.shields.io/badge/merged-8957e5?style=flat-square) |
| [#1161](https://github.com/Suwayomi/Suwayomi-WebUI/pull/1161) | Remembered search history | ![open](https://img.shields.io/badge/open-3fb950?style=flat-square) |

---

## `$ ls -la ~/projects`

<table>
<tr>
<td width="50%" valign="top">

### [warp-local-adapter](https://github.com/Aryan795/warp-local-adapter)

Warp terminal's AI agent loop runs on Warp's servers, so the app refuses `localhost`. This
impersonates that server locally and forwards to any OpenAI-compatible endpoint. Wire protocol
reverse-engineered from scratch against a patched client.

`protobuf` · `axum` · `reverse engineering`

</td>
<td width="50%" valign="top">

### [jarvis](https://github.com/Aryan795/jarvis)

Offline-first voice assistant for Home Assistant. OpenWakeWord and Piper TTS on a Raspberry Pi,
Faster-Whisper STT behind FastAPI. A scored intent router over two FAISS indexes and a regex rule
engine keeps ~85% of fallbacks local on Gemma 3:4B at 200–400 ms, with only ~5% escalating to a
cloud API.

`Python` · `FastAPI` · `FAISS` · `Ollama` · `SQLite`

</td>
</tr>
<tr>
<td width="50%" valign="top">

### [webapp-dash](https://github.com/Aryan795/webapp-dash)

Wall-tablet dashboard for Home Assistant. The HA token never reaches the tablet — a Node proxy
holds it and fans state out over a tokenless socket, behind a server-side service allowlist.
Built to run unattended for months.

`React` · `TypeScript` · `Node` · `Kotlin`

</td>
<td width="50%" valign="top">

### [bench](https://github.com/Aryan795/bench)

Self-hosted site for projects and writing, with an admin panel. For people who make things in
more than one discipline and want a single coherent index. One `docker compose up`.

`Node` · `Express` · `MongoDB`

</td>
</tr>
<tr>
<td width="50%" valign="top">

### [Ha_fan_integration](https://github.com/Aryan795/Ha_fan_integration)

Local Home Assistant integration for Atomberg fans over LAN UDP — fan, light, sleep mode and
timer entities, with no cloud round-trip.

`Python` · `HACS`

</td>
<td width="50%" valign="top">

### [Car_Counter](https://github.com/Aryan795/Car_Counter)

Real-time vehicle detection and counting from video.

`Python` · `OpenCV` · `YOLOv8`

</td>
</tr>
</table>

---

## `$ systemctl status homelab`

Two long-running builds that don't live in a repo, and the infrastructure under everything above.

**Self-hosted infrastructure platform** — a virtualization stack on Proxmox with a TrueNAS storage
VM exporting NFS to LXC containers and Docker Compose services, Jellyfin and Grafana included.
Services are published through a Caddy reverse proxy with automatic TLS over a Cloudflare Tunnel,
so there is zero inbound port forwarding, plus a Tailscale mesh and a self-hosted exit node for
remote access. Network-wide DNS filtering runs on AdGuard Home behind a custom OpenWrt router on a
Raspberry Pi 3B+.

**Smart switch retrofit** — custom circuits that convert manual wall switches into smart switches
using ESP microcontrollers and relays, keeping full manual operation even when the controller or
network is down. Integrated into Home Assistant over ESPHome and MQTT with real-time state sync
between physical presses and app actions. Two years of daily use.

<details>
<summary><b>What's actually running</b></summary>

<br/>

| Layer | Detail |
|---|---|
| **Compute** | Proxmox on an i5 host · TrueNAS with a 3×500 GB RAIDZ1 pool · LXC + Docker Compose |
| **Network** | OpenWrt on a Raspberry Pi 3B+ · Caddy with automatic TLS · Cloudflare Tunnel · Tailscale mesh and exit node · AdGuard Home |
| **Automation** | Home Assistant OS on a Pi 4 · ~22 ESPHome devices · 79 automations · MQTT and Zigbee |
| **Media & making** | Jellyfin · Suwayomi manga server · Anycubic Kobra 2 Neo on Klipper |

</details>

---

## `$ cat /etc/stack`

<div align="center">

![Python](https://img.shields.io/badge/Python-0d1117?style=flat-square&logo=python&logoColor=3fb950&labelColor=010409)
![C++](https://img.shields.io/badge/C++-0d1117?style=flat-square&logo=cplusplus&logoColor=3fb950&labelColor=010409)
![C](https://img.shields.io/badge/C-0d1117?style=flat-square&logo=c&logoColor=3fb950&labelColor=010409)
![Java](https://img.shields.io/badge/Java-0d1117?style=flat-square&logo=openjdk&logoColor=3fb950&labelColor=010409)
![JavaScript](https://img.shields.io/badge/JavaScript-0d1117?style=flat-square&logo=javascript&logoColor=3fb950&labelColor=010409)
![TypeScript](https://img.shields.io/badge/TypeScript-0d1117?style=flat-square&logo=typescript&logoColor=3fb950&labelColor=010409)

![FastAPI](https://img.shields.io/badge/FastAPI-0d1117?style=flat-square&logo=fastapi&logoColor=58a6ff&labelColor=010409)
![Node.js](https://img.shields.io/badge/Node.js-0d1117?style=flat-square&logo=nodedotjs&logoColor=58a6ff&labelColor=010409)
![Express](https://img.shields.io/badge/Express-0d1117?style=flat-square&logo=express&logoColor=58a6ff&labelColor=010409)
![React](https://img.shields.io/badge/React-0d1117?style=flat-square&logo=react&logoColor=58a6ff&labelColor=010409)
![PyTorch](https://img.shields.io/badge/PyTorch-0d1117?style=flat-square&logo=pytorch&logoColor=58a6ff&labelColor=010409)
![TensorFlow](https://img.shields.io/badge/TensorFlow-0d1117?style=flat-square&logo=tensorflow&logoColor=58a6ff&labelColor=010409)
![scikit-learn](https://img.shields.io/badge/scikit--learn-0d1117?style=flat-square&logo=scikitlearn&logoColor=58a6ff&labelColor=010409)
![OpenCV](https://img.shields.io/badge/OpenCV-0d1117?style=flat-square&logo=opencv&logoColor=58a6ff&labelColor=010409)

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-0d1117?style=flat-square&logo=postgresql&logoColor=adbac7&labelColor=010409)
![MySQL](https://img.shields.io/badge/MySQL-0d1117?style=flat-square&logo=mysql&logoColor=adbac7&labelColor=010409)
![MongoDB](https://img.shields.io/badge/MongoDB-0d1117?style=flat-square&logo=mongodb&logoColor=adbac7&labelColor=010409)
![SQLite](https://img.shields.io/badge/SQLite-0d1117?style=flat-square&logo=sqlite&logoColor=adbac7&labelColor=010409)

![Linux](https://img.shields.io/badge/Linux-0d1117?style=flat-square&logo=linux&logoColor=f0883e&labelColor=010409)
![Docker](https://img.shields.io/badge/Docker-0d1117?style=flat-square&logo=docker&logoColor=f0883e&labelColor=010409)
![Kubernetes](https://img.shields.io/badge/Kubernetes-0d1117?style=flat-square&logo=kubernetes&logoColor=f0883e&labelColor=010409)
![Proxmox](https://img.shields.io/badge/Proxmox-0d1117?style=flat-square&logo=proxmox&logoColor=f0883e&labelColor=010409)
![Nginx](https://img.shields.io/badge/Nginx-0d1117?style=flat-square&logo=nginx&logoColor=f0883e&labelColor=010409)
![Grafana](https://img.shields.io/badge/Grafana-0d1117?style=flat-square&logo=grafana&logoColor=f0883e&labelColor=010409)
![Prometheus](https://img.shields.io/badge/Prometheus-0d1117?style=flat-square&logo=prometheus&logoColor=f0883e&labelColor=010409)
![AWS](https://img.shields.io/badge/AWS-f0883e?style=flat-square&labelColor=010409)

![Home Assistant](https://img.shields.io/badge/Home%20Assistant-0d1117?style=flat-square&logo=homeassistant&logoColor=41BDF5&labelColor=010409)
![ESPHome](https://img.shields.io/badge/ESPHome-0d1117?style=flat-square&logo=esphome&logoColor=41BDF5&labelColor=010409)
![MQTT](https://img.shields.io/badge/MQTT-0d1117?style=flat-square&logo=mqtt&logoColor=41BDF5&labelColor=010409)
![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-0d1117?style=flat-square&logo=raspberrypi&logoColor=41BDF5&labelColor=010409)
![Arduino](https://img.shields.io/badge/Arduino-0d1117?style=flat-square&logo=arduino&logoColor=41BDF5&labelColor=010409)
![OpenWrt](https://img.shields.io/badge/OpenWrt-0d1117?style=flat-square&logo=openwrt&logoColor=41BDF5&labelColor=010409)

</div>

---

## `$ cat stats.json`

<div align="center">

<img src="./assets/stats.svg" alt="GitHub statistics" width="520" />

</div>

> Generated inside this repo by a [GitHub Action](.github/workflows/stats.yml) rather than a
> third-party service, so it can't break when someone else's free tier runs out.

---

## `$ cat credentials.txt`

**Education** — B.Tech, Computer Science and Engineering · Lovely Professional University,
Phagwara · 2024–2028 · **CGPA 9.50**

**Certificates** — Oracle Agentic AI Certified Foundations Associate (2026) · Database Management
Systems, Infosys Springboard (2026) · Programming Using C++, Infosys Springboard (2025) · Data
Structures & Algorithms, CipherSchools (2026)

**Problem solving** — 200+ LeetCode problems solved, primarily in C++ (116 medium, 38 hard),
74-day maximum daily streak and the 100 Days Badge 2025

---

## `$ ./contributions --animate`

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Aryan795/Aryan795/output/snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Aryan795/Aryan795/output/snake.svg" />
  <img alt="Contribution graph animation" src="https://raw.githubusercontent.com/Aryan795/Aryan795/output/snake.svg" />
</picture>

</div>
