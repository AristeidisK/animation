#!/usr/bin/env python3
"""
Generate brand/palette.html from brand/tokens.json.

Generated, never hand-written, so it cannot go stale. Edit tokens.json, re-run
this, and the reference page matches what the cast and plates actually build
with. Derived tones come from the same shift() the cast uses, so what you see
here is literally what gets drawn.

Usage:  python3 pipeline/build_palette.py
Output: brand/palette.html
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "pipeline"))
from build_cast import shift  # identical derivation to the cast

TOK = json.loads((ROOT / "brand/tokens.json").read_text())
CORE = TOK["core"]
HEX2NAME = {v["hex"].upper(): k for k, v in CORE.items()}

# Where each token actually appears, beyond the one-line note in tokens.json.
WHERE = {
    "ink":        ("Structure", ["Cypress and trunk silhouettes", "Eyes and pupils, all cast",
                                 "Kouki's brows", "Subtitle plate", "Cast shadows at 15%"]),
    "bone":       ("Structure", ["Limestone, dry stone walls, road dust", "Hare belly, muzzle, tail",
                                 "Tortoise shell plates", "Catchlights", "Subtitle text"]),
    "aegean":     ("Distance",  ["Sky, top of the gradient", "Far hills on cool plates",
                                 "Brand primary"]),
    "deepsea":    ("Distance",  ["Night water", "Deep distance", "Darkest blue available"]),
    "storm":      ("Distance",  ["Hazed far hills", "Dry stone wall shadow faces",
                                 "Northern weather"]),
    "olive":      ("Land",      ["All foliage mass", "Mid hills, grove floor",
                                 "Tortoise shell", "The perch branch"]),
    "seafoam":    ("Land",      ["Olive-leaf silver highlights", "Sky at the horizon band",
                                 "Tortoise skin", "Shallow water"]),
    "sun":        ("Warmth",    ["Dry grass, the whole ground plane", "THE HARE",
                                 "Kouki's eye discs and feet", "Lamplight"]),
    "terracotta": ("Warmth",    ["The road surface, bare earth", "Poppies, oleander flowers",
                                 "Kouki's beak", "Hare inner ear and nose"]),
    "plum":       ("Reserved",  ["KOUKI ONLY — body, tufts, wing", "Dusk skies",
                                 "Forbidden in Aesop backgrounds"]),
}

GROUPS = ["Structure", "Distance", "Land", "Warmth", "Reserved"]

RULES = [
    ("Plum lock", "Kouki is the only plum object in any frame she appears in. Nothing else "
                  "may use plum while she is on screen — not a flower, not a shadow, not a sky. "
                  "This single rule does more for her identity than every other measure combined."),
    ("Warm balance", "terracotta and sun are ACCENTS, never both large in one frame. Only "
                     "hearth-amber may ground a scene in terracotta. Grounds default to olive, "
                     "aegean, seafoam or deepsea — the land is green and the distance is blue."),
    ("The hare's ground", "He is sun; dry grass is sun. He must never stand on a sun or "
                          "terracotta ground or he disappears. This is what forced the ramp rebalance."),
    ("The tortoise's skin", "Never bone. Backgrounds use bone constantly for limestone, dust and "
                            "walls, and she vanished into every one of them. seafoam is the fix."),
    ("One gradient", "Exactly one soft vertical sky gradient per plate. Nothing else gradients, "
                     "ever. Shading is flat two-tone, drawn as a shape."),
    ("Never pure", "No #000, no #FFF. ink and bone are the ends of the range."),
]


def swatch(name, spec):
    base = spec["hex"]
    group, uses = WHERE.get(name, ("", []))
    tones = [("base", base),
             ("light", shift(base, dl=+0.09, ds=-0.02)),
             ("dark",  shift(base, dl=-0.10, ds=+0.03)),
             ("deep",  shift(base, dl=-0.18, ds=+0.05))]
    strip = "".join(
        f'<div class="tone"><span style="background:{h}"></span>'
        f'<b>{lbl}</b><code>{h}</code></div>' for lbl, h in tones)
    lis = "".join(f"<li>{u}</li>" for u in uses)
    res = ' <em class="res">reserved</em>' if name == "plum" else ""
    return f"""<article class="tok">
  <div class="chip" style="background:{base}"></div>
  <div class="meta">
    <h3>{name}{res}</h3>
    <code class="big">{base}</code>
    <p>{spec['use']}</p>
    <ul>{lis}</ul>
    <div class="tones">{strip}</div>
  </div>
</article>"""


def ramp_row(key, spec):
    roles = ["sky", "ground", "far", "mid", "foreground"]
    cells = "".join(
        f'<div class="band" style="background:{h}">'
        f'<b>{roles[i]}</b><span>{HEX2NAME.get(h.upper(), h)}</span></div>'
        for i, h in enumerate(spec["ramp"]))
    return f"""<div class="ramp">
  <div class="ramp-h"><h3>{key}</h3><p>{spec['mood']}</p></div>
  <div class="bands">{cells}</div>
  <p class="use">{spec['use']}</p>
