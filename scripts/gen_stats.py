#!/usr/bin/env python3
"""Render a self-contained stats card SVG from the GitHub GraphQL API.

Runs in CI (GITHUB_TOKEN) or locally (`gh auth token`). Output is committed to the
repo, so the card never depends on a third-party service staying up.
"""
import json, os, subprocess, sys, urllib.request
from html import escape

LOGIN = os.environ.get("STATS_LOGIN", "Aryan795")
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
            entry = langs.setdefault(name, {"size": 0, "color": edge["node"]["color"] or "#8b949e"})
            entry["size"] += edge["size"]
    upstream = sum(
        1
        for pr in user["pullRequests"]["nodes"]
        if pr["repository"]["owner"]["login"].lower() != LOGIN.lower()
    )
    total = sum(v["size"] for v in langs.values()) or 1
    top = sorted(langs.items(), key=lambda kv: -kv[1]["size"])[:5]
    return {
        "repos": user["repositories"]["totalCount"],
        "stars": stars,
        "merged": user["pullRequests"]["totalCount"],
        "upstream": upstream,
        "followers": user["followers"]["totalCount"],
        "contribs": user["contributionsCollection"]["contributionCalendar"]["totalContributions"],
        "langs": [(n, v["size"] * 100.0 / total, v["color"]) for n, v in top],
    }


W, H = 460, 250


def render(s):
    tiles = [
        ("Contributions", s["contribs"], "past year"),
        ("Public repos", s["repos"], "sources only"),
        ("Merged PRs", s["merged"], "all time"),
        ("Merged upstream", s["upstream"], "others' repos"),
    ]
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
        f'role="img" aria-label="GitHub statistics for {escape(LOGIN)}" font-family="\'Segoe UI\',Ubuntu,Helvetica,sans-serif">',
        "<defs>",
        '<linearGradient id="edge" x1="0" y1="0" x2="1" y2="1">',
        '<stop offset="0%" stop-color="#7aa2f7"/><stop offset="50%" stop-color="#bb9af7"/>'
        '<stop offset="100%" stop-color="#7dcfff"/>',
        "</linearGradient>",
        "<style>",
        ".bg{fill:#ffffff;stroke:url(#edge);stroke-width:1.5}",
        ".title{fill:#1f2328;font-size:15px;font-weight:700}",
        ".label{fill:#59636e;font-size:10.5px}",
        ".value{fill:#1f2328;font-size:20px;font-weight:700}",
        ".sub{fill:#8b949e;font-size:8.5px}",
        ".lang{fill:#1f2328;font-size:10px}",
        "@media (prefers-color-scheme: dark){",
        ".bg{fill:#0d1117}.title{fill:#e6edf3}.value{fill:#e6edf3}",
        ".label{fill:#9198a1}.lang{fill:#e6edf3}.sub{fill:#6e7681}}",
        ".fx{animation:in .6s ease backwards}",
        "@keyframes in{from{opacity:0}to{opacity:1}}",
        "@keyframes grow{from{transform:scaleX(0)}to{transform:scaleX(1)}}",
        ".bar{transform-origin:left center;animation:grow .9s cubic-bezier(.3,.8,.4,1) backwards}",
        "@media (prefers-reduced-motion: reduce){.fx,.bar{animation:none}}",
        "</style>",
        "</defs>",
        f'<rect class="bg" x="1" y="1" width="{W-2}" height="{H-2}" rx="10"/>',
        f'<text class="title fx" x="24" y="34" style="animation-delay:.05s">{escape(LOGIN)} &#183; GitHub</text>',
    ]

    # Four stat tiles in a 2x2 grid.
    for i, (label, value, sub) in enumerate(tiles):
        x = 24 + (i % 2) * 214
        y = 66 + (i // 2) * 56
        d = 0.12 + i * 0.07
        out += [
            f'<g class="fx" style="animation-delay:{d:.2f}s">',
            f'<text class="label" x="{x}" y="{y}">{label}</text>',
            f'<text class="value" x="{x}" y="{y+22}">{value:,}</text>',
            f'<text class="sub" x="{x+len(f"{value:,}")*12+8}" y="{y+22}">{sub}</text>',
            "</g>",
        ]

    # Stacked language bar.
    by = 196
    out.append(f'<text class="label fx" x="24" y="{by-8}" style="animation-delay:.45s">Most-used languages</text>')
    bw, bx = W - 48, 24.0
    out.append(f'<g><clipPath id="r"><rect x="24" y="{by}" width="{bw}" height="9" rx="4.5"/></clipPath>')
    out.append('<g clip-path="url(#r)">')
    for i, (_, pct, color) in enumerate(s["langs"]):
        seg = bw * pct / 100.0
        out.append(
            f'<rect class="bar" x="{bx:.1f}" y="{by}" width="{seg:.1f}" height="9" fill="{color}" '
            f'style="animation-delay:{.5+i*.08:.2f}s"/>'
        )
        bx += seg
    if bx < 24 + bw - 0.5:
        out.append(
            f'<rect class="bar" x="{bx:.1f}" y="{by}" width="{24+bw-bx:.1f}" height="9" '
            f'fill="#8b949e" opacity=".35" style="animation-delay:.9s"/>'
        )
    out.append("</g></g>")

    # Legend.
    lx = 24
    for i, (name, pct, color) in enumerate(s["langs"]):
        out += [
            f'<g class="fx" style="animation-delay:{.62+i*.06:.2f}s">',
            f'<circle cx="{lx+4}" cy="{by+27}" r="4" fill="{color}"/>',
            f'<text class="lang" x="{lx+13}" y="{by+31}">{escape(name)} {pct:.1f}%</text>',
            "</g>",
        ]
        lx += 20 + len(f"{name} {pct:.1f}%") * 5.6
    out.append("</svg>")
    return "\n".join(out)


if __name__ == "__main__":
    stats = summarise(fetch())
    os.makedirs(os.path.dirname(OUT) or ".", exist_ok=True)
    with open(OUT, "w") as fh:
        fh.write(render(stats))
    print(f"wrote {OUT}: {stats}")
