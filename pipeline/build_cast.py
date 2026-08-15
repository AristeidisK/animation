#!/usr/bin/env python3
"""
Build the cast as flat-vector SVGs from a single geometry spec.

Characters are drawn, not generated. fal.ai gave us a dog when we asked for a
hare, and a different owl in every shot; that is a property of the model, not a
prompting problem. Drawing them once removes drift as a category.

Because drift is gone, the earlier minimal geometry has no reason to stay
minimal — it was a hedge against a problem that no longer exists. These are
built with real detail: flat TWO-TONE shading, articulated limbs, facial
structure. Bluey is not gradient-shaded either; it is flat base colour plus a
flat shadow shape. That is what this does.

Every colour derives from brand/tokens.json. Second tones are computed from the
palette rather than invented, so the cast can never fall out of step with it.

Usage:  python3 pipeline/build_cast.py
Output: brand/characters/*.svg
"""

import colorsys
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "brand" / "characters"

RAW = {k: v["hex"] for k, v in
       json.loads((ROOT / "brand/tokens.json").read_text())["core"].items()}


# ---------- derived tones ----------

def shift(hexstr, dl=0.0, ds=0.0):
    """Lighten/darken and saturate a token colour in HLS space."""
    h = hexstr.lstrip("#")
    r, g, b = (int(h[i:i+2], 16) / 255 for i in (0, 2, 4))
    hh, ll, ss = colorsys.rgb_to_hls(r, g, b)
    # Clamp inside the legal range, never to 0 or 1 — the bible forbids pure
    # black and pure white, and unclamped shifts drove ink and bone straight
    # into both. ink and bone ARE the ends of the range.
    ll = max(0.085, min(0.955, ll + dl))
    ss = max(0.0, min(1.0, ss + ds))
    r, g, b = colorsys.hls_to_rgb(hh, ll, ss)
    return "#%02X%02X%02X" % (round(r * 255), round(g * 255), round(b * 255))


C = dict(RAW)
for _name, _hex in RAW.items():
    C[f"{_name}-dark"]  = shift(_hex, dl=-0.10, ds=+0.03)
    C[f"{_name}-deep"]  = shift(_hex, dl=-0.18, ds=+0.05)
    C[f"{_name}-light"] = shift(_hex, dl=+0.09, ds=-0.02)


# ---------- primitives ----------

def ell(cx, cy, rx, ry, fill, rot=None, op=None):
    t = f' transform="rotate({rot} {cx} {cy})"' if rot else ""
    o = f' opacity="{op}"' if op else ""
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{C[fill]}"{t}{o}/>'


def rect(x, y, w, h, r, fill, rot=None):
    t = f' transform="rotate({rot} {x + w/2} {y + h/2})"' if rot else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{C[fill]}"{t}/>'


def tri(cx, cy, w, h, fill):
    return (f'<polygon points="{cx-w/2},{cy-h/2} {cx+w/2},{cy-h/2} {cx},{cy+h/2}" '
            f'fill="{C[fill]}"/>')


def path(d, fill):
    return f'<path d="{d}" fill="{C[fill]}"/>'


def clipped(cid, shape_svg, inner):
    """Flat shadow: draw `inner`, show it only inside `shape_svg`. This is how
    two-tone shading stays crisp instead of becoming a gradient."""
    return (f'<clipPath id="{cid}">{shape_svg}</clipPath>'
            f'<g clip-path="url(#{cid})">{"".join(inner)}</g>')


def svg(name, w, h, parts):
    doc = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
           f'width="{w}" height="{h}">\n  ' + "\n  ".join(parts) + "\n</svg>\n")
    (OUT / f"{name}.svg").write_text(doc)
    return len(doc)


# ---------- the cast ----------
# One core hue each, so identity survives at thumbnail size.
#   Kouki    plum    (RESERVED — host only)
#   Hare     sun     (fast, showy, warm)
#   Tortoise olive shell + seafoam skin (earthy, steady)
# Tortoise skin is never bone: backgrounds use bone constantly and she vanishes.

def kouki():
    body = '<ellipse cx="400" cy="522" rx="260" ry="272"/>'
    return svg("kouki", 800, 900, [
        ell(400, 758, 120, 76, "plum-deep"),                 # tail
        ell(276, 286, 34, 82, "plum-dark", rot=25),          # ear tufts
        ell(524, 286, 34, 82, "plum-dark", rot=-25),
        ell(280, 292, 20, 60, "plum", rot=25),
        ell(520, 292, 20, 60, "plum", rot=-25),
        ell(400, 522, 260, 272, "plum"),                     # body
        clipped("k1", body, [ell(566, 566, 190, 286, "plum-dark")]),
        ell(228, 566, 74, 168, "plum-deep", rot=-8),         # folded wing
        ell(236, 556, 56, 140, "plum-dark", rot=-8),
        ell(400, 402, 188, 156, "plum-light"),               # facial disc
        ell(400, 648, 128, 116, "bone"),                     # chest
        ell(400, 692, 104, 68, "bone-dark", op="0.5"),
        ell(362, 638, 9, 13, "plum-light", op="0.5"),        # speckles
        ell(400, 620, 9, 13, "plum-light", op="0.5"),
        ell(438, 638, 9, 13, "plum-light", op="0.5"),
        ell(381, 670, 9, 13, "plum-light", op="0.45"),
        ell(419, 670, 9, 13, "plum-light", op="0.45"),
        ell(330, 415, 78, 78, "sun-dark"),                   # eyes
        ell(470, 415, 78, 78, "sun-dark"),
        ell(330, 412, 71, 71, "sun"),
        ell(470, 412, 71, 71, "sun"),
        ell(330, 415, 30, 30, "ink"),
        ell(470, 415, 30, 30, "ink"),
        ell(341, 402, 11, 11, "bone"),                       # catchlights
        ell(481, 402, 11, 11, "bone"),
        tri(400, 486, 62, 72, "terracotta"),                 # beak
        path("M369,462 L431,462 L400,478 Z", "terracotta-light"),
        rect(264, 300, 122, 19, 9, "ink", rot=-4),           # brows
        rect(414, 300, 122, 19, 9, "ink", rot=4),
        rect(310, 766, 84, 28, 13, "sun-dark"),              # feet
        rect(406, 766, 84, 28, 13, "sun-dark"),
        rect(316, 788, 20, 22, 9, "sun-dark"), rect(342, 788, 20, 22, 9, "sun-dark"),
        rect(368, 788, 20, 22, 9, "sun-dark"),
        rect(412, 788, 20, 22, 9, "sun-dark"), rect(438, 788, 20, 22, 9, "sun-dark"),
        rect(464, 788, 20, 22, 9, "sun-dark"),
    ])


