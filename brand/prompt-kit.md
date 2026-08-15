# Prompt kit

The machine-facing half of the style bible. Every image the art-director agent
requests is assembled from these blocks, in this order:

```
[STYLE PREAMBLE]  +  [SCENE KEY]  +  [PLANE BRIEF]  +  [SUBJECT]  +  [NEGATIVE]
```

Assemble mechanically. Do not let the agent rewrite the fixed blocks "for
variety" — variety comes from the subject and the scene key, never from the
style preamble. Rewording the preamble is the single most common cause of an
episode that does not match the rest of the catalogue.

---

## 1. Style preamble — fixed, every image

```
Flat vector illustration for a children's animated series. Bold flat colour
fills with no outlines; shapes read purely by colour contrast. Simple geometric
construction from circles and rounded rectangles. Completely flat — no
gradients except a single soft vertical sky gradient, no texture, no grain, no
brush marks, no shading, no rendering, no lighting simulation. Shadows are
hard-edged, cast in one consistent direction, with no blur. Never pure black or
pure white. Composition built as separate flat depth planes. Confident negative
space. Warm, calm, and legible at small size.
```

---

## 1a. Period kits — pick one per episode

**Every episode must declare a period.** Without one the model defaults to
postcard Greece — Byzantine domes, whitewashed Cycladic villages, bell towers —
which is roughly 1,200 years too late for Aesop and wrong for British tales in
every direction. This block is not optional.

**archaic-greek** — Aesop, ~6th century BC
```
Setting is archaic Greece, sixth century BC. Rough stone and mud-brick walls,
timber posts, low shallow-pitched terracotta tile roofs. Olive groves, cypress,
dry stone field walls, threshing floors, clay amphorae, woven baskets. Landscape
first, buildings sparse and low. Absolutely no domes, no whitewashed villages,
no bell towers, no arched windows, no blue shutters, no modern buildings.
```

**greek-village** — later Greek folk tales, 18th–19th century
```
Setting is a Greek village of the nineteenth century. Whitewashed stone walls,
blue shutters and doors, tiled roofs, a small bell tower, stepped lanes, olive
and lemon trees. The postcard Greece — correct here, and only here.
```

**british-rural** — Joseph Jacobs, timeless rural Britain
```
Setting is rural Britain. Dry stone walls, hedgerows, thatched cottages, oak and
hawthorn, muddy lanes, damp overcast light. No Mediterranean architecture, no
terracotta, no cypress.
```

Record the chosen kit in the episode's `shots.json` as `"period"`. Mixing kits
inside one episode is a bug unless the story crosses cultures deliberately.

---

## 1b. Compact blocks — for models with prompt length limits

