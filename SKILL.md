---
name: film-studio
description: "Design live-action AI films end-to-end AND write all of their production prompts: concept, a locked cast/set/prop bible, script, character sheet & location plate prompts, start/end frame prompts, video prompts, and audio cues (OST, VO, SFX). Three formats: serialized vertical micro-drama, long-form film/series, and music video. This skill's core is a DESIGNER + PROMPT WRITER: its main output is text files locked verbatim. Media generation is an optional ADAPTER (Spaces, Flow, Claude Code, or manual by the user) — the core never assumes a shell, a filesystem, or any specific generator tool. Use when the user asks to make an AI film, micro-drama, short movie, series, music video, storyboard, character sheet, or video prompts, or to continue an existing episode/project."
license: MIT
metadata:
  author: Choirul Anwar
  version: "2.1.0"
  updated: "2026-11-26"
  supersedes: "1.x (orchestrator stub)"
---

# Film Studio v2 — AI film designer + production prompt writer

**v2.1.0 · a major change from v1. See `CHANGELOG-DRAFT.md` for the change map and the reasoning behind it.**

**Language:** These instructions are written in English. Always converse with the user in the user's own language. All generated media prompts are written in English regardless of the conversation language.

## Lessons from v1 that produced v2 (do not repeat them)

v1 failed not because its idea was wrong, but because of four things:

1. **Its modules were stubs.** Important rules were a single line, so the LLM improvised — and its improvisation differed on every shot. v2: every gate has a thick reference containing verbatim examples, a list of prohibitions, and known failure modes.
2. **Consistency was stated, not enforced.** v1 had a `bible.json` but no verbatim-copy rule, no token aligned with filenames, and no checker. v2: locked blocks are copied **letter for letter**, the `[gambar_<nama>]` token always aligns with its filename, and the final gate runs a checker.
3. **Defaults were hard-coded.** v1 hard-coded aspect ratio, duration, and clip length per format. v2: **there are no defaults** — ratio, duration, episode/container count, dialogue language, look, and target tool are always asked in the brief.
4. **It assumed a Claude Code runtime.** v1 leaned on file/shell steps (`bible.json` on disk, `read` a module, save the sheet as a file). In other runtimes (Spaces, plain chat) those steps silently vanished and the reference stage was skipped. v2 separates the **CORE** (always runs, text only) from the **ADAPTER** (how that text is executed in a given runtime). See the Adapter section below.

## One engine, three formats

| | MICRO-DRAMA | LONG-FORM | MUSIC VIDEO |
|---|---|---|---|
| Form | vertical episodic series | feature film / multi-episode series | one song, per section |
| Structure | hook ≤3 seconds, cliffhanger every episode | three acts / arc per episode, resolution | song sections: intro, verse, chorus, bridge, outro |
| Bible reused | yes, across episodes | yes, across acts/episodes | yes, across sections |
| Audio | dialogue inside the clip + SFX cues | dialogue + score per scene | the song is the source; visuals follow the lyrics/energy |

The backbone is identical: brief → concept → bible → script → asset prompts → frame/video prompts → audio → verification. Only the script structure and pacing differ (see `workflows/`).

## Adapters — the core does not depend on the runtime

This skill's core **generates nothing and calls no tools**. It produces locked text.

Execution is done by an adapter, chosen from the session context (ask if unclear):

| Adapter | How it executes | What must be preserved |
|---|---|---|
| **Manual** (default) | The user copies prompts into their chosen image/video tool | Filenames in the markdown headings, outside the prompt blocks |
| **Spaces** | Bible text becomes nodes: 1 image node per sheet/plate (reference), 1 image node per start/end frame with **references wired in from the sheet/plate nodes**, 1 video node per scene with frame/references wired in. Never rely on `shell`/`read`/files in Spaces. Character descriptions are NOT paraphrased in node prompts — use the short block + wired references. | References must actually be connected as node inputs, not merely mentioned in prompt text |
| **Claude Code / filesystem** | Project files are written to the project folder; `bible.json` is a structured copy of the same bible text | The bible text is the source of truth; `bible.json` must never diverge from it |
| **Flow / direct Veo** | Start/end frames are used as frame slots; the video prompt is kept separate from the frame prompt | See the frame modes in `references/prompt-video.md` |

**Hard rule — Spaces and plain chat:** In the Spaces adapter and in plain chat: NEVER call shell, read, write, or any filesystem tool — including to read or write bible.json, templates, or project files. There is no filesystem in this runtime; the call will fail. The entire bible, brief, concept, and script live in the chat and in canvas text nodes, never in files. When a skill step names a file, produce its content in chat / a text node using the same filename as the title.

**Valid node inputs in Spaces — never invent handle names:**

| Node type | Valid inputs |
|---|---|
| image-gen | in:image, in:text |
| video-edit (motion node) | in:video, in:image, in:audio, in:text |
| sfx | in:text |
| text | (no inputs — never wire anything into it) |
| llm | in:image, in:video, in:text |

