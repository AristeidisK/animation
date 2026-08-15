#!/usr/bin/env python3
"""
Build the background plates as flat-vector SVGs, from the location specs.

Plates are drawn rather than generated for one reason: a model can be ASKED for
a period and will ignore you — "no domes" produced two domes and a bell tower.
A drawn plate simply IS the period. Era enforcement and background quality turn
out to be the same problem.

Cascade honoured here:
    brand/tokens.json           colour
    projects/aesop/project.md   era, species, vertical grammar
    .../locations/*.md          horizon, light, path, plane stack

Shots are camera positions on plates, not separate artworks: 12 shots, 5 plates.

Usage:  python3 pipeline/build_plates.py
Output: brand/plates/*.svg
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "brand" / "plates"

import sys
sys.path.insert(0, str(ROOT / "pipeline"))
from build_cast import C, ell, rect, path  # shared tokens + derived tones

W, H = 1080, 1920
HORIZON = round(H * 0.37)          # 710 — same on every plate, per road.md


# ---------- helpers ----------

def sky(top="aegean", bottom="seafoam"):
    """The single vertical gradient the bible permits. Nothing else gradients."""
    return (f'<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">'
            f'<stop offset="0" stop-color="{C[top]}"/>'
            f'<stop offset="1" stop-color="{C[bottom]}"/></linearGradient></defs>'
            f'<rect x="0" y="0" width="{W}" height="{HORIZON}" fill="url(#sky)"/>')


def hills(cy, ry, tone, spans):
    """Flat silhouettes peeking above the horizon. No interior detail."""
    return "".join(ell(cx, cy, rx, ry, tone) for cx, rx in spans)


def ground(tone="sun"):
    return rect(0, HORIZON, W, H - HORIZON, 0, tone)


def road_edges(y, cx_near, cx_far, half_near, half_far=13):
    """Linear taper from the bottom edge to the vanishing point."""
    t = max(0.0, min(1.0, (y - HORIZON) / (H - HORIZON)))
    return (cx_far + t * (cx_near - cx_far), half_far + t * (half_near - half_far))


def road(cx_near, cx_far, half_near, tone="terracotta"):
    cxb, hb = road_edges(H, cx_near, cx_far, half_near)
    cxt, ht = road_edges(HORIZON, cx_near, cx_far, half_near)
    d = f"M{cxb-hb},{H} L{cxb+hb},{H} L{cxt+ht},{HORIZON} L{cxt-ht},{HORIZON} Z"
    dust = f"M{cxb-hb},{H} L{cxb-hb+34},{H} L{cxt-ht+4},{HORIZON} L{cxt-ht},{HORIZON} Z"
    return path(d, tone) + path(dust, "bone")


def olive(cx, cy, r, trunk=True):
    """Clustered rounded masses with seafoam silver on the upper-left of each —
    that flash is what makes an olive read as an olive and not a lollipop."""
    parts = []
    if trunk:
        parts.append(path(f"M{cx-r*0.10},{cy+r*0.15} L{cx+r*0.10},{cy+r*0.15} "
                          f"L{cx+r*0.16},{cy+r*1.30} L{cx-r*0.16},{cy+r*1.30} Z", "ink"))
    for dx, dy, rr in [(-0.62, 0.10, 0.56), (0.58, 0.16, 0.52),
                       (-0.10, -0.34, 0.62), (0.22, 0.30, 0.50), (-0.34, 0.34, 0.44)]:
        parts.append(ell(cx + dx*r, cy + dy*r, rr*r, rr*r*0.82, "olive"))
    for dx, dy, rr in [(-0.78, -0.06, 0.22), (-0.26, -0.54, 0.24), (0.40, 0.02, 0.19)]:
        parts.append(ell(cx + dx*r, cy + dy*r, rr*r, rr*r*0.72, "seafoam"))
    return "".join(parts)


def cypress(cx, cy, h, tone="olive-deep"):
    return ell(cx, cy - h*0.5, h*0.13, h*0.5, tone) + \
           path(f"M{cx-4},{cy-6} L{cx+4},{cy-6} L{cx+6},{cy+h*0.10} L{cx-6},{cy+h*0.10} Z", "ink")


def wall(x0, yt0, yb0, x1, yt1, yb1, courses=7):
    """Dry stone as ONE receding mass with block divisions, never loose blocks."""
    out = [path(f"M{x0},{yt0} L{x1},{yt1} L{x1},{yb1} L{x0},{yb0} Z", "bone")]
    # shadow face along the bottom third
    f = 0.60
    out.append(path(f"M{x0},{yt0+(yb0-yt0)*f} L{x1},{yt1+(yb1-yt1)*f} "
                    f"L{x1},{yb1} L{x0},{yb0} Z", "storm"))
    for i in range(1, courses):
        k = i / courses
        xs = x0 + (x1 - x0) * (k ** 1.7)
        yt = yt0 + (yt1 - yt0) * (k ** 1.7)
        yb = yb0 + (yb1 - yb0) * (k ** 1.7)
        out.append(path(f"M{xs},{yt} L{xs+3},{yt} L{xs+3},{yb} L{xs},{yb} Z", "storm"))
    return "".join(out)


def canopy_band(y, r, spans):
    """A continuous mass of overlapping canopies so trunks rise INTO something."""
    return "".join(olive(cx, y + dy, r * s, trunk=False) for cx, dy, s in spans)


def tufts(specs, tone="olive-deep"):
    return "".join(ell(x, y, rx, ry, tone) for x, y, rx, ry in specs)


def poppies(specs):
    return "".join(ell(x, y, 7, 6, "terracotta") for x, y in specs)


def shade_pool(cx, cy, rx, ry, tone="olive-deep", op="1"):
    return ell(cx, cy, rx, ry, tone, op=op)


def write(name, parts):
    doc = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
           f'width="{W}" height="{H}">\n  ' + "\n  ".join(parts) + "\n</svg>\n")
    (OUT / f"{name}.svg").write_text(doc)
    return len(doc)


# ---------- plates ----------

def road_start():
    """Shots 2, 3, 5, 6. Widest and most populated. The boast and the start."""
    cxn, cxf, hn = 0.58*W, 0.46*W, 300
    ly = round(H * 0.62)
    lcx, lh = road_edges(ly, cxn, cxf, hn)
    return write("road-start", [
        sky(),
        hills(HORIZON + 150, 190, "storm", [(150, 430), (620, 380), (980, 300)]),
        hills(HORIZON + 96, 120, "olive", [(340, 400), (820, 360)]),
        ground("sun"),
        # terraces on the mid slope
        rect(60, HORIZON + 24, 380, 7, 3, "bone"),
        rect(640, HORIZON + 40, 330, 7, 3, "bone"),
        road(cxn, cxf, hn),
        # start line
        path(f"M{lcx-lh},{ly} L{lcx+lh},{ly} L{lcx+lh},{ly+11} L{lcx-lh},{ly+11} Z", "bone"),
        # dry stone wall, one mass running the left verge into depth
        wall(0, 1146, 1330, 470, HORIZON + 6, HORIZON + 34),
        poppies([(880, 1290), (930, 1350), (982, 1300), (856, 1420), (1010, 1420), (908, 1236)]),
        # signature olive, near left, canopy cropped by the top-left corner
        olive(120, 300, 300),
        tufts([(30, 1806, 250, 104), (360, 1852, 300, 118), (740, 1820, 270, 106),
               (1050, 1790, 250, 112)]),
    ])


def road_open():
    """Shots 7, 10. The long empty middle. The vanishing point is HIDDEN over a
    rise, which is what sells 'so far ahead he couldn't see her'."""
    cxn, cxf, hn = 0.54*W, 0.52*W, 250
    crest = round(H * 0.44)
    return write("road-open", [
        sky(),
        hills(HORIZON + 150, 190, "storm", [(150, 430), (620, 380), (980, 300)]),
        hills(HORIZON + 96, 120, "olive", [(340, 400), (820, 360)]),
        ground("sun"),
        road(cxn, cxf, hn),
        # the rise: ground swells across the road and cuts the far distance off
        path(f"M-40,{crest+300} Q{0.52*W},{crest-30} {W+40},{crest+300} "
             f"L{W+40},{crest+520} L-40,{crest+520} Z", "sun"),
        path(f"M-40,{crest+312} Q{0.52*W},{crest-14} {W+40},{crest+312} "
             f"L{W+40},{crest+360} L-40,{crest+360} Z", "sun-dark"),
        olive(96, 980, 108),                       # same tree, further along
        cypress(950, HORIZON + 240, 330),
        tufts([(70, 1812, 270, 110), (540, 1856, 320, 120), (1010, 1818, 260, 112)]),
        # cropped branch top-right so the emptiness reads as composed
        olive(1030, 120, 210, trunk=False),
    ])


