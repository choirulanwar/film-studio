# film-studio v2 — change map from v1 (draft 2026-11-26)

Status: **v2.1 — pushed to github.com/choirulanwar/film-studio on 2026-11-26 for testing from Spaces. Not declared a final release:** a real end-to-end generation test is still pending (see "What is not in this draft yet").

## v2.1 — 2026-11-26

Changes from the first live test (an LLM-node discussion in Spaces, 2026-11-26 — the gates were followed in order and the LLM created 30 nodes itself):

1. Instruction layer converted to English (user dialogue follows the user's language; media prompts remain English).
2. Spaces adapter: explicit ban on shell/read/filesystem tools.
3. Valid node handle table added.
4. Gate 6 must reuse Gate 5 asset nodes — duplicates are an error.
5. Scene durations must match the target tool's supported durations (split at beats); title/prompt/node setting must agree.
6. A frame that repeats another shot's camera must be wired from that frame.
7. Gate 0: never invent a default folder.
8. Concept/script check: scan for uncaused, unpaid-off fantasy elements.

## Why v1's output was bad (review summary)

1. Stub modules (35-line SKILL.md, 9–15-line modules) → the LLM improvised, differently on every shot.
2. Consistency was declared (`bible.json`) but not enforced: no verbatim rule, no token↔filename alignment, no checker.
3. Hard-coded defaults: ratio, duration, clip length per format.
4. It assumed a Claude Code runtime (files/shell/`bible.json` on disk) → in Spaces the reference stage silently vanished.
5. No examples, templates, verification, or repair loop.

## What changed in v2

| Area | v1 | v2 |
|---|---|---|
| Architecture | An orchestrator that assumed it could execute | **Core** (designer + prompt writer, text only) + **Adapters** (Manual / Spaces / Claude Code / Flow) — the core assumes no tools |
| Gates | 2 phases, 1 approval | 8 gates, 3 approvals (concept, bible, shot list) |
| Brief | none | Gate 1: two cards, **no defaults**, target tool mandatory, conflicting answers named |
| Characters/Sets | Entities in `bible.json` only | Locked blocks in **long + short** forms, **copied verbatim**, `[gambar_x]` tokens aligned with filenames, no facial marks, wardrobe variants, sets must include every door + one odd object, props locked |
| Video prompts | Storyboard table (start frame + motion) | **Eleven blocks** (STYLE, LANGUAGE, OPTICS, CAMERA, LIGHTING, CRITICAL, CHARACTERS, LOCATION, [CONTINUITY], AUDIO, MOVEMENT NOTE, SHOT BREAKDOWN) + separate frame prompts + start/end pairing kept from v1 |
| Failure prevention | none | Risky shots flagged at gate 4 · reference map + location tags + CONTINUITY for multiple locations · gap/glass shot rule · ban on piling up assertions · forbidden words in prompts |
| Audio | A 3-bullet module | Full reference: in-clip dialogue vs separate-audio modes (never doubled), OST per cue, verbatim VO, Foley per shot |
| Visual presets | 6 presets, all Japanese; lenses as 5 one-liners | JP family kept + `neutral-log-base`, `sea-warm-daylight`, `urban-night-neon-practical`, `noir-lowkey-bw-lean`; lens presets + per-shot FOV reference |
| Examples & templates | none | Empty templates for every file + `bible.json`; one complete example scene that passes the checker |
| Verification | none | Python checker (blocks, required phrases, forbidden words, token↔attachment, timecodes) + manual checklist + symptom→cause table + repair loop of 1–2 sentences, new version, rollback |
| Workflows | Fixed numbers per format | Relative pacing; all numbers come from the brief |

## Deliberately kept from v1

- The **project bible** idea as the single source of truth (now: bible text + `bible.json` as its structured copy).
- The **separation of still frame prompts vs motion video prompts**, and the frame-prompt assembly order.
- **Start/end frame pairing** for shots with large movement.
- **Audio as its own gate** (OST/VO/Foley) — v1's advantage over the comparison skill.
- **Music video** as a first-class format, not an add-on.
- The **JP color preset family** (the skill owner's signature style) — now one family among several.

## What is not in this draft yet (honest list)

- The checker does **not yet** fully verify verbatim equality of cast/set blocks across files (so far: token↔attachment, blocks, phrases, forbidden words, timecodes). That is the checker's next upgrade.
- The example is still **one scene** (20 seconds, 1 character, 1 location). A multi-episode & multi-location example has not been made — the multi-location pattern is written as rules but not yet proven in an example.
- Live-tested in Spaces via an LLM-node discussion on 2026-11-26: the gates were followed in order and the LLM created the project's 30 nodes itself. A real generation test (image/video output quality) is still pending, and it has not yet been tested in Claude Code. Suggested next tests: run the "Paket Terakhir" example as a new project, then one of Hero's real projects, and log new failures into the symptom→cause table.
- `LICENSE` & a plugin manifest (`.claude-plugin/`) are not yet included in this draft.
