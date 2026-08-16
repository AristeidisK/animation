# Objects

Single isolated assets, generated one at a time and composited as layers.

Plates (`brand/plates/`) are whole backgrounds drawn in one piece. Objects are
the opposite approach: each element generated alone, on its own transparent
layer, so the renderer can move them independently. That independence is the
entire point — a plate can only be pushed in on, whereas a stack of objects has
parallax, and parallax is what makes a flat scene read as deep.

**Cascade:** `brand/style-bible.md` → `projects/aesop/project.md` → `<object>/<object>.md`

---

## Scene: `kouki-perch-valley` — the demo

Kouki on a branch of an olive tree, the tree standing in a valley, hills behind,
blue sky with a little cloud.

| # | Layer | Plane | Parallax | Source |
|---|---|---|---|---|
| 1 | Sky gradient | P0 | 0.00 | **Code** — see below |
| 2 | `clouds` | P0 | 0.08 | Generated |
| 3 | `far-hills` | P1 | 0.15 | Generated |
| 4 | `valley` | P2 | 0.35 | Generated |
| 5 | `olive-tree` | P3 | 1.00 | Generated |
| 6 | `perch-branch` | P3 | 1.00 | Generated |
| 7 | Kouki | P3 | 1.00 | `brand/characters/Owl/kouki.svg` |
| 8 | `foreground-leaves` | P4 | 1.80 | Generated |

Parallax values come from `tokens.json:planes` and are not free parameters.
Clouds are the one deviation: P0 is specified as 0.00, but a dead sky behind a
moving landscape reads as a printed backdrop, so they get a slight independent
drift.

### The sky is not generated

`build_plates.py:38` already draws it: a single vertical gradient, `aegean`
#1F5FA8 at the top to `seafoam` #79C4C0 at the horizon. It is the only gradient
the style bible permits, it is exact in SVG, and a generated version would only
introduce banding. There is no `sky/` folder on purpose.

---

## How an object is generated

Every prompt assembles in this fixed order:

```
[STYLE] + [PERIOD] + [ISOLATE] + [SUBJECT]
```

`[STYLE]`, `[PERIOD]` and `[ISOLATE]` are pasted verbatim from
`brand/prompt-kit.md` and the block below. Only `[SUBJECT]` changes per object,
and it lives in that object's own `.md`. Rewording the fixed blocks is the most
common cause of an asset that will not sit with the others.

### `[ISOLATE]` — fixed, every object

```
One single isolated object, centred, complete and uncropped, on a plain flat
magenta #FF00FF background. Nothing else in frame — no ground, no sky, no
horizon, no other objects, no shadow cast onto the background.
```

**Preferred output — Recraft V3, `style: vector_illustration`.** Returns real
SVG with true transparency, no keying, and drops straight into the existing SVG
pipeline.

**Fallback — raster keyed off magenta.** Never ask a model for a "transparent"
or "white" background; it will fake both and leave a fringe you cannot key.
Magenta #FF00FF appears nowhere in `tokens.json` and cannot occur in the art, so
the key is lossless.

---

## Colour law

Every hex in every object file is a `tokens.json` token or a tone computed from
one by `build_cast.py:shift()`. Nothing here invents a colour. If an object
seems to need a colour outside the palette, that is a signal to escalate, not to
pick one.

| Token | Hex | dark | deep | light |
|---|---|---|---|---|
| `ink` | #23212B | #141219 | #13121A | #393644 |
| `bone` | #F7F1E4 | #EDDDBB | #E5CD9A | #FAF6EE |
| `aegean` | #1F5FA8 | #15477F | #0E335D | #2975CC |
| `sun` | #F2B33D | #F0A10C | #CB8708 | #F3C36A |
| `terracotta` | #D0603C | #B24927 | #923A1E | #D77F63 |
| `olive` | #6E8B4A | #546C36 | #3F5227 | #85A55E |
| `plum` | #6B4A78 | #50345B | #392442 | #835E92 |
| `seafoam` | #79C4C0 | #52B8B3 | #3FA29D | #9AD1CE |
| `storm` | #8B93A0 | #6C788C | #586477 | #A6ABB3 |
| `deepsea` | #123A68 | #09223E | #051526 | #1A508D |

`plum` is reserved for Kouki and must not appear in any object.
