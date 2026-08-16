# Object — Valley

**Cascade:** `brand/style-bible.md` → `projects/aesop/project.md` → this file.
**Scene:** `kouki-perch-valley`
**Plane:** P2 · parallax 0.35
**Canvas:** 1080 × 700, landscape
**Output:** `valley.svg`

---

## Role

The readable middle distance — the first plane where the viewer can tell what
things *are*. Far hills say "distance"; the valley says "archaic Greece". It is
the plane carrying the entire period lock, so everything in it is drawn from the
`project.md` species list and nothing else.

`project.md` is explicit: **prefer landscape to architecture.** There are no
buildings in this object. Terraces, dry stone wall lines, olive masses and one
cypress carry the era on their own.

---

## Colour lock

| Part | Token | Hex |
|---|---|---|
| Valley floor and slope | `olive` | `#6E8B4A` |
| Dry stone wall lines / terraces | `bone` | `#F7F1E4` |
| Olive tree masses | `olive-dark` | `#546C36` |
| Cypress | `olive-deep` | `#3F5227` |

Note the tree masses are `olive-dark`, one step down from the ground they stand
on. On this plane trees must separate from the ground by tone alone, since they
are too small to read by shape. The cypress goes darker still — it is vertical
punctuation against all the horizontals, per `road.md:78`, and needs the contrast
to register at this size.

---

## Prompt

```
A mid-distance valley floor and its far slope in muted olive green #6E8B4A,
terraced with three thin horizontal dry stone wall lines in warm off-white
#F7F1E4. Small simple rounded olive tree masses in darker olive #546C36
scattered unevenly along the terraces. One narrow tall cypress in deep dark
olive #3F5227, right of centre. Flat readable shapes, no interior texture. Runs
the full width of the frame.
```

## Negative

```
outlines, line art, sketch, watercolour, brush texture, paper grain, noise,
gradients, soft shading, cel shading, buildings, houses, domes, whitewash, bell
towers, arched windows, blue shutters, roads, fences, people, animals, flowers,
texture, grass blades, individual leaves, sky, clouds, horizon, blur, 3D render,
photorealism, photograph, text, watermark
```

## If it goes wrong

| Symptom | Fix |
|---|---|
| Buildings appear | Restate the period negative; add "landscape only, no structures of any kind" |
| Terraces read as roads | "Thin horizontal lines, one or two pixels of wall, never a surface" |
| Olive masses look like lollipops | "Rounded clustered masses, no visible trunks at this distance" |
| Cypress reads as a pine | "Narrow, tall, straight-sided, blunt-topped" |
| Ground and trees merge | Trees must be `olive-dark` #546C36 against `olive` #6E8B4A — check the model is honouring both |
| Whitewashed village appears | The classic failure. Period block was dropped or reworded — restore verbatim |
