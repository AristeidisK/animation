# Location — The Grove

**Cascade:** `brand/style-bible.md` → `projects/aesop/project.md` → this file.

**Shots:** 4, 8, 9. One plate, three camera positions.

**Scene key:** `olive-shade` throughout.

---

## The idea

This is the road seen from *under the trees* — not a separate place. The grove
sits on the left of the road, and the road itself is visible through the trunks
at the back of frame. That single decision keeps the geography honest: he falls
asleep beside the course he is racing on, and she walks past him on it.

Cool, still, and much darker than the road plates. The temperature drop is the
point — it is why he lies down.

---

## Build

| Plane | Content | Tokens |
|---|---|---|
| P0 | Sky, visible only in gaps between canopies | `seafoam` #79C4C0 |
| P1 | The road beyond the grove, a pale band | `sun` #F2B33D, `bone` dust |
| P2 | Trunks — four olives, staggered in depth, not evenly spaced | `ink` #23212B |
| P3 | Grove floor, dappled but **flat** | `olive` #6E8B4A ground, `olive-deep` shade pools |
| P4 | Broad canopy mass cropped by the top edge, plus grass tufts bottom | `olive`, `seafoam` highlights |

- **Horizon** stays at 37%, same as the road plates, though mostly occluded.
- **Light** still upper left, but broken. Shade pools on the floor are flat
  `olive-deep` shapes with hard edges — never soft, never gradient. Six or seven
  irregular pools, larger toward the back.
- **The broad olive** he sleeps under is the near-left trunk, its canopy filling
  the top third and cropped by the frame edge.
- **Dry stone wall** runs across the back at the grove's edge, `bone` with
  `storm` shadow faces, separating grove from road.
- **Tall grass** in the P4 foreground, `olive-deep`, cropped by the bottom edge —
  this is what the tortoise passes behind in shot 9.

---

## Path

She walks left-to-right *across* the frame here rather than into it, because the
grove runs parallel to the road. Depth change is small; the movement is lateral
with a slight rise.

```
path:
  near:      [18, 68, 0.62]
  far:       [86, 62, 0.52]
  vanishing: [52, 37]
  curve:     straight
```

**Shot 9 note:** she passes *behind* the P4 grass and *in front of* the sleeping
hare. That ordering is the shot — it is what makes "she didn't stop to look"
read without a word of narration.

---

## Camera positions

| Shot | Framing | Note |
|---|---|---|
| 4 | Low | Camera near the floor, looking slightly up. Tortoise centred low, canopy heavy above her — she is small and the world is big, and she is unbothered |
| 8 | Wide | The sleeping hare off-centre right beneath the near trunk. Hold long. Nothing moves but leaf shapes |
| 9 | Tracking | Lateral move following her along the path. Foreground grass parallaxes fast across the lens; the hare stays put and slides out of frame behind her |
