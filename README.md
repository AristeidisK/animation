# Paramythia

Bilingual Greek–English children's folk tales and fables, produced with an
AI-orchestrated pipeline. Pre-pilot: nothing has been produced yet, and no money
has been committed.

**Working codename.** The channel name is deliberately deferred until after
Gate 1 — see the brief.

---

## What's here

| Path | What it is |
|---|---|
| `paramythia-brief.html` | The feasibility investigation. Economics, YouTube policy constraints, the agent pipeline, three pilots, and the kill criteria. **Read this first.** |
| `brand/style-bible.md` | The base every story inherits — direction, tone, episode architecture, cohesion checklist |
| `brand/tokens.json` | Source of truth for colour, type, scene keys, depth planes |
| `brand/prompt-kit.md` | Exact prompt blocks for image generation, plus retry diagnosis |
| `brand/characters/owl.md` | The host character, specced for drift resistance |

Figma identity file: https://www.figma.com/design/UE7NV9tT3aSLXojGOHFUjC

---

## The one-paragraph version

Flat vector shapes on separate depth planes, Bluey-adjacent in construction but
not in ambition. Every scene keyed to one of six expressive colour moods rather
than naturalistic light. A recurring owl narrator — Athena's bird — bookends every episode
and is the strongest cohesion device in the system. English and Greek ship as two
audio tracks on one video via YouTube's multi-language audio feature, so a single
asset serves both markets.

The economics are hostile — "Made for Kids" content earns roughly $1–3 RPM and
loses comments, memberships and personalised ads — so the project is deliberately
structured to stay cheap enough that it never depends on ad revenue.

---

## Two halves of one style bible

Consistency has to be enforced twice, because Figma and the image models govern
different parts of the screen:

- **Figma** owns what gets composited — title cards, end cards, lower thirds,
  thumbnails, the wordmark. It cannot enforce anything on generated frames.
- **`brand/tokens.json` + `brand/prompt-kit.md`** own what gets generated. The
  art-director agent quotes these verbatim into every image prompt.

Both derive from the same values. Change `tokens.json` first, then mirror it into
Figma — never the other way round.

---

## Status

Pre-pilot. Gate 0 not yet run.

- [x] Feasibility brief
- [x] Style bible, tokens, prompt kit
- [x] Host character spec
- [x] Figma foundations: variables, type styles, Colour and Type pages
- [x] Title Card and Thumbnail components
- [ ] End Card, Lower Third components
- [ ] Owl model sheet (blocked on character art from episode 001)
- [ ] Six licensed music cues
- [ ] Host's name
- [ ] **Gate 0** — bilingual script + narration test, ~$0

---

## Rights

Sources are public domain: Aesop, Joseph Jacobs' *English Fairy Tales* (1890) and
*Celtic Fairy Tales* (1892), and pre-1930 Greek collections. Twentieth-century
Greek folklore collections remain in copyright — the tale is free, a specific
scholar's written version is not. All retellings are written fresh from the
motifs, which is both the safest legal route and what makes the work original
under YouTube's inauthentic-content policy.

Every episode records the public-domain source it derives from.
