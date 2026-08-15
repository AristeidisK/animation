# Host character — the Owl

**Status:** locked spec, unbuilt.
**Role:** frame narrator. Opens and closes every episode. Never appears inside the tale.
**Screen time:** 2–4 shots per episode. One locked sheet carries the whole catalogue.

Supersedes the earlier grandmother spec. The reasoning is in §2.

---

## 1. Name

Working name: **Kouki** — short for κουκουβάγια. Warm to a Greek ear, sayable by an
English four-year-old, and not a word that means anything else.

Alternatives if it doesn't sit right: **Bouboú**, **Nyx** (owls are night birds;
also a Greek primordial goddess, which is either perfect or too much), or
**Glafki** (from γλαύκα, the classical owl — the most literary, the least sayable).

Not recommended: Sofia. Wisdom-as-a-name is the joke everyone makes.

---

## 2. Why an owl, and why this one

Athena's owl is on the Athenian tetradrachm. It is the oldest continuously
recognisable Greek symbol there is, it reads as *storyteller* in English without
explanation, and it costs nothing to establish.

It also solves a production problem. A human face is the least consistent thing
an image model produces — every frame renegotiates the eyes, the nose, the age.
An owl built from two circles and a dome renegotiates nothing. The design below
is chosen for reproducibility first and charm second, on the theory that a
character who looks the same in episode 40 is more charming than one who doesn't.

---

## 3. The three locks

Non-negotiable, and present in every prompt that includes her.

**1. Silhouette lock.** A rounded dome — wider than tall at the base, tapering to
two blunt ear tufts. No visible legs, no separated wings at rest. The whole bird
is one continuous mass. It must be identifiable with the fill set to solid black.

