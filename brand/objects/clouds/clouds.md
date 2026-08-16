# Object — Clouds

**Cascade:** `brand/style-bible.md` → `projects/aesop/project.md` → this file.
**Scene:** `kouki-perch-valley`
**Plane:** P0 · parallax 0.08
**Canvas:** 1080 × 420, landscape strip
**Output:** `clouds.svg`

---

## Role

The only moving thing in the top third of frame. Their job is to stop the sky
reading as a printed backdrop — nothing more. They must never compete with the
tree or with Kouki for attention, and they must never gather into weather.

Sparse is correct. Four shapes, widely spaced, unequal. A carpet of cloud reads
as overcast, which is the `storm-grey` scene key and the wrong mood entirely.

---

## Colour lock

| Part | Token | Hex |
|---|---|---|
| Cloud body | `bone` | `#F7F1E4` |
| Underside shadow | `seafoam` | `#79C4C0` |

The underside shadow is `seafoam`, not grey and not a darker white — it is the
sky bouncing back up into the cloud, and it ties the clouds to the sky gradient
they sit in front of. Two tones only.

---

## Prompt

```
Four simple flat cloud shapes built from overlapping circles and rounded
rectangles, warm off-white #F7F1E4, each with one flat pale seafoam #79C4C0
shadow shape along its underside only. Unequal sizes, widely spaced, arranged in
a loose horizontal band across the frame. Flat-bottomed, rounded on top. No
wisps, no tapering tails, no fluff, no rendering.
```

## Negative

```
outlines, line art, sketch, watercolour, brush texture, paper grain, noise,
gradients, soft shading, cel shading, fluffy, wispy, cirrus, storm clouds, dark
clouds, rain, overcast, sky, horizon, ground, sun, sunbeams, god rays, lens
flare, blur, 3D render, photorealism, photograph, text, watermark, pure white
```

## If it goes wrong

| Symptom | Fix |
|---|---|
| Wispy or feathered edges | Insist "built from overlapping circles, flat-bottomed" — the shape must be constructible from two primitives |
| Clouds gather into a mass | "Four separate clouds, widely spaced, large gaps of empty frame between them" |
| Reads as overcast | Too many, too large, or too grey. Reduce count before touching colour |
| Grey undersides | Shadow is `seafoam` #79C4C0, never a desaturated white |
| Sky generated behind them | Strengthen `[ISOLATE]`; the magenta must be the only background |
