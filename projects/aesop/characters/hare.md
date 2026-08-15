# Character — The Hare

**Cascade:** `brand/style-bible.md` → `projects/aesop/project.md` → this file.
**Built by:** `pipeline/build_cast.py::hare()` → `brand/characters/hare.svg`

Drawn, never generated. Asking a model for a hare produced a dog.

---

## 1. Colour lock — from `tokens.json`

He is **`sun`**. One hue, always, in every episode he appears in.

| Part | Token | Hex |
|---|---|---|
| Body, head, haunch, ears | `sun` | `#F2B33D` |
| Shadow side, outer ear, head rim | `sun-dark` | computed −10% L |
| Far limbs, foot pads, deepest shade | `sun-deep` | computed −18% L |
| Belly, muzzle, tail | `bone` | `#F7F1E4` |
| Inner ear, nose | `terracotta` | `#D0603C` |
| Eye | `ink` | `#23212B` |
| Catchlight | `bone` | `#F7F1E4` |

Second tones are **computed in HLS from the palette**, never invented — see
`shift()` in the builder. Ten tokens yield forty tones and none of them can
drift from the brand.

**He must never be drawn on a `sun` or `terracotta` ground.** He is gold; the
land is gold. Put him on `olive`, `seafoam` or `aegean` or he disappears. This is
why the scene ramps were rebalanced.

---

## 2. Silhouette lock

Long and low. The shape must read as *speed at rest* — a coiled thing.

- Body a long horizontal ellipse; haunch a large circle behind it, higher than
  the shoulder. The haunch is the whole character: it is where the speed lives.
- Two tall ears, near-vertical, slightly splayed, the left raked back further
  than the right. Never symmetrical, never floppy.
- Head small relative to the haunch. Overconfidence reads better on a small head.
- Feet long and flat on the ground.
- Identifiable as him with the fill set to solid black.

---

## 3. Face

- **Eye:** one solid `ink` circle with a `bone` catchlight up-left. No lid, no lash.
- **Muzzle:** a soft `bone` ellipse, low and forward.
- **Nose:** small `terracotta` ellipse at the muzzle's tip.
- **No mouth.** Expression comes from the ears and the tilt of the head.
- **No whiskers.**

---

## 4. Never

- Never with individual fur, texture, or gradient shading
- Never with separated toes beyond the three flat pads
- Never standing on his hind legs like a cartoon rabbit — he is a hare, and he
  stays horizontal
- Never in the frame story; he exists only inside the tale
- Never plum, in any part, ever — that is Kouki's alone

---

## 5. Prompt block

For reference or for a model that ever needs to match him. The built SVG is the
source of truth; this is the description of it.

```
A stylised hare in flat vector, no outlines. Long low golden-yellow body with a
large rounded haunch behind, higher than the shoulder. Two tall near-vertical
ears, slightly splayed and asymmetric, dark golden outer and warm terracotta
inner. Small head, soft cream muzzle, small terracotta nose, one solid dark eye
with a single cream catchlight, no mouth. Cream belly, cream tail. Flat
two-tone shading only: a darker gold shadow shape along the underside, no
gradients, no texture, no outlines. Reads as coiled speed at rest.
```
