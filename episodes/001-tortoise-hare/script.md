# 001 — The Tortoise and the Hare

**Format:** vertical Short, 1080×1920, ~52 seconds, 12 shots
**Purpose:** end-to-end pipeline proof. Can we produce video at a standard worth publishing?
**Source:** Aesop. Original retelling from the motifs — not a translation of any
published text. Public domain reference: Jacobs, *The Fables of Aesop* (1894).

---

## The editorial idea

Everyone knows this fable, which is exactly the problem — it has been told so
often it has stopped meaning anything. The retelling hangs on one detail the
familiar version throws away: **the hare was genuinely faster.** He was right
about that. His mistake was somewhere else entirely, and the closing question
asks the child to find it rather than being told.

No moral is stated. The Owl asks and does not answer.

---

## Narration

Written in English and Greek in parallel, not translated. The Greek is modern and
spoken, pitched at a six-year-old. **Read it aloud before generating anything** —
that is the check no tool can do for you.

| # | Time | EN | GR |
|---|---|---|---|
| 1 | 0:00 | Everyone knows this one. Almost nobody remembers why it's good. | Την ξέρουν όλοι αυτή. Σχεδόν κανείς δεν θυμάται γιατί είναι καλή. |
| 2 | 0:05 | The hare was fast. | Ο λαγός ήταν γρήγορος. |
| 3 | 0:10 | "Nobody here is faster than me." | «Κανείς εδώ δεν τρέχει πιο γρήγορα από μένα.» |
| 4 | 0:13 | The tortoise said: "Let's find out." | Η χελώνα είπε: «Θες να το δούμε;» |
| 5 | 0:17 | Everyone laughed. The tortoise didn't. | Γέλασαν όλοι. Η χελώνα όχι. |
| 6 | 0:20 | And they were off. | Και ξεκίνησαν. |
| 7 | 0:24 | He was so far ahead he couldn't see her any more. | Είχε φύγει τόσο μπροστά που δεν την έβλεπε πια. |
| 8 | 0:28 | "I could sleep and still win." So he did. | «Μπορώ και να κοιμηθώ και πάλι θα κερδίσω.» Και κοιμήθηκε. |
| 9 | 0:33 | She walked past him. She didn't stop to look. | Πέρασε δίπλα του. Δεν σταμάτησε να κοιτάξει. |
| 10 | 0:38 | He woke up. | Ξύπνησε. |
| 11 | 0:42 | She was already there. | Εκείνη ήταν ήδη εκεί. |
| 12 | 0:46 | The hare was faster. He was right about that. So — what did he get wrong? | Ο λαγός ήταν πιο γρήγορος. Σ' αυτό είχε δίκιο. Λοιπόν — σε τι έκανε λάθος; |

**Word counts:** EN ~95, GR ~100. At a slow, unhurried read that is ~48–52s in
both languages, which is what the shot timings assume.

---

## Direction notes

- **Line 5 is the emotional hinge.** "The tortoise didn't" gets a beat of silence
  after it. Do not fill it.
- **Line 9 is the one that must not gloat.** She walks past. No triumph, no
  glance. The restraint is the whole character.
- **Line 12 lands on a question and stops.** No music sting, no bounce. Cut to
  black on the question mark.
- Hold shot 11 two full seconds with no narration before the Owl returns.
- Owl's register: dry, unhurried, faintly amused. Never sing-song.

---

## Shot list

Machine-readable version with assembled prompts: `shots.json`.

| # | Scene key | Shot |
|---|---|---|
| 1 | hearth-amber | Owl perched three-quarter, both eyes to camera |
| 2 | midday-white | Wide village road, hare mid-stride, dust behind |
| 3 | midday-white | Hare close, chest out, chin up |
| 4 | olive-shade | Tortoise low angle, calm, unimpressed |
| 5 | midday-white | Small crowd of animals laughing; tortoise still |
| 6 | midday-white | Start line, hare exploding off, tortoise a step behind |
| 7 | midday-white | Very wide, hare tiny and far, empty road behind |
| 8 | olive-shade | Hare asleep on his back under an olive tree, ear over eyes |
| 9 | olive-shade | Tortoise walking past the sleeping hare, foreground crop |
| 10 | midday-white | Hare upright, eyes wide, mid-scramble |
| 11 | hearth-amber | Tortoise at the finish, small crowd, warm light |
| 12 | hearth-amber | Owl back three-quarter, looking away, olive branch cropped |

---

## Budget

| Stage | Volume | Est. |
|---|---|---|
| Key frames | 12 finals, ~3× retries | $3–6 |
| Motion | ~52s, ~2.5× retries | $7–10 |
| Narration EN + GR | ~200 words total | free tier |
| **Total** | | **$10–16** |

---

## What this test answers

1. Can we hit a visual standard worth publishing?
2. Does the Owl stay on-model across 4 separate generations?
3. Does flat-vector-on-depth-planes survive image-to-video, or does it melt?
4. What is the real retry ratio? Every cost estimate downstream depends on it.
5. How many hands-on hours does one finished minute actually take?

Question 3 is the one to watch. It is the assumption the entire style rests on.
