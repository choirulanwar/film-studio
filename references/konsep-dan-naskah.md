# Concept & script — Gates 2 and 4

## Gate 2 · Concept

The `konsep.md` output must contain:

1. **Logline** — one sentence: who, what they want, what blocks them, what is at stake.
2. **Premise in 3 lines** — line 3 must contain **one detail that is off** (something that does not fit and makes you curious) and **one character rule** (a habit/prohibition of the character that will produce scenes, not just a trait).
3. **Arc per container** — for a series: one line per episode (starting state → event → cliffhanger). For long-form: per act. For an MV: per song section.
4. **3 alternative hooks with different formulas** — example formulas: (a) an unanswered visual question, (b) an action whose consequence is not yet seen, (c) an arrival/departure that changes the status quo. The user picks one; do not merge all three into one crowded hook.

### Check before presenting (mandatory, silently)

- The hook and arc **do not contradict** the premise (a character who "tidak pernah membuka pintu" must not open the door in the ep.1 arc unless that is the point of the story).
- **No important beat depends on writing that must be read** — a name on a package label, a chat on a phone screen, a name board. AI video cannot render text reliably and our prompts ban on-screen text. Deliver that beat through image, object, or sound.
- The genre it is NOT: if the premise can be misread by the model (an empty house, peeking, a silent elderly person), note in the concept the genre that must later be banned in the `VIDEO STYLE & FORMAT` block (e.g. `NOT horror`).
- Scan for any object/event that has no cause in the premise and is never paid off in the script (a coin from a future year, a sound with no source, an object that appears exactly once). If found, delete it or make it a deliberate part of the premise/arc — never let it slip in.

### Anti-generic (cliché detector)

Reject and rewrite if a concept/script contains any of these without a new twist:

- A character "keeping a big secret" that is never specified in the concept.
- Exposition dialogue: a character says something both characters already know, for the audience's sake.
- Soap-opera dialogue: repeated exclamations, names called in every line, threats spoken instead of done.
- A coincidence that solves the problem (the helper may be a coincidence; the solution may not).
- A "time passes" montage as a substitute for a scene.
- An episode ending that is just a character staring at the camera / eyes widening, with no change of state.

Dialogue test: read it aloud. If a line could be spoken by any character in any story, that line is generic — rewrite it with details belonging to this character (their job, the object in their hand, their address).

## Gate 4 · Script + shot list

Output `epNN/naskah.md` (long-form: `actNN/` may be combined per episode; MV: per section):

1. **Complete dialogue script** — readable as a story without looking at its prompts.
2. **Rundown per shot** — shot number, duration, size/lens, physical camera position, action, dialogue (or an explicit note of no dialogue).
3. **Scene division** — one scene = one video prompt = one generation.

### Scene splitting

- The duration unit follows the target tool in `brief.md`. With no specific tool: **4–30 seconds** per generation.
- Before writing scene durations, check the durations the target tool supports (from the brief). If a scene needs a duration outside those options (e.g. Omni only offers 3/5/8/10s), split the scene at a beat into several generations with supported durations — never write a duration the node cannot select. The duration in the node title, in the prompt, and in the node settings must all three be identical.
- A container/episode longer than that unit is split **at beats** (e.g. 60 seconds → 30+30, or 20+20+20), **never mid-dialogue**, and **a location change is always a new scene**.
- The timecode in every prompt always starts at `00:00` — each generation stands alone.
- Total duration is checked against `brief.md`. Overruns are reported with an offer of which shots to cut; never cut silently.

### Risky shots — flag them, report them, the user decides

| Risk | Why it fails | Alternative offered |
|---|---|---|
| The same place from two sides (door, fence, window) | The character leaks to the wrong side | One side only + sound from the other side; or a reference map + location tags + CONTINUITY (Gate 6) |
| A shot through a gap, glass, window | The model plants a face/object in the gap; glass turns transparent | Write only what is visible; a plate from that gap's own angle |
| A camera angle that does not exist in the plate | The model invents the room's geometry | Make an additional plate from that angle, or move the camera position to the plate's angle |
| An object must persist across cuts | The object disappears/moves/duplicates | A CONTINUITY block (max. 3 objects) |
| A close-up with no face near a dialogue moment | The model adds dialogue lines / a mouth from another character | Move the dialogue to a shot with a face, or mark that shot explicitly as no-dialogue |
| A crowd reacting together | Movement in unison like a choir | The MOVEMENT NOTE splits the reactions (Gate 6) |
| Writing that must be readable | It renders as random letters | Change the beat: the writing is delivered through sound/image |

The list of risky shots is written at the end of `naskah.md` together with the user's decision (kept / replaced).

### Blocking vs set

If the blocking needs a door, window, or room element that is not yet in `set.md`, **add it now** (addition only, never change old blocks) and note it as a revision in `set.md` — before any prompt is written.
