#!/usr/bin/env python3
"""Render a self-contained stats card SVG from the GitHub GraphQL API.

Runs in CI (GITHUB_TOKEN) or locally (`gh auth token`). Output is committed to the
repo, so the card never depends on a third-party service staying up.
"""
import json, os, subprocess, sys, urllib.request
from html import escape

LOGIN = os.environ.get("STATS_LOGIN", "Aryan795")
# Languages the profile advertises. Anything else (build files, vendored trees,
# languages not claimed as a skill) is left out of the chart.
INCLUDE_LANGS = {
    l.strip().lower()
    for l in os.environ.get(
        "INCLUDE_LANGS", "python,c++,c,java,javascript,typescript,kotlin,shell,html,css"
    ).split(",")
    if l.strip()
}
OUT = os.environ.get("STATS_OUT", "assets/stats.svg")

QUERY = """
query($login:String!){
  user(login:$login){
    followers{totalCount}
    contributionsCollection{contributionCalendar{totalContributions}}
    pullRequests(states:MERGED, first:100){
      totalCount
      nodes{ repository{ owner{ login } } }
    }
    repositories(first:100, ownerAffiliations:OWNER, isFork:false, privacy:PUBLIC){
      totalCount
      nodes{
        stargazerCount
        languages(first:10, orderBy:{field:SIZE,direction:DESC}){
          edges{ size node{ name color } }
        }
      }
    }
  }
}
"""


def token():
    for var in ("GITHUB_TOKEN", "GH_TOKEN"):
        if os.environ.get(var):
            return os.environ[var]
    return subprocess.check_output(["gh", "auth", "token"], text=True).strip()