</div>"""


CSS = """
:root{color-scheme:dark;--bg:#1A1820;--card:#242130;--line:#332F42;--fg:#F7F1E4;--dim:#A79FB8}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);padding:44px 40px 90px;
 font:15px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",system-ui,sans-serif}
h1{font-size:30px;font-weight:650;margin:0 0 6px;letter-spacing:-.02em}
.lede{margin:0 0 4px;color:var(--dim);max-width:70ch}
.src{margin:0 0 40px;color:var(--dim);font-size:13px}
.src code{background:var(--card);padding:3px 8px;border-radius:5px;font-size:12px}
h2{font-size:12px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;
 color:#F2B33D;margin:44px 0 16px;padding-bottom:9px;border-bottom:1px solid var(--line)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:16px}
.tok{display:flex;gap:16px;background:var(--card);border:1px solid var(--line);
 border-radius:10px;padding:16px;align-items:flex-start}
.chip{width:78px;height:126px;border-radius:7px;flex:0 0 auto;
 box-shadow:inset 0 0 0 1px #0004}
.meta{min-width:0;flex:1}
.meta h3{margin:0;font-size:17px;font-weight:650;letter-spacing:-.01em}
.res{font-style:normal;font-size:9.5px;letter-spacing:.13em;background:#6B4A78;
 color:#F7F1E4;padding:2px 7px;border-radius:4px;vertical-align:2px;margin-left:7px}
code{font-family:ui-monospace,SFMono-Regular,Menlo,monospace}
.big{display:block;font-size:13px;color:var(--dim);padding:3px 0 8px;letter-spacing:.04em}
.meta p{margin:0 0 9px;font-size:13.5px;color:var(--dim)}
.meta ul{margin:0;padding-left:17px;font-size:13px}
.meta li{padding:1px 0}
.meta li::marker{color:#5E5772}
.tones{display:flex;gap:7px;margin-top:12px;padding-top:11px;border-top:1px solid var(--line)}
.tone{flex:1;text-align:center}
.tone span{display:block;height:24px;border-radius:4px;box-shadow:inset 0 0 0 1px #0004}
.tone b{display:block;font-size:9.5px;font-weight:600;letter-spacing:.07em;
 color:var(--dim);padding-top:4px}
.tone code{font-size:8.5px;color:#6E6683}
.ramp{background:var(--card);border:1px solid var(--line);border-radius:10px;
 padding:16px;margin-bottom:12px}
.ramp-h{display:flex;align-items:baseline;gap:14px;flex-wrap:wrap}
.ramp-h h3{margin:0;font-size:16px;font-weight:650}
.ramp-h p{margin:0;font-size:13px;color:var(--dim)}
.bands{display:flex;gap:5px;margin:12px 0 9px}
.band{flex:1;height:74px;border-radius:6px;padding:7px 8px;
 box-shadow:inset 0 0 0 1px #0004;display:flex;flex-direction:column;justify-content:space-between}
.band b{font-size:9px;letter-spacing:.1em;text-transform:uppercase;color:#00000075}
.band span{font-size:10.5px;color:#00000090;font-weight:600}
.use{margin:0;font-size:12.5px;color:var(--dim)}
.rules{display:grid;grid-template-columns:repeat(auto-fill,minmax(330px,1fr));gap:12px}
.rule{background:var(--card);border-left:3px solid #97362B;border-radius:0 8px 8px 0;padding:14px 16px}
.rule h3{margin:0 0 5px;font-size:13.5px;font-weight:650}
.rule p{margin:0;font-size:13px;color:var(--dim)}
footer{margin-top:52px;padding-top:18px;border-top:1px solid var(--line);
 color:#6E6683;font-size:12px;font-family:ui-monospace,Menlo,monospace;line-height:1.8}
"""


def main():
    groups = {g: [] for g in GROUPS}
    for name, spec in CORE.items():
        groups[WHERE.get(name, ("Structure", []))[0]].append(swatch(name, spec))
    sections = "".join(
        f'<h2>{g}</h2><div class="grid">{"".join(groups[g])}</div>'
        for g in GROUPS if groups[g])
    ramps = "".join(ramp_row(k, v) for k, v in TOK["sceneKeys"].items())
    rules = "".join(f'<div class="rule"><h3>{t}</h3><p>{b}</p></div>' for t, b in RULES)

    html = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Paramythia &mdash; Palette</title><style>{CSS}</style></head><body>
<h1>Palette</h1>
<p class="lede">Ten colours. Everything &mdash; the cast, the plates, the Figma variables and the
image prompts &mdash; reads from one file. Nothing may introduce a colour outside this set.</p>
<p class="src">Generated from <code>brand/tokens.json</code> &middot; rebuild with
<code>python3 pipeline/build_palette.py</code></p>
{sections}
<h2>Scene ramps</h2>
<p class="lede" style="margin-bottom:16px">Each scene key assigns the palette to the five depth
planes. This is what decides what dominates a frame &mdash; more than the colours themselves.</p>
{ramps}
<h2>Rules</h2>
<div class="rules">{rules}</div>
<footer>
brand/tokens.json &mdash; source of truth. Figma mirrors it; tokens.json wins on any disagreement.<br>
Derived tones (light +9% L, dark &minus;10% L, deep &minus;18% L) are computed at build time in
pipeline/build_cast.py::shift() &mdash; 10 tokens, 40 tones, none of them invented.<br>
Change a hex here, then rebuild: build_cast.py, build_plates.py, build_palette.py.
</footer>
</body></html>"""

    out = ROOT / "brand" / "palette.html"
    out.write_text(html, encoding="utf-8")
    print(f"  wrote {out.relative_to(ROOT)}  ({len(html)//1024} KB)")
    print(f"  {len(CORE)} tokens in {len([g for g in GROUPS if groups[g]])} groups, "
          f"{len(TOK['sceneKeys'])} scene ramps, {len(RULES)} rules")


if __name__ == "__main__":
    main()
