# Location — The Road

**Cascade:** `brand/style-bible.md` → `projects/aesop/project.md` → this file.
Inherits the era lock, the species list, the colour law and the vertical grammar.
Specialises them for one place.

**Shots:** 2, 3, 5, 6, 7, 10, 11 — seven of the twelve. Three plates.

---

## Shared world — all three plates must agree

These three are the same road at three points along it. If any of the following
differs between plates, the geography breaks and the film reads as three
disconnected sets.

| Property | Value |
|---|---|
| **Horizon** | 37% from top of frame, dead level, on every plate |
| **Light** | Hard sun from upper left. Every cast shadow falls lower-right, `ink` at 15%, zero blur |
| **Sky** | Single vertical gradient, `aegean` #1F5FA8 at top → `seafoam` #79C4C0 at horizon. The one permitted gradient |
| **Far hills** | `storm` #8B93A0, flat silhouette, no interior detail, same profile across all three |
| **Mid hills** | `olive` #6E8B4A, terraced with `bone` #F7F1E4 dry stone wall lines |
| **Road surface** | `terracotta` #D0603C, with `bone` #F7F1E4 dust scuffs |
| **Verges** | `sun` #F2B33D dry grass, sparse `terracotta` poppy dots (6–8 max, never a carpet) |
| **Signature tree** | One olive, left of road, present on all three plates at different distances — it is how the viewer knows it is one road |

### Plane stack — every plate

```
P0  sky          gradient, parallax 0.00
P1  far hills    storm, flat silhouette,        parallax 0.15
P2  mid hills    olive + wall lines,            parallax 0.35
P3  road + verge the subject plane,             parallax 1.00
P4  foreground   grass tufts / olive branch,    parallax 1.80  — cropped by frame edge
```

---

## §A — Road, start

**Shots 2, 3, 5, 6.** Where the boast happens and the race begins.

The widest, most populated plate. The road enters bottom-centre-right and runs
away to the vanishing point. A low dry stone wall runs along the left verge — it
gives the crowd somewhere to sit and gives the eye a line into depth. The
signature olive stands close, left, its canopy cropped by the top-left corner.

- **Start line:** a shallow scratch drawn across the road in `bone`, at 62% down
  frame, wide enough to read at thumbnail size
- **Dry stone wall:** `bone` blocks, `storm` shadow faces, running from the left
  edge diagonally to the vanishing point
- **Foreground:** grass tufts in `sun` and `olive-deep`, cropped by the bottom edge
- **Poppies:** six, clustered right verge, mid-distance

```
path:
  near:      [58, 76, 1.00]
  far:       [47, 39, 0.24]
  vanishing: [46, 37]
  curve:     straight
```

---

## §B — Road, open

**Shots 7, 10.** The long empty middle. The loneliest plate — this is where the
hare's lead is made visible.

Almost nothing in it. The road curves gently right and disappears over a low
rise, so the vanishing point is *hidden* — which is exactly what sells "so far
ahead he couldn't see her." No wall, no crowd, no buildings. One cypress far
right as vertical punctuation against all the horizontals.

- **Rise:** the road crests at 44% down frame and the far side is not visible
- **Signature olive:** far back, small, left — the same tree from §A seen from
  further along
- **Cypress:** single, right, `olive-deep`, tall and narrow
- **Verges:** wider here, more `sun` grass, no poppies — drier ground
- **Foreground:** a single cropped olive branch, top-right, to stop the emptiness
  reading as an unfinished frame

```
path:
  near:      [54, 80, 1.00]
  far:       [52, 44, 0.20]
  vanishing: [52, 42]
  curve:     right
```

---

## §C — Road, finish

**Shot 11.** Where she is already standing. Warm, quiet, enclosed.

Scene key shifts to `hearth-amber` — late afternoon, the light gone long and
gold. This is the only road plate that changes light, and it is deliberate: the
day has moved on while he slept.

The signature olive is now close and large on the right, its shade falling
across the road. The finish is a scratch in the dust beside its trunk. A few
flat animal shapes stand around, quiet rather than cheering.

- **Light:** still upper left, but lower and warmer. Shadows longer, `ink` at 18%
- **Sky:** `sun` #F2B33D at the horizon band, `aegean` retained at the very top
- **Signature olive:** right, close, canopy cropped by the top-right corner, its
  shadow pooling `olive-deep` across the road
- **Finish line:** `bone` scratch across the road at 66% down frame
- **Foreground:** long grass, cropped bottom-left

```
path:
  near:      [50, 72, 0.85]
  far:       [49, 46, 0.32]
  vanishing: [49, 43]
  curve:     straight
```

---

## Drawing notes

- The three plates share a hill profile. Draw §A first and reuse its far-hill
  silhouette in §B and §C, shifted and rescaled — never redrawn from scratch.
- Olive canopies are **clustered rounded masses**, not one blob and not a
  lollipop. Three to five overlapping ellipses, with `seafoam` highlight clumps
  on the upper-left of each — that silver flash is what makes an olive read as
  an olive rather than as a generic tree.
- The road narrows toward the vanishing point on a straight taper. Give it a
  soft `bone` dust edge on the sunlit left side only.
- No figures are drawn into the plates. Characters are composited.