def fetch():
    body = json.dumps({"query": QUERY, "variables": {"login": LOGIN}}).encode()
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=body,
        headers={
            "Authorization": f"bearer {token()}",
            "Content-Type": "application/json",
            "User-Agent": "profile-stats-card",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        payload = json.load(r)
    if "errors" in payload:
        sys.exit(f"GraphQL error: {payload['errors']}")
    return payload["data"]["user"]


def summarise(user):
    repos = user["repositories"]["nodes"]
    stars = sum(r["stargazerCount"] for r in repos)
    langs = {}
    for repo in repos:
        for edge in repo["languages"]["edges"]:
            name = edge["node"]["name"]
            if name.lower() not in INCLUDE_LANGS:
                continue
            entry = langs.setdefault(name, {"size": 0, "color": edge["node"]["color"] or "#8b949e"})
            entry["size"] += edge["size"]
    upstream = sum(
        1
        for pr in user["pullRequests"]["nodes"]
        if pr["repository"]["owner"]["login"].lower() != LOGIN.lower()
    )
    total = sum(v["size"] for v in langs.values()) or 1
    top = sorted(langs.items(), key=lambda kv: -kv[1]["size"])[:8]
    return {
        "repos": user["repositories"]["totalCount"],
        "stars": stars,
        "merged": user["pullRequests"]["totalCount"],
        "upstream": upstream,
        "followers": user["followers"]["totalCount"],
        "contribs": user["contributionsCollection"]["contributionCalendar"]["totalContributions"],
        "langs": [(n, v["size"] * 100.0 / total, v["color"]) for n, v in top],
    }


W, H = 520, 292
GREEN, BRIGHT, DIM, RED = "#3fb950", "#adbac7", "#6e7681", "#3fb950"


def render(s):
    tiles = [
        ("contributions", s["contribs"], "past year"),
        ("public repos", s["repos"], "sources"),
        ("merged PRs", s["merged"], "all time"),
        ("merged upstream", s["upstream"], "others' repos"),
    ]
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
        f'role="img" aria-label="GitHub statistics for {escape(LOGIN)}">',
        "<defs>",
        '<clipPath id="fr"><rect x="0" y="0" width="%d" height="%d" rx="10"/></clipPath>' % (W, H),
        '<pattern id="scan" width="4" height="4" patternUnits="userSpaceOnUse">',
        '<rect width="4" height="1" fill="#000" opacity=".55"/></pattern>',
        '<linearGradient id="bgg" x1="0" y1="0" x2="0" y2="1">',
        '<stop offset="0%" stop-color="#0d1117"/><stop offset="100%" stop-color="#010409"/>',
        "</linearGradient>",
        "<style>",
        "text{font-family:'SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace}",
        f".prompt{{font-size:12px;fill:{RED}}}.path{{fill:{DIM}}}.cmd{{fill:{BRIGHT}}}",
        f".label{{fill:{DIM};font-size:10px}}",
        f".value{{fill:#e6edf3;font-size:21px;font-weight:700}}",
        f".sub{{fill:#6e7681;font-size:8.5px}}",
        f".lang{{fill:{BRIGHT};font-size:9.5px}}",
        ".fx{animation:in .5s ease backwards}",
        "@keyframes in{from{opacity:0}to{opacity:1}}",
        "@keyframes grow{from{transform:scaleX(0)}to{transform:scaleX(1)}}",
        ".bar{transform-origin:left center;animation:grow .9s cubic-bezier(.3,.8,.4,1) backwards}",
        ".cur{fill:%s;animation:blink 1.05s steps(1) infinite}" % GREEN,
        "@keyframes blink{50%{opacity:0}}",
        "@media (prefers-reduced-motion: reduce){.fx,.bar,.cur{animation:none}}",
        "</style>",
        "</defs>",
        '<g clip-path="url(#fr)">',
        f'<rect width="{W}" height="{H}" fill="url(#bgg)"/>',
        '<text class="prompt" x="22" y="30">aryan@homelab<tspan class="path">:~$</tspan>'
        '<tspan class="cmd" dx="7">cat stats.json</tspan></text>',
        f'<line x1="22" y1="42" x2="{W-22}" y2="42" stroke="#21262d"/>',
    ]

    for i, (label, value, sub) in enumerate(tiles):
        x = 22 + (i % 2) * 250
        y = 72 + (i // 2) * 60
        d = 0.10 + i * 0.07
        out += [
            f'<g class="fx" style="animation-delay:{d:.2f}s">',
            f'<text class="label" x="{x}" y="{y}"><tspan fill="{GREEN}">&#9656;</tspan> {label}</text>',
            f'<text class="value" x="{x}" y="{y+24}">{value:,}</text>',
            f'<text class="sub" x="{x+len(f"{value:,}")*13+8}" y="{y+24}">{sub}</text>',
            "</g>",
        ]

    by = 212
    out.append(f'<text class="label fx" x="22" y="{by-9}" style="animation-delay:.45s"><tspan fill="{GREEN}">&#9656;</tspan> languages</text>')
    bw, bx = W - 44, 22.0
    out.append(f'<clipPath id="r"><rect x="22" y="{by}" width="{bw}" height="8" rx="4"/></clipPath>')
    out.append('<g clip-path="url(#r)">')
    for i, (_, pct, color) in enumerate(s["langs"]):
        seg = bw * pct / 100.0
        out.append(
            f'<rect class="bar" x="{bx:.1f}" y="{by}" width="{seg:.1f}" height="8" fill="{color}" '
            f'style="animation-delay:{.5+i*.08:.2f}s"/>'
        )
        bx += seg
    if bx < 22 + bw - 0.5:
        out.append(
            f'<rect class="bar" x="{bx:.1f}" y="{by}" width="{22+bw-bx:.1f}" height="8" '
            f'fill="{DIM}" opacity=".3" style="animation-delay:.9s"/>'
        )
    out.append("</g>")

    lx, ly = 22, by + 20
    for i, (name, pct, color) in enumerate(s["langs"]):
        label = f"{name} {pct:.1f}%"
        span = 22 + len(label) * 5.4
        if lx + span > W - 22:          # wrap onto the next legend row
            lx, ly = 22, ly + 16
        out += [
            f'<g class="fx" style="animation-delay:{.62+i*.05:.2f}s">',
            f'<rect x="{lx}" y="{ly}" width="7" height="7" fill="{color}"/>',
            f'<text class="lang" x="{lx+12}" y="{ly+7}">{escape(label)}</text>',
            "</g>",
        ]
        lx += span
    out.append(f'<rect class="cur" x="{W-34}" y="{H-24}" width="8" height="13"/>')
    out.append(f'<rect width="{W}" height="{H}" fill="url(#scan)" opacity=".13"/>')
    out.append(f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="10" fill="none" stroke="#30363d" stroke-width="1.5"/>')
    out.append("</g></svg>")
    return "\n".join(out)


if __name__ == "__main__":
    stats = summarise(fetch())
    os.makedirs(os.path.dirname(OUT) or ".", exist_ok=True)
    with open(OUT, "w") as fh:
        fh.write(render(stats))
    print(f"wrote {OUT}: {stats}")
