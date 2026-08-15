# Project — Aesop

**Cascade position:** child of `brand/`. Inherits `tokens.json`, `style-bible.md`
and `prompt-kit.md`. May narrow them. May never contradict them.

Every character and location file in this project inherits *this* file. Read the
chain top-down before drawing anything:

```
brand/style-bible.md          construction, tone, episode architecture
  └── projects/aesop/project.md          era, world, species, palette subset
        ├── characters/*.md              one cast member each
        └── locations/*.md               one place each, with its path spec
              └── episodes/NNN/shots.json    camera position per shot
```

---

## 1. Era — locked

**Archaic Greece, 6th century BC.** Aesop's own era.

Everything in frame must be from within it. This is not a stylistic preference;
it is a hard constraint, and it is the reason backgrounds are drawn rather than
generated — a model can be *asked* for a period, a drawn plate simply *is* one.

**Never in frame:** domes, crosses, bell towers, arched windows, whitewashed
villages, blue shutters, plaster render, glass, metal roofing, wheeled carts
with spoked wheels, anything Byzantine, Ottoman or modern.

**Correct for the period:** rough undressed stone, mud brick, timber posts, low
shallow-pitched terracotta pantiles, small square door openings, dry stone field
walls, threshing floors, clay amphorae, woven baskets, goat tracks.

Most Aesop fables are animal stories in open country. **Prefer landscape to
architecture.** If a fable does not need a building, do not draw one.

---

## 2. The world — Greek countryside, late spring

Hot, dry, high-contrast light. Grass already gone gold; hills still holding
green in the folds. Cicadas weather.

### Species — draw these, not generic trees

| Element | Form | Tokens |
|---|---|---|
| **Olive** | Low, broad, gnarled. Rounded foliage mass, never a lollipop. Silver underside is the whole point. | `olive` #6E8B4A mass, `seafoam` #79C4C0 highlight clumps, `ink` #23212B trunk |
| **Cypress** | Tall, narrow, vertical. Used sparingly as punctuation — one or two, never a row. | `olive-deep` or `ink` silhouette |
| **Fig** | Broad hand-shaped leaves, open crown, lower than olive | `olive-light` |
| **Oleander** | Roadside shrub, dense, with sparse pink-red flower dots | `olive` mass, `terracotta` flowers |
| **Dry grass** | Verges, hillsides, everything not shaded | `sun` #F2B33D |
| **Poppies** | Scattered dots in the verge. Late spring only. Sparse — six or eight, never a carpet. | `terracotta` #D0603C |
| **Limestone** | Outcrops, dry stone walls, road dust | `bone` #F7F1E4, shaded `storm` #8B93A0 |
| **Earth** | The road itself, bare ground | `terracotta` #D0603C |
| **Far hills** | Hazed, flat, no interior detail | `storm` #8B93A0 or `deepsea` #123A68 |
| **Sky** | Hard, high, cloudless | `aegean` #1F5FA8 to `seafoam` #79C4C0 at horizon |

### Colour law for this project

Inherits the warm-balance rule from `tokens.json`. Restated for the countryside:

- **The land is gold and green. The distance is blue.** `sun` for dry grass,
  `olive` for foliage, `aegean`/`storm` for distance.
- **`terracotta` is earth and flowers only** — the road surface and poppy dots.
  It never grounds a scene here and never sits in a large mass beside `sun`.
- **`seafoam` does double duty**: olive-leaf silver, and the pale band where sky
  meets hill. It is what stops the greens going flat.
- **`plum` is forbidden in Aesop backgrounds.** It belongs to Kouki alone.
- **One vertical sky gradient per plate** — the single gradient the bible allows.
  Nothing else gradients, ever.

---

## 3. Vertical format — the rule that shapes every location

The frame is **1080 × 1920**. This is not a landscape composition cropped; it is
a different grammar, and getting it wrong is why vertical animation usually
looks wrong.

- **The horizon sits at 34–40% from the top.** That leaves ~60% of the frame for
  ground, which is where the story happens.
- **Depth runs up the frame, not across it.** A road recedes from the bottom
  edge toward a vanishing point near the horizon. A character travelling along
  it moves *up* frame and *shrinks*. That reads as real distance.
- **Never pan horizontally.** In 9:16 a horizontal pan shows almost no new
  information and reads as a mistake. Camera moves are push, pull, and vertical
  tilt.
- **Every plate declares a path** (§4) so movement is perspective-correct rather
  than a sprite sliding sideways.
- **Keep the lower 22% clear of story detail** — burnt-in subtitles live there.
- **Compose subjects centrally.** A 16:9 crop may be pulled from these later.

---

## 4. Path specification — required in every location file

A path lets a character walk *into* the picture correctly. Coordinates are
percentages of frame width and height; `scale` is relative to the character
SVG's natural size.

```
path:
  near:      [x%, y%, scale]     where the character enters, closest to camera
  far:       [x%, y%, scale]     where it exits, at the vanishing point
  vanishing: [x%, y%]            must sit on the horizon
  curve:     straight | left | right
```

Scale must fall roughly with distance — a character at the vanishing point sits
near `0.2`, at the near edge near `1.0`. Anything flatter than that kills the
depth the plate is built to create.

---

## 5. Plate inventory

Five plates cover the whole of episode 001. Shots are camera positions on
plates, not separate artworks.

| Plate | File | Shots | Owner |
|---|---|---|---|
| Perch | `brand/locations/perch.md` | 1, 12 | brand — every project |
| Road, start | `locations/road.md` §A | 2, 3, 5, 6 | aesop |
| Road, open | `locations/road.md` §B | 7, 10 | aesop |
| Road, finish | `locations/road.md` §C | 11 | aesop |
| Grove | `locations/grove.md` | 4, 8, 9 | aesop |

The three road plates are the same road at three points along it, and must share
a horizon height, a light direction and a hill silhouette so they read as one
continuous country.