def road_finish():
    """Shot 11. hearth-amber. The only road plate that changes light — the day
    moved on while he slept."""
    cxn, cxf, hn = 0.50*W, 0.49*W, 270
    ly = round(H * 0.66)
    lcx, lh = road_edges(ly, cxn, cxf, hn)
    return write("road-finish", [
        sky("aegean", "sun"),
        hills(HORIZON + 150, 190, "storm", [(150, 430), (620, 380), (980, 300)]),
        hills(HORIZON + 96, 120, "olive", [(340, 400), (820, 360)]),
        ground("sun"),
        road(cxn, cxf, hn),
        path(f"M{lcx-lh},{ly} L{lcx+lh},{ly} L{lcx+lh},{ly+11} L{lcx-lh},{ly+11} Z", "bone"),
        # long shade pooling left off the near tree
        shade_pool(560, 1330, 520, 120, "olive-deep", op="0.40"),
        olive(880, 720, 330),                      # signature tree, close and right
        tufts([(40, 1810, 260, 112), (440, 1856, 300, 122), (1000, 1822, 250, 108)]),
    ])


def grove():
    """Shots 4, 8, 9. The road seen from under the trees — not a separate place.
    The road is visible through the trunks at the back."""
    return write("grove", [
        rect(0, 0, W, HORIZON, 0, "seafoam"),
        rect(0, HORIZON - 40, W, 130, 0, "sun"),           # the road beyond
        rect(0, HORIZON + 60, W, 18, 0, "bone"),           # dust edge
        wall(0, HORIZON + 78, HORIZON + 140, W, HORIZON + 70, HORIZON + 132, courses=11),
        rect(0, HORIZON + 140, W, H - HORIZON - 140, 0, "olive"),
        # flat shade pools — hard edges, never soft
        shade_pool(210, 1080, 300, 92, "olive-deep"),
        shade_pool(760, 1180, 330, 104, "olive-deep"),
        shade_pool(430, 1400, 380, 118, "olive-deep"),
        shade_pool(910, 1560, 300, 96, "olive-deep"),
        shade_pool(180, 1700, 340, 110, "olive-deep"),
        # trunks, staggered in depth, never evenly spaced
        rect(300, 300, 30, 1000, 8, "ink"),
        rect(690, 380, 22, 900, 6, "ink"),
        rect(940, 250, 36, 1100, 9, "ink"),
        # continuous canopy across the top — the trunks rise into it
        canopy_band(180, 300, [(60, 40, 1.05), (390, -30, 0.92), (700, 60, 1.00),
                               (1010, -10, 0.95)]),
        canopy_band(430, 190, [(210, 0, 0.9), (860, 40, 0.8)]),
        tufts([(30, 1790, 280, 130), (390, 1840, 320, 140), (810, 1800, 300, 132),
               (1060, 1770, 260, 138)]),
    ])


