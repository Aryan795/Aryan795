#!/usr/bin/env python3
"""Render the animated terminal header SVG.

Pure CSS animation inside the SVG, no scripting, so it still plays when GitHub
serves the file through camo as an <img>. Fonts fall back to the system
monospace stack because an <img>-loaded SVG cannot fetch a webfont.
"""
import os, random
from html import escape

OUT = os.environ.get("HEADER_OUT", "assets/header.svg")
W, H = 900, 290
BAR = 36
GLYPHS = "0123456789ABCDEF<>/\\|{}[]$#%&*+=~^_"
GREEN, DIM, RED, CYAN = "#3fb950", "#2d4f3a", "#f85149", "#58a6ff"

random.seed(7)  # keep the rain identical between runs so diffs stay clean


def rain():
    """Background hex/code columns drifting downward."""
    out = []
    for col in range(30):
        x = 14 + col * 30
        glyphs = "".join(random.choice(GLYPHS) for _ in range(9))
        dur = round(random.uniform(7.0, 15.0), 1)
        delay = round(random.uniform(-14.0, 0.0), 1)
        op = round(random.uniform(0.03, 0.085), 3)
        out.append(
            f'<text class="rain" x="{x}" y="-10" opacity="{op}" '
            f'style="animation-duration:{dur}s;animation-delay:{delay}s">'
        )
        for i, g in enumerate(glyphs):
            out.append(f'<tspan x="{x}" dy="{0 if i == 0 else 19}">{escape(g)}</tspan>')
        out.append("</text>")
    return "\n".join(out)


def build():
    name = "ARYAN PANDEY"
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"
     role="img" aria-label="Aryan Pandey - terminal header">
<title>aryan@homelab: ~/profile</title>
<defs>
  <clipPath id="frame"><rect x="0" y="0" width="{W}" height="{H}" rx="12"/></clipPath>
  <clipPath id="screen"><rect x="0" y="{BAR}" width="{W}" height="{H-BAR}"/></clipPath>
  <clipPath id="type" clipPathUnits="userSpaceOnUse">
    <rect class="reveal" x="40" y="60" width="430" height="26"/>
  </clipPath>
  <clipPath id="type2" clipPathUnits="userSpaceOnUse">
    <rect class="reveal2" x="40" y="214" width="640" height="26"/>
  </clipPath>
  <pattern id="scan" width="4" height="4" patternUnits="userSpaceOnUse">
    <rect width="4" height="1" fill="#000" opacity=".55"/>
  </pattern>
  <linearGradient id="glow" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#0d1117"/><stop offset="100%" stop-color="#010409"/>
  </linearGradient>
  <style>
    text{{font-family:'SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace}}
    .rain{{font-size:16px;fill:{GREEN};animation-name:fall;animation-timing-function:linear;
      animation-iteration-count:infinite}}
    @keyframes fall{{from{{transform:translateY(0)}}to{{transform:translateY({H+190}px)}}}}
    .reveal{{transform-origin:40px 0;animation:type 1.6s steps(24) .2s backwards}}
    .reveal2{{transform-origin:40px 0;animation:type 2.2s steps(34) 2.0s backwards}}
    @keyframes type{{from{{transform:scaleX(0)}}to{{transform:scaleX(1)}}}}
    .cmd{{font-size:17px;fill:#adbac7}}
    .arg{{fill:#adbac7}}
    .sub{{font-size:14px;fill:#768390}}
    .name{{font-size:52px;font-weight:700;letter-spacing:.04em}}
    .base{{fill:#e6edf3}}
    .gr{{fill:{RED};mix-blend-mode:screen;animation:gr 3.4s steps(1) infinite}}
    .gc{{fill:{CYAN};mix-blend-mode:screen;animation:gc 3.4s steps(1) infinite}}
    @keyframes gr{{0%,86%,100%{{transform:translate(0,0);opacity:0}}
      88%{{transform:translate(-3px,1px);opacity:.45}}91%{{transform:translate(2px,-1px);opacity:.35}}
      94%{{transform:translate(-2px,0);opacity:.6}}96%{{opacity:0}}}}
    @keyframes gc{{0%,86%,100%{{transform:translate(0,0);opacity:0}}
      89%{{transform:translate(3px,-1px);opacity:.4}}92%{{transform:translate(-2px,1px);opacity:.6}}
      95%{{transform:translate(2px,0);opacity:.5}}97%{{opacity:0}}}}
    .flick{{animation:flick 6s ease-in-out infinite}}
    @keyframes flick{{0%,88%,100%{{opacity:1}}90%{{opacity:.88}}92%{{opacity:1}}94%{{opacity:.85}}}}
    .cur{{fill:{GREEN};animation:blink 1.05s steps(1) infinite}}
    @keyframes blink{{50%{{opacity:0}}}}
    .fade{{animation:fade .9s ease 2.9s backwards}}
    @keyframes fade{{from{{opacity:0}}to{{opacity:1}}}}
    @media (prefers-reduced-motion: reduce){{
      .rain,.reveal,.reveal2,.gr,.gc,.flick,.cur,.fade{{animation:none}}
      .gr,.gc{{opacity:0}}}}
  </style>
</defs>

<g clip-path="url(#frame)">
  <rect width="{W}" height="{H}" fill="url(#glow)"/>
  <g clip-path="url(#screen)">{rain()}</g>

  <!-- window chrome -->
  <rect width="{W}" height="{BAR}" fill="#161b22"/>
  <line x1="0" y1="{BAR}" x2="{W}" y2="{BAR}" stroke="#21262d"/>
  <circle cx="20" cy="18" r="5.5" fill="#ff5f56"/>
  <circle cx="40" cy="18" r="5.5" fill="#ffbd2e"/>
  <circle cx="60" cy="18" r="5.5" fill="#27c93f"/>
  <text x="{W/2}" y="23" text-anchor="middle" font-size="12.5" fill="#6e7681">aryan@homelab: ~/profile</text>

  <g class="flick">
    <!-- prompt one -->
    <g clip-path="url(#type)">
      <text class="cmd" x="40" y="79">
        <tspan fill="{GREEN}">aryan@homelab</tspan><tspan fill="#6e7681">:~$</tspan>
        <tspan class="arg"> whoami --verbose</tspan>
      </text>
    </g>

    <!-- glitched name -->
    <g class="fade">
      <text class="name gr" x="40" y="146">{name}</text>
      <text class="name gc" x="40" y="146">{name}</text>
      <text class="name base" x="40" y="146">{name}</text>
      <text class="sub" x="40" y="180">self-hosted systems &#183; applied ML &#183; embedded &#183; home automation</text>
    </g>

    <!-- prompt two -->
    <g clip-path="url(#type2)">
      <text class="cmd" x="40" y="233">
        <tspan fill="{GREEN}">aryan@homelab</tspan><tspan fill="#6e7681">:~$</tspan>
        <tspan class="arg"> cat about.txt</tspan>
      </text>
    </g>
    <text class="sub fade" x="40" y="258">&#187; two PRs merged upstream &#183; 22 esphome nodes &#183; 79 automations</text>
    <rect class="cur" x="376" y="218" width="9" height="17"/>
  </g>

  <rect width="{W}" height="{H}" fill="url(#scan)" opacity=".13"/>
  <rect x="1" y="1" width="{W-2}" height="{H-2}" rx="12" fill="none" stroke="#30363d" stroke-width="1.5"/>
</g>
</svg>"""


if __name__ == "__main__":
    os.makedirs(os.path.dirname(OUT) or ".", exist_ok=True)
    open(OUT, "w").write(build())
    print(f"wrote {OUT}")
