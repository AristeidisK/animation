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
