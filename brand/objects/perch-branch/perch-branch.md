# Object — Perch branch

**Cascade:** `brand/style-bible.md` → `projects/aesop/project.md` → this file.
**Scene:** `kouki-perch-valley`
**Plane:** P3 · parallax 1.00
**Canvas:** 1080 × 300, landscape strip
**Output:** `perch-branch.svg`

---

## Role

Kouki's seat, and the most load-bearing object in the scene despite being the
simplest. It is generated separately from `olive-tree` for one reason: Kouki must
sit **on** it with her feet in contact, and a branch buried inside the tree asset
cannot be positioned against her independently.

`perch.md` calls it "always the same branch, cropped both sides". It reads left
to right across the frame, thicker where it would meet the trunk.

**Nothing is perched on it.** Models add a bird to an empty branch almost every
time; the negative below is doing real work.

---

## Colour lock

| Part | Token | Hex |
|---|---|---|
| Branch body | `olive` | `#6E8B4A` |
| Underside shadow | `olive-deep` | `#3F5227` |
| Leaf clusters | `olive` | `#6E8B4A` |

Flat two-tone: base plus one shadow along the underside only. The shadow sits
low because the light is upper-left, and it is what gives a flat bar of colour
enough weight to look sat-upon.

---

## Prompt

```
One single horizontal olive branch running left to right, thicker at the left
where it would meet a trunk and tapering gently to the right. Muted olive green
#6E8B4A with one flat darker olive #3F5227 shadow shape along its underside
only. Two small simple leaf clusters growing from it. Roughly straight, gently
tapering, no forks. Nothing sitting or perched on it, no birds, no animals.
```

## Negative

```
outlines, line art, sketch, watercolour, brush texture, paper grain, noise,
gradients, soft shading, cel shading, bark texture, twigs, forks, branching,
birds, owl, animals, nest, fruit, olives, blossom, flowers, tree, trunk, ground,
sky, leaves in detail, veins, blur, 3D render, photorealism, photograph, text,
watermark
```

## If it goes wrong

| Symptom | Fix |
|---|---|
| A bird appears on it | Near-universal. Keep "Nothing sitting or perched on it, no birds" in the subject **and** the negative |
| Branch forks or branches | "Roughly straight, no forks" — one continuous taper |
| Whole tree generated | Strengthen `[ISOLATE]`; add `tree, trunk` to the negative |
| Too thin to sit on | "Thick and solid at the left, substantial enough to bear weight" |
| Shadow on the wrong edge | Underside only. Light is upper-left project-wide |
| Reads as a stick | Add the two leaf clusters back — they are what make it living wood |