Recraft V3 caps prompts at 1000 characters. These are the authorised short
forms. They are shorter, **not looser** — every constraint dropped here is one
the model parameter already enforces (`style: vector_illustration` carries "flat
vector, no outlines"; the `colors` array carries the palette).

Use these only when the assembled prompt would exceed the model's budget, and
never edit them ad hoc. If a model needs something shorter still, that model is
wrong for this job.

**Compact style preamble**
```
Flat vector children's illustration. Bold flat colour, no outlines, simple geometric shapes, no texture or gradients, hard-edged shadows, generous negative space.
```

**Compact plane brief**
```
Built as flat overlapping depth planes: flat sky, silhouetted far landscape, readable mid-ground, the subject, and a foreground element cropped by the frame edge.
```

**Compact period kits**
```
archaic-greek: Archaic Greece sixth century BC: rough stone and mud-brick, low terracotta roofs, olive groves, cypress, dry stone walls. No domes, no whitewash, no bell towers.
greek-village: Nineteenth-century Greek village: whitewashed stone, blue shutters, tiled roofs, stepped lanes, olive and lemon trees.
british-rural: Rural Britain: dry stone walls, hedgerows, thatch, oak and hawthorn, muddy lanes, damp overcast light. No Mediterranean architecture.
```

**Compact scene keys**
```
midday-white: Bleached midday Mediterranean light, bone-white ground, golden ochre, deep blue, terracotta, hard blue shadows.
dusk-violet: Evening, deep violet ground, terracotta rooftops, golden lit windows, cool sky, warm interior light.
olive-shade: Cool shade beneath trees, grey-green olive ground, pale seafoam, warm bone highlights, flat light.
storm-grey: Cold damp northern weather, muted blue-grey ground, deep darks, exactly one warm golden point of light.
hearth-amber: Warm lamplit interior, terracotta ground, golden light, bone highlights, deep soft shadows.
sea-deep: Deep night water, dark navy ground, saturated blue, pale seafoam highlights, a few small white stars.
```

---

## 2. Scene key fragments

Pick exactly one per shot. Pull the hex values from `tokens.json` — they are
duplicated here only for prompt convenience, and `tokens.json` wins on any
mismatch.

**midday-white** — bleached Greek noon, high key, heat
```
Bleached midday Mediterranean light. Warm bone-white ground (#F7F1E4) with
golden ochre (#F2B33D), deep saturated blue (#1F5FA8), and terracotta (#D0603C).
Hard blue shadows. High key, sun-flooded, almost overexposed.
```

**dusk-violet** — evening, warm windows, cooling sky
```
Evening settling in. Deep violet ground (#6B4A78) with terracotta rooftops
(#D0603C) and golden lit windows (#F2B33D). Cool sky, warm interior light.
Calm and end-of-day.
```

**olive-shade** — under trees, cool and still
```
Cool shade beneath trees. Grey-green olive ground (#6E8B4A) with pale seafoam
(#79C4C0) and warm bone highlights (#F7F1E4). Flat dappled light, no soft
edges. Quiet and sheltered.
```

**storm-grey** — cold, damp, northern; one warm point only
```
Cold damp northern weather. Muted blue-grey ground (#8B93A0) with deep ink
darks (#23212B). Exactly one warm golden point of light (#F2B33D) in the frame.
Sparse, tense, and still.
```

**hearth-amber** — indoors, lamplit, safe
```
Warm lamplit interior. Terracotta ground (#D0603C) with golden light (#F2B33D)
and bone highlights (#F7F1E4). Deep soft ink shadows. Enclosed, safe, and warm.
```

**sea-deep** — night and deep water
```
Deep night water. Dark navy ground (#123A68) with saturated blue (#1F5FA8) and
pale seafoam highlights (#79C4C0). A few small bone-white stars or lights.
Vast, quiet, full of wonder.
```

---

## 3. Plane brief

Name the planes explicitly. Models compose depth far more reliably when told to.

```
Composed as five flat overlapping depth planes: a flat sky, a silhouetted far
landscape with no interior detail, a mid-ground of readable building and tree
shapes, the subject plane, and a near foreground element cropped by the edge of
the frame.
```

Interiors may drop the far plane, but **never** drop the cropped foreground —
that crop is what makes the parallax read as depth rather than as sliding
cardboard.

---

## 4. Negative prompt — fixed, every image

```
outlines, line art, black outlines, cross-hatching, sketch, watercolour,
gouache, oil painting, brush texture, paper grain, noise, film grain, gradients,
soft shading, cel shading, ambient occlusion, specular highlights, lens flare,
depth of field, bokeh, blur, drop shadow blur, 3D render, CGI, photorealism,
photograph, realistic proportions, detailed faces, nostrils, individual fingers,
text, watermark, signature, pure black, pure white
```

---

## 5. Assembly example

Tortoise and the Hare, shot 07 — the Hare naps under a tree.

```
[STYLE PREAMBLE]

Cool shade beneath trees. Grey-green olive ground (#6E8B4A) with pale seafoam
(#79C4C0) and warm bone highlights (#F7F1E4). Flat dappled light, no soft
edges. Quiet and sheltered.

Composed as five flat overlapping depth planes: a flat sky, a silhouetted far
landscape with no interior detail, a mid-ground of readable building and tree
shapes, the subject plane, and a near foreground element cropped by the edge of
the frame.

A hare asleep on his back beneath a broad olive tree, one ear flopped over his
eyes, built from simple circles and rounded rectangles. Far plane: low hills.
Mid plane: a dry stone wall. Foreground: a cluster of olive branches cropped by
the top-left frame edge. Wide shot, subject off-centre right.

[NEGATIVE]
```

---

## 6. Retry protocol

Do not reroll blindly — it burns budget and rarely converges. Diagnose first.

| Symptom | Cause | Fix |
|---|---|---|
| Outlines appear | Preamble reworded or truncated | Restore preamble verbatim |
| Looks 3D or plasticky | Negative prompt dropped | Re-append negative block |
| Flat, no depth | Plane brief omitted | Add plane brief, insist on the cropped foreground |
| Colours drifting off-key | Scene key paraphrased | Paste key fragment with hex values intact |
| Host looks wrong | Character block paraphrased | Restore from `characters/owl.md` verbatim |
| Host blends into scene | Plum appears elsewhere | Change scene key, or remove the competing plum |
| Face too detailed | Model defaulting to realism | Strengthen negative: `detailed faces, nostrils` |

Three failed attempts on one shot means the **shot** is wrong, not the prompt.
Rewrite the shot description rather than rerolling a fourth time.

---

## 7. Rules for the agent

- Fixed blocks are pasted verbatim. Never paraphrased, never summarised, never
  "improved".
- Exactly one scene key per shot. Never blend two.
- Read hex values from `tokens.json` at assembly time rather than from memory.
- Every episode logs its scene keys per shot to the episode manifest, so a
  finished catalogue can be audited for drift.
- If a shot seems to need a colour outside the core palette, that is a signal to
  escalate to a human, not to invent one.