Reference images (sheet/plate/prop/frame) ALWAYS enter via in:image, whatever kind of reference they are. There is no in:reference, in:reference_image, or any other variant. When one handle takes several references, wire them all to the same handle.

If an adapter has no way to attach a reference image, **say so up front** and lower face-consistency expectations — do not pretend a reference was used just because it is mentioned in the text.

## Workflow — eight gates, do not skip any

### 0 · Workspace & continuation detection
- Ask for the project folder / flow / workspace if it is not yet clear. Never hardcode any location.
  If the work location/folder is unclear, ASK — never fill in any default, including a plausible-looking path such as /app/<project-name>/. A value invented at Gate 0 propagates through the whole project. In Spaces there is no project folder: the project IS the flow — never ask for or invent a folder path there.
- New project: copy `assets/template/` as the skeleton.
- Continuation: read the existing bible (`cast.md`, `set.md`, `bible.json`) and **use it as-is**. Do not rewrite it — that is what preserves consistency. New characters/locations are added below the old ones.

### 1 · BRIEF — ask first, never guess
Read `references/brief.md`. Two question cards (maximum 4 per card):
- **Card 1:** topic · format · ratio · dialogue language
- **Card 2:** duration per container · number of containers · look/visual preset · target tool (determines the generation unit & frame mode)

All values start empty — **there are no defaults**. Skip whatever the user's first message already answered. If answers conflict (topic "every night" vs look "bright daylight"), name the conflict; do not silently pick one.
**The number of shots is never asked.** Shots are determined by the script.
**Output:** `brief.md`

### 2 · CONCEPT → request approval
Read `references/konsep-dan-naskah.md` and its anti-cliché section.
**Output:** `konsep.md` — logline, a 3-line premise (including one off-kilter detail and one character rule), an arc per container, **3 alternative hooks with different formulas**.
Check before presenting: the hook & arc do not contradict the premise; no important beat depends on writing that must be read on screen.
**Stop.** The user picks a hook and approves the concept first.

### 3 · BIBLE: CAST, SET & PROPS → request approval
Read `references/cast-set-properti.md`.
**Output:** `cast.md`, `set.md`, and `bible.json` (a structured copy of the same content).
- Characters: one locked block in two forms — **long** (sheet prompt) and **short** (the CHARACTERS block of the video prompt). **No marks on the face** (scars/moles/tattoos) unless the mark serves the story.
- Sets: one block per location, including **every door and entrance** the arc uses, floor material, and one odd object that marks the room.
- Recurring props: locked like characters (plated, or text only).
- Every plated character/set/prop gets a `[gambar_<nama>]` token aligned with its filename.
- Lock exactly **one** color preset and **one** lens preset from `references/visual-presets.md` into the bible.
**Stop.** Changing a character description after prompts are written = rewriting everything.

### 4 · SCRIPT + SHOT LIST → request approval
Read the script section of `references/konsep-dan-naskah.md`.
**Output:** `epNN/naskah.md` (or `actNN/` / MV section) — full dialogue that reads as a story, a per-shot rundown, scene breakdown.
- One scene = one video prompt = one generation. The generation unit length follows the **target tool from the brief** (generally 4–30 seconds; narrow adapters such as Omni at 3–15 seconds split smaller). Never split in the middle of dialogue. A location change = a new scene.
- Check the total duration against `brief.md`. If it runs over, report it and offer what to cut — never cut silently.
- **Risky shots are flagged and reported** (list in `references/konsep-dan-naskah.md`): the same place from two sides, a shot through a gap/glass, an angle that is not in the plate, an object that must survive across cuts, a close-up with no face near dialogue. The user decides.
**Stop.**

### 5 · ASSET PROMPTS
Read `references/prompt-aset.md`.
**Output:** `epNN/prompt-aset.md` — only the **new** assets in that container, plus one "reuse" line for old assets.
Character sheets are always: **close-up on the left, full front body in the centre, full back body on the right, name printed on the image**, neutral grey background, flat studio light. Forbidden: dramatic rim light, heavy grain, bokeh, tool-specific syntax (e.g. `--ar`) inside the prompt — ratio is set in the tool, not in the prompt.

### 6 · FRAME & VIDEO PROMPTS
Read `references/prompt-video.md`. This skill's most important file.
**Output:** `epNN/prompt-video.md`.
- The **frame prompt (still image)** and the **video prompt (motion)** are always separate. Frame: only the frozen composition of that frame, no camera-movement verbs. Video: eleven blocks in order — `VIDEO STYLE & FORMAT, LANGUAGE, OPTICS, CAMERA, LIGHTING, CRITICAL, CHARACTERS, LOCATION, [CONTINUITY], AUDIO, MOVEMENT NOTE, SHOT BREAKDOWN`.
- For shots with large subject movement (walking, opening a door, turning far), create a **start frame + end frame pair** with identical lighting & background geometry.
- Every shot entry names the references to attach/wire in: `Attach: <filename>` in the markdown heading, **outside** the prompt block.
- Asset nodes created at Gate 5 ARE the asset nodes used downstream — never create a second sheet/plate/prop node for the same entity. At Gate 6, wire the existing Gate 5 asset nodes as inputs to frames and motions. If a Gate 5 asset node does not exist yet (e.g. a new session), create it first, then use that same node at Gate 6. Two nodes for one entity is an error, not a backup.