def hare():
    body = '<ellipse cx="390" cy="428" rx="188" ry="126"/>'
    return svg("hare", 900, 700, [
        ell(598, 160, 30, 124, "sun-dark", rot=-9),          # ears
        ell(666, 152, 30, 124, "sun-dark", rot=7),
        ell(598, 168, 22, 108, "sun", rot=-9),
        ell(666, 160, 22, 108, "sun", rot=7),
        ell(598, 176, 11, 78, "terracotta", rot=-9),
        ell(666, 168, 11, 78, "terracotta", rot=7),
        ell(148, 388, 36, 34, "bone"),                       # tail
        ell(152, 398, 26, 22, "bone-dark", op="0.5"),
        rect(300, 512, 50, 104, 24, "sun-deep"),             # far legs
        rect(576, 470, 46, 140, 22, "sun-deep"),
        ell(258, 424, 136, 132, "sun-dark"),                 # haunch
        ell(252, 416, 120, 118, "sun"),
        ell(390, 428, 188, 126, "sun"),                      # body
        clipped("h1", body, [ell(430, 512, 210, 96, "sun-dark")]),
        ell(392, 486, 122, 56, "bone"),                      # belly
        rect(196, 546, 178, 58, 28, "sun-dark"),             # near back foot
        rect(206, 540, 158, 46, 22, "sun"),
        rect(214, 592, 22, 20, 9, "sun-deep"), rect(246, 592, 22, 20, 9, "sun-deep"),
        rect(278, 592, 22, 20, 9, "sun-deep"),
        rect(496, 462, 52, 152, 25, "sun-dark"),             # near front leg
        rect(502, 456, 42, 140, 20, "sun"),
        rect(492, 594, 64, 26, 12, "sun-deep"),
        ell(622, 332, 100, 90, "sun-dark"),                  # head
        ell(618, 326, 92, 82, "sun"),
        ell(668, 356, 56, 44, "bone"),                       # muzzle
        ell(676, 316, 17, 17, "ink"),                        # eye
        ell(681, 310, 6, 6, "bone"),
        ell(714, 360, 11, 8, "terracotta"),                  # nose
        ell(690, 374, 22, 13, "bone-dark", op="0.4"),
    ])


def tortoise():
    shell = '<ellipse cx="380" cy="294" rx="232" ry="150"/>'
    plates = []
    for cx, cy, rx, ry in [(268, 286, 54, 40), (380, 256, 62, 46), (492, 286, 54, 40),
                           (320, 342, 50, 34), (440, 342, 50, 34)]:
        plates.append(ell(cx, cy, rx, ry, "olive-light"))
        plates.append(ell(cx, cy + 6, rx - 12, ry - 10, "olive-dark", op="0.32"))
    return svg("tortoise", 900, 600, [
        ell(138, 372, 30, 20, "seafoam-dark"),               # tail
        rect(250, 386, 82, 96, 32, "seafoam-deep"),          # far legs
        rect(452, 390, 82, 96, 32, "seafoam-deep"),
        rect(200, 384, 92, 108, 34, "seafoam-dark"),         # near legs
        rect(208, 378, 76, 96, 28, "seafoam"),
        rect(214, 468, 20, 20, 8, "seafoam-deep"), rect(240, 468, 20, 20, 8, "seafoam-deep"),
        rect(404, 388, 92, 108, 34, "seafoam-dark"),
        rect(412, 382, 76, 96, 28, "seafoam"),
        rect(418, 472, 20, 20, 8, "seafoam-deep"), rect(444, 472, 20, 20, 8, "seafoam-deep"),
        ell(380, 300, 242, 158, "olive-dark"),               # shell
        ell(380, 294, 232, 150, "olive"),
        *plates,
        clipped("t1", shell, [ell(430, 400, 260, 110, "olive-dark", op="0.45")]),
        ell(380, 378, 248, 54, "olive-deep"),                # rim
        ell(380, 372, 240, 42, "olive-dark"),
        rect(580, 326, 122, 68, 32, "seafoam-dark"),         # neck
        rect(584, 322, 116, 58, 26, "seafoam"),
        ell(734, 350, 84, 72, "seafoam-dark"),               # head
        ell(730, 344, 76, 65, "seafoam"),
        ell(766, 330, 15, 15, "ink"),                        # eye
        ell(771, 324, 5, 5, "bone"),
        ell(798, 362, 9, 7, "seafoam-deep"),                 # nostril
        ell(752, 382, 26, 12, "seafoam-deep", op="0.5"),     # mouth
    ])


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for fn in (kouki, hare, tortoise):
        print(f"  {fn.__name__:9s} {fn():5d} bytes")
    print(f"\n{len(RAW)} palette tokens -> {len(C)} tones (base, -dark, -deep, -light).")
    print("Second tones are computed, never invented. Flat two-tone, no gradients.")
