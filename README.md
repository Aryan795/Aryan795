<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:7aa2f7,50:bb9af7,100:7dcfff&height=200&section=header&text=Aryan%20Pandey&fontSize=46&fontColor=ffffff&fontAlignY=34&desc=Self-hosted%20systems%20%C2%B7%20Rust%20%C2%B7%20Home%20automation&descSize=15&descAlignY=54" alt="" />

<a href="https://github.com/Aryan795">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=19&pause=1400&color=7AA2F7&center=true&vCenter=true&width=720&height=42&lines=I+build+things+that+run+on+hardware+I+own;Rust+%C2%B7+reverse-engineered+Warp%27s+agent+protocol;Home+Assistant+%C2%B7+22+ESPHome+devices+%C2%B7+79+automations;2+PRs+merged+into+Suwayomi-WebUI" alt="I build things that run on hardware I own" />
</a>

<br/>

<a href="https://www.linkedin.com/in/aryan-pandey817">
  <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
<a href="https://github.com/Aryan795?tab=repositories">
  <img src="https://img.shields.io/badge/Repositories-181717?style=for-the-badge&logo=github&logoColor=white" alt="Repositories" /></a>
<img src="https://img.shields.io/badge/Based%20in-India-FF9933?style=for-the-badge&logoColor=white" alt="Based in India" />

</div>

---

## 🧭 About

I build things that run on hardware I own. Most of my work orbits a home-automation and
self-hosting stack — a Proxmox host, a Raspberry Pi doing routing and DNS, a fleet of ESPHome
devices — plus the tools I needed along the way and couldn't find anywhere.

A few of those turned into protocol reverse-engineering projects. CS undergrad in India.
I care about systems that keep running when nobody is watching them.

---

## 🔀 Merged upstream

Contributions to **[Suwayomi-WebUI](https://github.com/Suwayomi/Suwayomi-WebUI)**, the web client
for a self-hosted manga server:

| PR | What it does | Status |
|---|---|---|
| [#1159](https://github.com/Suwayomi/Suwayomi-WebUI/pull/1159) | Fuzzy search across the library | ![merged](https://img.shields.io/badge/merged-8957e5?style=flat-square) |
| [#1160](https://github.com/Suwayomi/Suwayomi-WebUI/pull/1160) | Autocomplete in the search bar | ![merged](https://img.shields.io/badge/merged-8957e5?style=flat-square) |
| [#1161](https://github.com/Suwayomi/Suwayomi-WebUI/pull/1161) | Remembered search history | ![open](https://img.shields.io/badge/open-3fb950?style=flat-square) |

---

## 🔧 Selected work

<table>
<tr>
<td width="50%" valign="top">

### 🦀 [warp-local-adapter](https://github.com/Aryan795/warp-local-adapter)

Warp terminal's AI agent loop runs on Warp's servers, so the app refuses `localhost`.
This impersonates that server locally and forwards to any OpenAI-compatible endpoint.
Wire protocol reverse-engineered from scratch.

`Rust` `protobuf` `axum`

</td>
<td width="50%" valign="top">

### 📱 [webapp-dash](https://github.com/Aryan795/webapp-dash)

Wall-tablet dashboard for Home Assistant. The HA token never reaches the tablet — a Node
proxy holds it and fans state out over a tokenless socket, behind a server-side service
allowlist. Built to run unattended for months.

`React` `TypeScript` `Node` `Kotlin`

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🎙️ [jarvis](https://github.com/Aryan795/jarvis)

Offline voice assistant for Home Assistant. ESP32-S3 satellite handles wake word, a CPU-only
brain runs on an LXC, and no generative model sits in the action path. Design is settled and
documented; the code is still a scaffold.

`Python` `ESP32-S3`

</td>
<td width="50%" valign="top">

### 📚 [bench](https://github.com/Aryan795/bench)

Self-hosted site for projects and writing, with an admin panel. For people who make things in
more than one discipline and want a single coherent index. One `docker compose up`.

`Node` `Express` `MongoDB`

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🌀 [Ha_fan_integration](https://github.com/Aryan795/Ha_fan_integration)

Local Home Assistant integration for Atomberg fans over LAN UDP — fan, light, sleep mode and
timer entities, with no cloud round-trip.

`Python` `HACS`

</td>
<td width="50%" valign="top">

### 🚗 [Car_Counter](https://github.com/Aryan795/Car_Counter)

Real-time vehicle detection and counting from video.

`Python` `OpenCV` `YOLOv8`

</td>
</tr>
</table>

---

## 🏠 The homelab

<details>
<summary><b>The thing most of my code exists to serve</b> — click to expand</summary>

<br/>

| Layer | What runs there |
|---|---|
| **Compute** | Proxmox on an i5 box · TrueNAS with a 3×500 GB RAIDZ1 pool · everything in Docker Compose |
| **Network** | OpenWrt on a Raspberry Pi 3B+ · reverse proxy and a mesh VPN for remote access · network-wide DNS filtering |
| **Automation** | Home Assistant OS on a Pi 4 · ~22 ESPHome devices · 79 automations · MQTT and Zigbee |
| **Media & making** | Jellyfin · a Suwayomi manga server · an Anycubic Kobra 2 Neo running Klipper |

</details>

---

## 🛠️ Stack

<div align="center">

**Languages**

![Rust](https://img.shields.io/badge/Rust-000000?style=for-the-badge&logo=rust&logoColor=white)
![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white)
![C++](https://img.shields.io/badge/C%2B%2B-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white)
![Kotlin](https://img.shields.io/badge/Kotlin-7F52FF?style=for-the-badge&logo=kotlin&logoColor=white)

**Infrastructure**

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Proxmox](https://img.shields.io/badge/Proxmox-E57000?style=for-the-badge&logo=proxmox&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![OpenWrt](https://img.shields.io/badge/OpenWrt-00B5E2?style=for-the-badge&logo=openwrt&logoColor=white)
![Caddy](https://img.shields.io/badge/Caddy-1F88C0?style=for-the-badge&logo=caddy&logoColor=white)

**Hardware & home automation**

![Home Assistant](https://img.shields.io/badge/Home%20Assistant-41BDF5?style=for-the-badge&logo=home-assistant&logoColor=white)
![ESPHome](https://img.shields.io/badge/ESPHome-000000?style=for-the-badge&logo=esphome&logoColor=white)
![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-C51A4A?style=for-the-badge&logo=raspberrypi&logoColor=white)
![Arduino](https://img.shields.io/badge/Arduino-00979D?style=for-the-badge&logo=arduino&logoColor=white)
![MQTT](https://img.shields.io/badge/MQTT-660066?style=for-the-badge&logo=mqtt&logoColor=white)

**Application & ML**

![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Node.js](https://img.shields.io/badge/Node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)

</div>

---

## 📊 Stats

<div align="center">

<img src="./assets/stats.svg" alt="GitHub statistics" width="520" />

</div>

> This card is generated inside this repo by a [GitHub Action](.github/workflows/stats.yml)
> rather than a third-party service, so it can't break when someone else's free tier runs out.

---

## 🐍 Contribution graph

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Aryan795/Aryan795/output/snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Aryan795/Aryan795/output/snake.svg" />
  <img alt="Snake eating the contribution graph" src="https://raw.githubusercontent.com/Aryan795/Aryan795/output/snake.svg" />
</picture>

</div>

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:7dcfff,50:bb9af7,100:7aa2f7&height=120&section=footer" alt="" />

</div>
