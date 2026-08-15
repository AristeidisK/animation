#!/usr/bin/env python3
"""
Build the cast as flat-vector SVGs from a single geometry spec.

Characters are drawn, not generated. fal.ai gave us a dog when we asked for a
hare and a different owl in every shot; that is a property of the model, not a
prompting problem. Drawing them once removes drift as a category rather than
managing it forever.

Colours are read from brand/tokens.json at build time, so the cast can never
fall out of step with the palette. The Figma components mirror these numbers.

Usage:  python3 pipeline/build_cast.py
Output: brand/characters/*.svg
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "brand" / "characters"

C = {k: v["hex"] for k, v in
     json.loads((ROOT / "brand/tokens.json").read_text())["core"].items()}


# ---------- primitives ----------

def ell(cx, cy, rx, ry, fill, rot=None):
    t = f' transform="rotate({rot} {cx} {cy})"' if rot else ""
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{C[fill]}"{t}/>'

def rect(x, y, w, h, r, fill, rot=None):
    t = f' transform="rotate({rot} {x + w/2} {y + h/2})"' if rot else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{C[fill]}"{t}/>'

def tri(cx, cy, w, h, fill):
    p = f"{cx-w/2},{cy-h/2} {cx+w/2},{cy-h/2} {cx},{cy+h/2}"
    return f'<polygon points="{p}" fill="{C[fill]}"/>'

def svg(name, w, h, parts):
    body = "\n  ".join(parts)
    doc = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
           f'width="{w}" height="{h}">\n  {body}\n</svg>\n')
    (OUT / f"{name}.svg").write_text(doc)
    return len(doc)


# ---------- the cast ----------
# Colour-coded, one core hue each, so identity survives at thumbnail size.
#   Kouki  plum   (RESERVED — host only)
#   Hare   sun     (fast, showy, warm)
#   Tortoise olive shell + seafoam skin (earthy, steady)
# Skin is never bone: backgrounds use bone constantly and she vanishes into them.

def kouki():
    """Host. Geometry identical to the Figma component. Branch excluded —
    she composites onto whatever perch the background provides."""
    return svg("kouki", 800, 900, [
        ell(282, 291, 32, 75, "plum", rot=24),      # ear tuft L
        ell(518, 291, 32, 75, "plum", rot=-24),     # ear tuft R
        ell(400, 522, 260, 272, "plum"),            # body dome
        ell(400, 645, 126, 111, "bone"),            # chest
        rect(318, 770, 72, 26, 13, "sun"),          # foot L
        rect(410, 770, 72, 26, 13, "sun"),          # foot R
        ell(330, 415, 75, 75, "sun"),               # eye disc L
        ell(470, 415, 75, 75, "sun"),               # eye disc R
        ell(330, 415, 27, 27, "ink"),               # pupil L
        ell(470, 415, 27, 27, "ink"),               # pupil R
        tri(400, 481, 58, 66, "terracotta"),        # beak
        rect(268, 302, 118, 18, 9, "ink"),          # brow L
        rect(414, 302, 118, 18, 9, "ink"),          # brow R
    ])


def hare():
    """Facing right. Built long and low — the silhouette has to read as speed."""
    return svg("hare", 900, 700, [
        ell(600, 165, 27, 118, "sun", rot=-9),      # ear L
        ell(664, 158, 27, 118, "sun", rot=7),       # ear R
        ell(600, 175, 12, 82, "terracotta", rot=-9),
        ell(664, 168, 12, 82, "terracotta", rot=7),
        ell(150, 392, 32, 32, "bone"),              # tail
        ell(258, 424, 132, 128, "sun"),             # haunch
        ell(390, 428, 186, 122, "sun"),             # body
        ell(392, 486, 120, 58, "bone"),             # belly
        rect(184, 552, 176, 54, 27, "sun"),         # back foot
        rect(548, 462, 48, 150, 24, "sun"),         # front leg (must touch the body)
        ell(622, 332, 96, 86, "sun"),               # head
        ell(676, 318, 15, 15, "ink"),               # eye
        ell(714, 366, 9, 7, "terracotta"),          # nose
    ])


def tortoise():
    """Facing right. Low, wide, immovable — the visual opposite of the hare."""
    # Head and neck are drawn AFTER the shell so the rim cannot swallow them.
    return svg("tortoise", 900, 600, [
        ell(140, 372, 26, 18, "seafoam"),           # tail
        rect(212, 384, 88, 104, 34, "seafoam"),     # back leg
        rect(408, 388, 88, 104, 34, "seafoam"),    # front leg
        ell(380, 300, 240, 155, "olive"),           # shell
        ell(298, 268, 60, 40, "bone"),              # shell plates
        ell(390, 250, 66, 44, "bone"),
        ell(480, 270, 58, 38, "bone"),
        ell(380, 378, 246, 52, "olive"),            # shell rim
        rect(586, 328, 116, 64, 30, "seafoam"),     # neck
        ell(732, 350, 80, 68, "seafoam"),           # head
        ell(766, 332, 13, 13, "ink"),               # eye
        ell(796, 366, 8, 6, "terracotta"),          # nostril
    ])


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for fn in (kouki, hare, tortoise):
        n = fn.__name__
        print(f"  {n:9s} {fn():5d} bytes -> brand/characters/{n}.svg")
    print("\nColours read from brand/tokens.json — the cast cannot drift from the palette.")
