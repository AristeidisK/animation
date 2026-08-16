# Object — Olive tree

**Cascade:** `brand/style-bible.md` → `projects/aesop/project.md` → this file.
**Scene:** `kouki-perch-valley`
**Plane:** P3 · parallax 1.00
**Canvas:** 900 × 1200, portrait
**Output:** `olive-tree.svg`

---

## Role

The subject-plane anchor. Kouki perches on its branch, so this tree is the thing
the whole frame is built around — it must be broad enough to feel sheltering and
low enough that a perched owl sits comfortably inside its mass rather than on
top of it.

`project.md` species table: **"Low, broad, gnarled. Rounded foliage mass, never a
lollipop. Silver underside is the whole point."** That silver flash is the single
detail that separates an olive from a generic tree, and it is the thing models
drop first.

Generated whole and complete. The composite crops it, not the generator.

---

## Colour lock

| Part | Token | Hex |
|---|---|---|
| Trunk and limbs | `ink` | `#23212B` |
| Canopy masses | `olive` | `#6E8B4A` |
| Silver highlight clumps | `seafoam` | `#79C4C0` |

The trunk is `ink`, not brown. There is no brown in `tokens.json` — olive bark
in this system reads as near-black silhouette, exactly as `build_plates.py:75`
draws it. Highlight clumps sit on the **upper left of each mass**, because the
light is locked upper-left across the whole project (`road.md:20`).

---

## Prompt

```
One broad olive tree, whole and complete. A dark charcoal #23212B trunk, low and
thick and gnarled, splitting into three heavy limbs. A canopy of five
overlapping rounded foliage masses in muted olive green #6E8B4A, each carrying
one pale seafoam #79C4C0 highlight clump on its upper left. Broad, low and
wide-spreading, wider than it is tall. Never a lollipop, never a cone, never a
conifer, never a single round blob.
```

## Negative

```
outlines, line art, sketch, watercolour, brush texture, paper grain, noise,
gradients, soft shading, cel shading, bark texture, individual leaves, veins,
branches with twigs, lollipop tree, single round canopy, cone shape, conifer,
pine, cypress, palm, brown trunk, roots, fruit, olives, birds, animals, ground,
grass, sky, shadow, blur, 3D render, photorealism, photograph, text, watermark
```

## If it goes wrong

| Symptom | Fix |
|---|---|
| Lollipop — one round blob on a stick | "Five overlapping masses" is the fix; say *five*, not "clustered" |
| Silver highlights missing | The most common failure. Restate "one pale seafoam clump on the upper left of EACH mass" |
| Trunk comes back brown | No brown exists in the palette. Insist on charcoal #23212B |
| Too tall, reads as a poplar | "Wider than it is tall" — broad and low is the whole silhouette |
| Highlights on the wrong side | Light is locked upper-left project-wide. Restate the direction |
| Canopy too detailed | Strengthen `individual leaves, twigs` in the negative |
