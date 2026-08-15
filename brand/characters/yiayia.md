# Host character — Yiayiá

**Status:** locked spec, unbuilt. Name TBD.
**Role:** frame narrator. Opens and closes every episode. Never appears inside the tale itself.
**Screen time:** 3–5 shots per episode, roughly 20 seconds. One locked sheet carries the entire catalogue.

---

## Why she is designed this way

Human faces are the least consistent thing an image model produces. Every rule below trades a little charm for a lot of reproducibility. The goal is that a viewer identifies her from silhouette and colour alone, at thumbnail size, before any facial detail resolves — because facial detail is exactly what will drift between episodes.

If a generated frame is ambiguous, the failure is almost always that one of these rules was omitted from the prompt. Check the rules before regenerating.

---

## The three locks

These are non-negotiable and appear in every prompt that includes her.

**1. Silhouette lock.** A rounded triangle. Headscarf at the apex, shawl widening through the shoulders, skirt to the floor. No visible feet, no visible neck. The whole figure is one continuous tapering mass. This silhouette must be identifiable as hers with the fill set to solid black.

**2. Colour lock.** She is the only `plum` (#6B4A78) object in any frame she appears in. Shawl and skirt are plum. Headscarf is `bone`. Apron is `terracotta`. Nothing else in the scene may use plum while she is on screen — not a flower, not a shadow, not a sky. This single rule does more work than every other consistency measure combined.

**3. Proportion lock.** Three and a half heads tall. Stylised, never realistic. Hands are simple rounded mittens with no separated fingers.

---

## Face

Deliberately minimal. There is very little here to drift.

- **Eyes:** two solid `ink` dots. No pupils, no whites, no lashes, no lids.
- **Mouth:** a single curved `ink` line. Three states only — resting soft smile, open oval for speech, flat line for gravity.
- **Cheeks:** two soft `terracotta` circles, always present, always the same size.
- **Nose:** none.
- **Eyebrows:** two short `ink` strokes. These carry the entire emotional range. Raised for wonder, angled for concern, level for calm.
- **Hair:** silver-white, visible only as two small curved shapes at the temples beneath the scarf. Never more.

Expression comes from eyebrows, head tilt and shoulder posture. Not from the face.

---

## Signature object

A small brass **bríki** (Greek coffee pot), `sun` coloured. She is holding it, setting it down, or it sits beside her. It gives every frame a fixed warm accent, and it gives an animator one obvious thing to move.

---

## Permitted poses

Keep the vocabulary small. A short list generates far more consistently than an open brief.

| Pose | Use |
|---|---|
| Seated, three-quarter, hands in lap | Default. Opening line. |
| Seated, leaning forward slightly | The hook. "Listen to this one." |
| Seated, one hand raised, palm open | Mid-tale aside, direct address to camera |
| Seated, holding the bríki | Transitions, the settling beat |
| Standing, back three-quarter, looking off | Closing shot only. Never her face on the last frame. |

Front-on symmetrical framing is **not** in the vocabulary. It flattens her silhouette and reads stiff.

---

## Never

- Never in profile below the shoulder — the triangle collapses
- Never with visible fingers
- Never with a rendered or shaded face
- Never inside the tale being told; she exists only in the frame story
- Never in a scene keyed to `dusk-violet`, which would put her plum against a plum ground

---

## Prompt block

Paste verbatim. Do not paraphrase — paraphrasing is how drift starts.

```
An elderly Greek grandmother rendered as flat vector shapes with no outlines.
Silhouette is a rounded triangle: bone-white headscarf at the top, widening
plum shawl and long plum skirt to the floor, no feet, no neck. Terracotta
apron. Three and a half heads tall, stylised, hands are simple rounded mittens
with no separate fingers. Face has only two solid dark dots for eyes, two short
dark eyebrow strokes, one curved line mouth, and two soft terracotta circle
cheeks. No nose. Silver-white hair visible only as two small curves at the
temples. She holds a small brass coffee pot in warm gold. Completely flat
colour fills, no gradients, no texture, no shading, no rendering, no outlines.
She is the only purple object in the image.
```

Append the scene key fragment and the global negative prompt from `../prompt-kit.md`.

---

## Open

- **Her name.** Wanted a real one, not "Yiayiá" as a proper noun. Something that a Greek parent hears as warm rather than generic, and that an English child can say. Suggestions on request.
- **Whether pappoú ever appears.** Currently no. Adding him doubles the consistency burden for one more voice, and the fourth wall works fine with a single narrator.
