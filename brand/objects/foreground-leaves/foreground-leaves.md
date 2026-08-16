# Object — Foreground leaves

**Cascade:** `brand/style-bible.md` → `projects/aesop/project.md` → this file.
**Scene:** `kouki-perch-valley`
**Plane:** P4 · parallax 1.80
**Canvas:** 700 × 700, square
**Output:** `foreground-leaves.svg`

---

## Role

The nearest plane, and the one that does the most work per pixel. `tokens.json`
is blunt about it: **"P4 cropping is what sells the depth. Every exterior scene
needs a P4 element."**

At parallax 1.80 this moves nearly twice as fast as the subject plane. That
speed differential against the near-static far hills is what the eye reads as
depth — more than scale, more than overlap.

**Generated whole, composited cropped.** It must be pushed partly outside the
canvas at composite time. An uncropped foreground element reads as a floating
bush and actively destroys the effect it exists to create.

---

## Colour lock

| Part | Token | Hex |
|---|---|---|
| Leaves and twig | `olive-deep` | `#3F5227` |

**One colour, near-silhouette.** No highlight clumps here — the silver flash
belongs to `olive-tree` on the subject plane, and repeating it forward flattens
the distinction between the two planes. This object is dark because it is close
and unlit, and its flatness is what keeps the eye travelling past it into the
scene rather than stopping on it.

---

## Prompt

```
One dense cluster of olive leaves on a thin twig, in deep dark olive green
#3F5227, near-silhouette and clearly darker than any other foliage. Simple
pointed leaf shapes, flat, no veins and no interior detail, all one single
colour. Dense at the lower left and thinning toward the upper right. Fills most
of the frame.
```

## Negative

```
outlines, line art, sketch, watercolour, brush texture, paper grain, noise,
gradients, soft shading, cel shading, highlights, second colour, silver, veins,
leaf detail, stems in detail, flowers, blossom, fruit, olives, birds, animals,
whole tree, trunk, ground, sky, background scenery, blur, depth of field, bokeh,
3D render, photorealism, photograph, text, watermark
```

## If it goes wrong

| Symptom | Fix |
|---|---|
| Highlights or a second tone appear | One colour only — restate "all one single colour, near-silhouette" |
| Too light, competes with the tree | Must be `olive-deep` #3F5227. If it reads as mid-ground it is too pale |
| Sparse, floats in frame | "Fills most of the frame, dense at the lower left" |
| A whole tree is generated | Strengthen `[ISOLATE]`; add `whole tree, trunk` to the negative |
| Reads as a bush in the scene | Not a generation fault — it is not cropped hard enough at composite time |
