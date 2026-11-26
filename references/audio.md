# Audio — Gate 7 (OST, VO, Foley)

A strength of v1, kept and sharpened. Output: `epNN/audio.md`.

## When audio is separate, and when it is not

- The target video tool **generates dialogue inside the clip** (most tools today): dialogue stays in the video prompt (the `LANGUAGE` block + `SHOT BREAKDOWN`). `audio.md` contains only **score & SFX for the edit stage**, not a second dialogue script. Writing dialogue in two places with different words = two versions of the truth.
- The adapter **separates audio** (e.g. a Spaces pipeline: an ElevenLabs TTS node + a silent video node): `audio.md` becomes the source of the VO/dialogue script for the TTS node, copied **verbatim** from `naskah.md`. Delivery tone is marked here, not in the video prompt.

Note which mode is used at the head of `audio.md`.

## 1 · Score / OST (Suno or similar)

Per cue, not per project — one cue per container or per major emotional shift:
- `style tags` (≤200 characters): genre, era, core instrumentation, mood — specific, not "cinematic emotional"
- BPM & dynamics: where it swells, where it drops to silence
- Structure with metatags: `[Intro] [Verse] [Instrumental Swell] [Outro]` following the story's sections/beats
- Bans: vocals if the cue is meant to be instrumental; lyrics, if any, are written separately and checked not to collide with dialogue in the same minute

## 2 · VO / TTS dialogue (separate-audio mode only)

- Text **copied verbatim** from `naskah.md` — do not paraphrase for TTS.
- One delivery tag per line: `[softly]`, `[whispering]`, `[hesitant pause]` — sparingly, at most one tag per line.
- One line = one TTS generation unit; mark the character + the shot number the line comes from, so syncing in the edit requires no guessing.

## 3 · Foley & ambience per shot

A table per shot: `Shot | Ambience bed | Key foley | Deliberately silent`.
Correct entries are specific: `distant train crossing bell`, `raindrops on vinyl umbrella`, `plastic chair leg scraping tile` — not `background sounds`.
Deliberate silence is written explicitly (`— total silence, room tone only`) so the editor does not fill it in.