def perch():
    """brand-level. Frame story of every episode, every project. Deliberately
    shallow — the tale has distance, the perch does not."""
    return write("perch", [
        rect(0, 0, W, H, 0, "terracotta"),
        ell(540, 760, 620, 620, "terracotta-deep", op="0.55"),
        ell(880, 520, 460, 460, "terracotta-light", op="0.45"),   # warm source, off right
        ell(880, 520, 300, 300, "sun", op="0.20"),
        ell(540, 1740, 720, 380, "terracotta-deep", op="0.7"),
        # the branch — always the same branch, cropped both sides
        path(f"M0,1210 L{W},1136 L{W},1284 L0,1358 Z", "olive"),
        path(f"M0,1300 L{W},1226 L{W},1284 L0,1358 Z", "ink"),
        olive(170, 1076, 180, trunk=False),
        olive(560, 1040, 150, trunk=False),
        olive(950, 1090, 195, trunk=False),
        olive(60, 180, 320, trunk=False),                   # leaves cropped top-left
        olive(430, 90, 250, trunk=False),
        olive(1020, 300, 260, trunk=False),
        ell(540, 1860, 700, 260, "terracotta-deep", op="0.6"),
    ])


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for fn in (road_start, road_open, road_finish, grove, perch):
        print(f"  {fn.__name__:12s} {fn():5d} bytes")
    print(f"\n5 plates, {W}x{H}, horizon locked at {HORIZON}px (37%).")
    print("12 shots are camera positions on these — not 12 artworks.")