### 7 · AUDIO
Read `references/audio.md`.
**Output:** `epNN/audio.md` — score/OST cues (style tag, BPM, instrumentation, structure), backup VO/dialogue scripts for TTS if the adapter separates audio, and a Foley/ambience list per shot.
Note: if the target video tool generates dialogue inside the clip, audio.md is a complement (score & SFX for the editor), **not** a separate dialogue file replacing the dialogue in the video prompt. Never double it.

### 8 · VERIFICATION & HANDOVER
Read `references/verifikasi.md`.
Run the checker (if Python is available): `python assets/tools/check_prompts.py <project folder>` — it checks verbatim copies, the eleven blocks, tokens vs attachments, durations/timecodes, and forbidden words. Fix until it passes, then the manual checklist, then hand over the file list + how to use it + known remaining weaknesses.
**Repair loop:** if the user returns with a bad generation result, dissect it first, fix **one or two sentences** that target the cause, save as a new version, roll back if it gets worse. A longer prompt does not make a model more obedient.

## Mandatory rules (summary — full version in references)

1. **Cast/set/prop blocks are written identically, letter for letter, wherever they appear.** Never summarize, never paraphrase. One word changes, the face changes.
2. **There are no defaults** for ratio, duration, container count, language, look, or target tool. Everything comes from the brief.
3. **Ratio, resolution, seed, model name, and human headers do NOT go inside prompt blocks.** Those are tool settings / markdown headings outside the block.
4. **Dialogue is embedded in the video prompt** and spoken exactly as written (the `LANGUAGE` block). No subtitles/captions/on-screen text — those words may only appear as a prohibition in `LANGUAGE`.
5. **Important beats never depend on writing that must be read.** Convey them through image or sound.
6. **Characters get no facial marks** as anchors. Faces are locked by the sheet image; distinguish characters by age, hair, build, and wardrobe.
7. **The `MOVEMENT NOTE` is always present.** With >2 people in frame: extras' movement must be broken up and synchronized movement explicitly forbidden.
8. **Lighting is written as source + direction + colour temperature + contrast**, never as adjectives (`dramatic lighting` is forbidden standing alone).
9. **More than one location plate in a single generation** requires three things at once: a reference map at the start of `LOCATION`, a location tag on every SHOT line, and character/object positions in `CONTINUITY`.
10. **Objects that must survive across cuts** are locked in `CONTINUITY`: exactly where, from which shot, visible in which shots, and in other shots only out of frame. Maximum 3 objects; do not re-assert the same object over and over across many blocks.
11. **Shots through gaps/glass/a character's eyes: write only what is visible.** Do not mention the character, breath, eyes, or a no-people prohibition on that shot line — those words plant a face in the frame.
12. **The three approval gates are never skipped:** concept, bible, shot list.
13. **Risky shots are reported, not hidden and not silently replaced.**
14. **Prompts are written generally** (English; dialogue in the user's chosen language), not bound to one tool's syntax.

## Skill structure

| File | Contents |
|---|---|
| `references/brief.md` | gate 1: two cards, anti-guessing, conflicting answers |
| `references/konsep-dan-naskah.md` | gates 2 & 4: per-format structure, hooks, anti-cliché, shot list, risky shots, scene splitting |
| `references/cast-set-properti.md` | gate 3: long/short locked blocks, tokens, sets, props, wardrobe variants |
| `references/prompt-aset.md` | gate 5: 3-panel sheets, set/prop plates, Avoid list |
| `references/prompt-video.md` | gate 6: frame vs video prompts, eleven blocks, CONTINUITY, reference map, start/end pairing |
| `references/audio.md` | gate 7: OST/Suno, VO/TTS, Foley per shot |
| `references/visual-presets.md` | locked color & lens presets (including the JP family from v1, expanded) |
| `references/verifikasi.md` | gate 8: checker, manual checklist, symptom → cause, repair loop |
| `workflows/flow-micro-drama.md` | micro-drama pacing (no locked-in defaults) |
| `workflows/flow-long-form.md` | long-form pacing |
| `workflows/flow-music-video.md` | song section → visual mapping |
| `assets/template/` | empty skeletons for every output file + `bible.json` |
| `assets/contoh/satu-scene/` | one complete scene that passes the checker (a form reference, not a story to copy raw) |
| `assets/tools/check_prompts.py` | gate 8 checker — Python 3, no dependencies |