**2. Colour lock.** She is the only `plum` (#6B4A78) object in any frame she
appears in. Body and tufts are plum. Chest is `bone`. Eye discs are `sun`. Beak
is `terracotta`. Nothing else in the scene may use plum while she is on screen.
A plum owl is not naturalistic and that is the point — Bluey is a blue dog.

**3. Proportion lock.** Two heads tall, where the head is the top third of the
dome. Eyes occupy roughly a third of the total width. Stylised, never realistic.

---

## 4. Face

Almost everything here is a circle. There is very little to drift.

- **Eyes:** two large `sun` discs, touching or nearly touching at the centre.
  Solid `ink` pupils, always centred unless the shot calls for a glance.
- **Brows:** two short `ink` strokes above the discs. These carry the entire
  emotional range — raised for mischief, angled for gravity, level for calm.
- **Beak:** a small downward `terracotta` triangle between the eyes. No mouth.
- **Chest:** a soft `bone` rounded shape, roughly half the body height.
- **Ear tufts:** two blunt plum triangles. Never sharp, never feathered.
- **Feet:** only when perched — two small `sun` shapes, no separated talons.

No individual feathers, ever. Wings are simple rounded shapes when extended.

---

## 5. Signature setting

She sits on an **olive branch**, always the same branch, cropped by the frame edge.
It fixes her in a place, gives every frame a foreground element, and gives an
animator one obvious thing to move.

---

## 6. Permitted poses

Keep the vocabulary small. A short list generates far more consistently.

| Pose | Use |
|---|---|
| Perched, three-quarter, both eyes to camera | Default. The opening line. |
| Perched, head tilted | The hook. Curiosity. |
| Perched, one wing lifted slightly | Mid-tale aside |
| Perched, eyes half-lidded (brows lowered) | Dry humour, the knowing beat |
| Perched, back three-quarter, looking away | Closing shot only |

Front-on and perfectly symmetrical is **not** in the vocabulary — it flattens the
silhouette and reads stiff.

---

## 7. Never

- Never with individual feathers or rendered texture
- Never with separated talons or fingers
- Never flying — she is always perched
- Never inside the tale; she exists only in the frame story
- Never in a `dusk-violet` scene, which would put plum on plum

---

## 8. Prompt block

Paste verbatim. Paraphrasing is how drift starts.

```
A stylised owl rendered as flat vector shapes with no outlines. Body is a
rounded dome in deep plum purple, wider at the base, tapering to two blunt
plum ear tufts. Soft bone-white chest shape covering the lower half. Two very
large golden-yellow circular eyes taking up about a third of the width, with
solid dark round pupils, and two short dark eyebrow strokes above them. Small
downward terracotta triangle beak between the eyes. No mouth, no individual
feathers, no visible legs. Two heads tall, stylised, not realistic. Perched on
an olive branch. Completely flat colour fills, no gradients, no texture, no
shading, no rendering, no outlines. She is the only purple object in the image.
```

Append the scene key fragment and the global negative prompt from
`../prompt-kit.md`.

### Compact block — for models with prompt length limits

Authorised short form. Shorter, not looser: the dropped constraints are the ones
`style: vector_illustration` and the `colors` array already enforce. Never edit
ad hoc.

```
A stylised owl: rounded plum-purple dome body tapering to two blunt ear tufts, bone-white chest, two very large golden circular eyes with dark round pupils, two short dark eyebrow strokes above them, a small terracotta triangle beak, no mouth, no feathers, no visible legs. Two heads tall, stylised. Perched on an olive branch. The only purple object in the image.
```

---

## 9. Voice

Dry, unhurried, faintly amused. Never sing-song, never "children's presenter".
She likes the story and assumes you will too. The register a good grandparent
uses when they are about to tell you something they find funny.

She asks the question at the end and does not answer it.

---

## 10. Reference prompt — preschool-animation idiom

**Purpose:** exploration and reference only. Kouki ships as a drawn vector asset
(`pipeline/build_cast.py::kouki`) because generated characters proved unreliable
— a different bird in every shot, twice in one frame. Use this to explore looks,
brief a human illustrator, or sanity-check the design. Never for production frames.

**Do not name the reference show in the prompt.** Named properties push models
toward derivative output you could not safely publish, and described attributes
steer better anyway. Everything that makes the idiom recognisable is a describable
quality, and they are all listed below.

### Full prompt

```
A stylised owl character for a modern preschool animated television series.
Flat 2D vector illustration with no outlines whatsoever — every shape reads by
colour contrast alone.

Construction: built from simple geometry. A rounded dome body, wider at the
base, tapering to two short blunt ear tufts. A soft off-white chest oval
covering the lower half. Two oversized circular eyes taking up roughly a third
of the head width, each with a small solid dark pupil and one bright catchlight.
Two short dark eyebrow strokes above the eyes carrying the entire expression. A
small downward triangular beak. No mouth, no individual feathers, no visible
legs beyond two small feet. Two heads tall, chunky and rounded, never realistic.

Colour: deep muted purple body (#6B4A78), warm off-white chest (#F7F1E4),
golden-yellow eye discs (#F2B33D), soft dark charcoal pupils and brows
(#23212B), warm terracotta beak (#D0603C). She is the only purple object in
frame.

Shading: flat two-tone only — one base colour plus a single darker flat shadow
shape along one side. Absolutely no gradients, no soft shading, no texture, no
grain, no rendering.

Pose: perched three-quarter on a simple olive-green branch, both eyes to camera,
brows level and calm. Warm, dry, faintly amused — a storyteller, not a mascot.

Clean flat background. Confident negative space. Bright, warm and legible at
small size.
```

### Compact prompt — for models capped near 1000 characters

```
A stylised owl for a preschool animated series. Flat 2D vector, no outlines, shapes read by colour contrast alone. Rounded dome body wider at the base, two short blunt ear tufts, soft off-white chest oval. Two oversized circular eyes about a third of the head width, small dark pupils, one catchlight each, two short dark eyebrow strokes above. Small triangular beak, no mouth, no feathers, no visible legs. Two heads tall, chunky and rounded. Deep muted purple body #6B4A78, off-white chest #F7F1E4, golden eye discs #F2B33D, charcoal pupils and brows #23212B, terracotta beak #D0603C. Flat two-tone shading only — one base colour plus a single darker flat shadow shape. No gradients, no texture, no rendering. Perched three-quarter on an olive branch, eyes to camera, brows level. Warm, dry, faintly amused. Clean flat background.
```

### Negative prompt

```
outlines, line art, black outlines, cross-hatching, sketch, watercolour, oil
painting, brush texture, paper grain, film grain, noise, gradients, soft
shading, cel shading with rim light, ambient occlusion, specular highlights,
depth of field, bokeh, blur, 3D render, CGI, Pixar style, photorealism,
photograph, realistic feathers, detailed plumage, sharp talons, open beak,
angry expression, dark or gothic mood, text, watermark, signature, pure black,
pure white
```

### If the output is wrong

| Symptom | Cause | Fix |
|---|---|---|
| Realistic owl | "stylised" and "preschool" dropped | Restore both; add `detailed plumage` to negatives |
| Outlines appear | Model default | Repeat "no outlines" in the pose sentence too |
| Eyes too small | Not stated as a proportion | Insist on "a third of the head width" |
| Looks menacing | Owls default to nocturnal-predator | Add "brows level", "warm", "friendly", "daylight" |
| Wrong purple | Hexes ignored | Most models ignore hex codes — say "deep muted purple, dusty, not violet" |
| Extra birds | Count not stated | Add "a single owl, one character only" |
