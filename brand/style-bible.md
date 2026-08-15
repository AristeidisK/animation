# Style bible

The base every story inherits. If a decision isn't in here, it isn't decided —
and if you make it ad hoc during an episode, bring it back here afterwards or
episode 40 will not look like a sibling of episode 1.

| File | Governs |
|---|---|
| `tokens.json` | Colour, type, scene keys, depth planes, formats. **Source of truth.** |
| `prompt-kit.md` | Exact text blocks injected into every image prompt |
| `characters/yiayia.md` | The host — locked spec |
| this file | Direction, tone, episode architecture, the cohesion checklist |
| [Figma file](https://www.figma.com/design/UE7NV9tT3aSLXojGOHFUjC) | Identity, components, title cards, thumbnails — mirrors `tokens.json` |

**Status:** pre-pilot, v0.1. Nothing has been produced against it yet. Expect
Pilot A to change something here — that's what pilots are for.

---

## 1. The direction in one paragraph

Flat vector shapes arranged on separate depth planes. No outlines; shapes read
by colour contrast alone. Characters built from circles and rounded rectangles
with dot eyes, where expression comes from posture and eyebrows rather than
facial detail. Every scene is keyed to a single expressive colour mood rather
than to naturalistic light. Movement is parallax across the planes plus one or
two animated elements per shot, over long confident holds.

**Reference:** Bluey, for identity discipline only. We are not chasing its
animation — that is a funded studio in After Effects and the comparison would
be fatal. What we take is the flat construction, the per-scene colour keys, the
colour-coded cast, and the refusal to soften cultural specificity for export.

**Why flat, beyond taste:** flat shapes have nothing to melt. There is no
rendering to become incoherent, no texture to flicker between frames, and a
limited palette makes errors obvious and cheap to fix. It is the most
drift-resistant style available, and it is also the cheapest to animate
convincingly.

---

## 2. The cultural rule

Bluey is aggressively Brisbane and never apologises for it. That specificity is
why it travels, not a tax on travelling.

So: **be specifically Greek, and specifically British, and never generically
Mediterranean or generically European.** Real cypress, real dry stone walls,
real Queen Anne's lace, a real bríki on a real gas ring. Name the village. The
diaspora parent who recognises it is exactly the viewer worth having, and the
English child who doesn't recognise it still reads a world with conviction in it.

The unifying device is the system, not the setting. Greek and British scenes use
the same construction rules, the same core palette and the same host — they just
pull different scene keys. `midday-white` for a Cycladic square, `storm-grey`
for a Yorkshire moor. Same series, obviously.

---

## 3. Tone and writing

**Dual-audience, Bluey-style.** A parent in the room should be genuinely engaged,
not merely tolerating it.

What that means concretely:

- **Never lecture.** The moral of a fable is delivered as a *question* the host
  asks and does not answer. "Do you think he was right to run so fast?" Bluey
  never once states its theme, and it is the most morally serious children's
  show on television.
- **Emotional honesty over sweetness.** The Hare is genuinely humiliated. Let it
  land for a beat before the warmth arrives.
- **Dry humour aimed slightly over the child's head**, never at the child's
  expense and never winking at the parent. If the joke requires the child not to
  get it, cut it.
- **Small stakes, fully felt.** The scale of a fable is domestic. Play it that way.
- **Real silence.** Hold on a frame with no narration for two seconds. It reads
  as confidence, it costs nothing, and it is the cheapest quality signal
  available to you.
- **No sound effects for their own sake.** No cartoon boings, no whooshes on
  every cut.

**Language.** Written in English and Greek in parallel, never translated after
the fact — a translated script always sounds translated. The Greek is modern and
spoken, aimed at a six-year-old. Public-domain Greek sources are written in an
archaic register that will sound wrong read aloud; the Greek editor's job is to
strip it entirely.

**Length.** 3–5 minutes for Aesop. 5–7 for folk tales. Bluey episodes are seven
minutes and that is not an accident.

**Never set accented Greek in all-caps.** Verified in Figma: Nunito has no
precomposed accented capitals, so `ΆΈΉΊΌΎΏ` render with detached, misaligned
tonos marks. This costs us nothing, because standard Greek orthography drops
accents in all-caps anyway — but it means all-caps Greek must be unaccented, and
any title needing accents must be set in mixed case. Applies to the eyebrow mark,
thumbnails, and title cards.

---

## 4. Episode architecture

A fixed shape is most of what makes a catalogue feel like one thing. Deviate
only with a reason.

| # | Beat | Length | Scene key | Notes |
|---|---|---|---|---|
| 1 | **Cold open** | 10–15s | `hearth-amber` | Host, direct address. A hook, not a greeting. Never "Hello children". |
| 2 | **Title card** | 3s | — | Fixed component. Episode title in both scripts. |
| 3 | **The world** | 20–30s | varies | Establish place before people. One wide shot held long. |
| 4 | **The tale** | 5–7 beats | varies | One scene key per beat. Change key when the emotional temperature changes, not when the location does. |
| 5 | **The turn** | 15–20s | contrast | The pivot. Break the key hard against the preceding beat. |
| 6 | **Settle** | 10–15s | `olive-shade` or `dusk-violet` | Let it land. Minimal or no narration. |
| 7 | **Host closes** | 15–20s | `dusk-violet` | The question. Never the answer. |
| 8 | **End card** | 5s | — | Fixed component. No "smash that subscribe". |

Total: roughly 24–32 shots for a four-minute episode.

**The host bookends every episode.** She is the strongest cohesion device you
have — a viewer arriving at episode 30 knows within four seconds that it belongs
to the same series. She never appears inside the tale.

---

## 5. Sound

- **One music bed per episode**, chosen from a fixed library of six cues so the
  catalogue sounds coherent. Licensed, not generated — see the rights section of
  the brief.
- **Traditional instruments used sparingly and specifically.** A bouzouki on
  every Greek episode is a costume. Once, at the right moment, is a choice.
- **Narration sits forward.** Music sits well under. If you notice the music, it
  is too loud.
- **Room tone, never digital silence**, under held frames.

---

## 6. What we never do

Worth being explicit, because these are the defaults the tooling drifts toward
and the things that make kids' content feel cheap.

- No outlines, no gradients beyond the one sky gradient, no texture
- No pure black or pure white
- No hyperactive cutting — this is not the Cocomelon attention model, and we
  cannot win that fight anyway
- No moral stated aloud
- No "Hello children", no subscribe begging, no end-screen clutter
- No AI-generated music (not Content ID eligible; see the brief)
- No character inconsistency shipped because the deadline is close. Reshoot the
  frame or cut the shot.

---

## 7. Cohesion checklist

Run before publishing any episode. If any answer is no, it is not finished.

- [ ] Host opens and closes, with the plum lock respected in every frame she's in
- [ ] Every shot's scene key is one of the six, logged in the episode manifest
- [ ] No outlines anywhere; no texture anywhere
- [ ] Every exterior shot has a cropped foreground element
- [ ] Title card and end card are the unmodified shared components
- [ ] Type is Nunito throughout, Greek glyphs verified rendering
- [ ] Moral is a question, not a statement
- [ ] At least one held frame of two seconds or more with no narration
- [ ] Both audio tracks present and level-matched
- [ ] Music is one of the six library cues
- [ ] Made-for-Kids flag set; synthetic content disclosed
- [ ] Source note recorded for the public-domain text this derives from

---

## 8. Open decisions

- **Channel name** — deferred until after Gate 1, by your call. Identity is being
  built name-agnostic with a wordmark slot.
- **Host's name** — needed before Pilot A ships.
- **Music library** — six cues to be selected and licensed. Not yet started.
- **Nunito Greek coverage** — verify glyph rendering at subtitle size before
  locking the typeface.
