# Character — The Hare

**Cascade:** `brand/style-bible.md` → `projects/aesop/project.md` → this file.
**Reference:** matches `../Owl/Owl - 01.png` and `Owl - 03.png` in construction,
shading and eye treatment. They are siblings and must read as one cast.

Aesop's animal is a **hare**, not a rabbit — longer ears, longer legs, leaner.
Worth keeping: the fable is about arrogance in something genuinely fast.

---

## Shared house style — identical to the Owl

Every cast member inherits this block verbatim.

- Rounded **squircle** body — a wide, soft rounded rectangle. Never a plain oval.
- **No outlines anywhere.** Shapes read by colour contrast alone.
- **Flat two-tone shading only:** one base colour plus a single slightly darker
  flat panel down the right side. Restrained. No gradients, no modelling.
- **One small white catchlight** per eye, upper-right of the pupil.
- **Thick short dark brows** floating above the eyes with a clear gap.
- Square 1:1, character centred, flat solid background.

**Difference from Kouki:** she has golden eye discs; they are an owl trait and
they are hers alone. The hare and tortoise have large dark eyes set straight on
the body colour. Same family, different signature.

---

## Colour lock

| Part | Token | Hex |
|---|---|---|
| Body, head, ears (outer) | `sun` | `#F2B33D` |
| Right-side shadow panel | `sun-dark` | `#F0A18C`-range, computed −10% L |
| Belly, muzzle, tail | `bone` | `#F7F1E4` |
| Inner ear, nose, feet | `terracotta` | `#D0603C` |
| Eyes, brows | `ink` | `#23212B` |
| Catchlight | white | — |
| Grass tuft | `olive` | `#6E8B4A` |

Never on a `sun` or `terracotta` background — he is gold and would vanish.

---

## Prompt

```
A stylised hare character for a preschool animated television series. Flat
vector illustration, square format, one character centred on a plain solid
background. No outlines anywhere — every shape reads by colour contrast alone.

Body: a soft rounded squircle, wide and slightly tapered, sitting upright in a
crouch. Warm golden-yellow (#F2B33D). A large cream rounded belly shape
(#F7F1E4) filling the lower half. Two long upright rounded ears rising from the
top of the head, golden outside with a narrower warm terracotta inner shape
(#D0603C). A small cream muzzle and a small terracotta nose. Two rounded
terracotta feet at the base. A short round cream tail.

Face: two large circular dark charcoal eyes (#23212B), each with one small white
catchlight in the upper right. Two thick short dark eyebrow strokes floating
above the eyes with a clear gap, angled very slightly. No mouth.

Shading: flat two-tone only — the golden base plus a single slightly darker flat
panel down the right side of the body. No gradients, no texture, no rendering.

Perched on a simple olive-green grass tuft. Chunky, warm, confident, a little
pleased with himself. Clean flat background, generous negative space.
```

## Negative

```
outlines, line art, black outlines, sketch, watercolour, brush texture, paper
grain, noise, gradients, soft shading, ambient occlusion, specular highlights,
depth of field, blur, 3D render, CGI, photorealism, photograph, realistic fur,
individual fur strands, whiskers, sharp claws, bared teeth, angry expression,
scary, text, watermark, signature, pure black, pure white, multiple characters
```

## If it goes wrong

| Symptom | Fix |
|---|---|
| Reads as a rabbit | Lengthen the ears, lengthen the back legs, say "hare, lean and long-legged" |
| Body too oval | Insist on "rounded squircle, a wide rounded rectangle, never an oval" |
| Ears floppy | "Two long UPRIGHT ears rising from the top of the head" |
| Too cute / babyish | Remove "chunky", add "alert and athletic"; keep brows level not raised |
| Vanishes into background | Background must be `olive`, `seafoam`, `aegean` or cream — never gold |
