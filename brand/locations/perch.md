# Location — The Perch

**Cascade position:** `brand/` — MASTER level, not a project.

This is deliberate. Kouki's branch is the frame story of **every episode in every
project** — Aesop, Greek folk tales, British tales alike. It is the one place a
viewer sees in all of them, and it is the strongest cohesion device the channel
has. A viewer arriving at episode 30 of any series knows within four seconds
that it belongs to the same channel.

It therefore does **not** inherit any project's era or species list. It is
outside the story, always.

**Shots:** first and last of every episode. Episode 001 shots 1 and 12.

**Scene key:** `hearth-amber`.

---

## The idea

Warm, close, enclosed — the opposite of wherever the tale goes. Lamplit rather
than sunlit. It should feel like the moment before a story starts and the moment
after it ends, and it should never compete with the tale for attention.

Deliberately **shallow**: two planes, almost no depth. The tale has distance;
the perch does not. That contrast is doing work.

---

## Build

| Plane | Content | Tokens |
|---|---|---|
| P0 | Warm ground, flat, unlit corners falling off | `terracotta` #D0603C |
| P2 | Soft rounded shapes suggesting a sheltered space — no readable architecture | `terracotta-deep`, `ink` |
| P3 | The branch, crossing the lower third | `olive` #6E8B4A, `ink` shadow face |
| P4 | Olive leaves cropped by the frame edge | `olive`, `seafoam` highlights |

- **The branch is always the same branch.** One thick horizontal limb with a
  slight rise to the right, crossing at 62% down frame, cropped by both side
  edges. It never changes between episodes.
- **Leaves:** clusters of `olive` with `seafoam` upper highlights, cropped
  top-left in shot 1 and top-right in shot 12 — the only difference between the
  opening and closing plates.
- **A single warm light source** off frame right. One soft `sun` #F2B33D pool on
  the branch where she sits. Everything else falls to `terracotta-deep`.
- **No horizon. No sky. No architecture.** If a viewer can tell what building
  she is in, the plate is wrong.
- **Never keyed `dusk-violet`** — that would put her plum against a plum ground
  and dissolve her silhouette. See the plum lock.

---

## Path

None. She does not travel. She is perched, and the camera moves instead: a slow
push in on the opening, a slow pull back on the close.

```
placement:
  open:  [62, 56, 0.42]     # shot 1  — she looks at camera
  close: [38, 56, 0.42]     # shot 12 — she looks away, and we leave
```

The side she sits on flips between open and close. It is a small thing and it
reads as an ending.
