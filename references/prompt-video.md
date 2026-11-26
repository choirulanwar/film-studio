# Frame & video prompts — Gate 6

The most important file in this skill. Output: `epNN/prompt-video.md`.

## Two kinds of prompt — never mix them

| | FRAME prompt (still image) | VIDEO prompt (motion) |
|---|---|---|
| For | start frame, end frame, storyboard still | one video generation |
| Contents | the frozen composition of one frame: framing, static pose, environment, light, locked preset | the eleven blocks below; motion lives only here |
| Banned | camera/subject motion verbs (`panning`, `walking across`, `dolly-in`) | frame descriptions that contradict its reference frame |

**Frame prompt assembly order** (kept from v1 — this is correct):
1. Framing & camera angle
2. Subject + wardrobe + static pose (the character's short block)
3. Environment & practical light (the set block)
4. Locked lens preset
5. Locked color preset (suffix)

**Start/end pairing:** shots with large subject movement (walking, opening a door, turning far, standing up from sitting) require a start + end frame pair with **identical** light, background geometry, and preset — only the subject's pose differs. Static/dialogue shots need only a start frame (or no frame, if the target tool is text-to-video).
If a shot's frame prompt says it repeats another shot's camera/composition, wire that shot's frame as an image input into this frame node — do not only mention it in the prompt text. Text without wiring locks nothing.

**Adapter modes:**
- Tools with frame slots (Flow/Veo I2V, Kling first/last): the frame is attached as a slot, the video prompt stays eleven blocks.
- Reference-only tools (Omni R2V etc.): the frame is used as a reference image; write in the markdown heading which frame is for which shot. Do not claim start/end is "locked" — in this mode it is only a soft reference.
- Spaces: frame = the output of an image node; the video node wires the frame + sheet/plate as inputs. State that wiring in the scene heading, not in the prompt block.
- Asset nodes created at Gate 5 ARE the asset nodes used downstream — never create a second sheet/plate/prop node for the same entity. At Gate 6, wire the existing Gate 5 asset nodes as inputs to frames and motions. Two nodes for one entity is an error, not a backup.
- Before writing scene durations, check the durations the target tool supports (from the brief). If a scene needs a duration outside those options (e.g. Omni only offers 3/5/8/10s), split the scene at a beat into several generations with supported durations — never write a duration the node cannot select. The duration in the node title, in the prompt, and in the node settings must all three be identical.

## File shape

Markdown heading + attachment notes **outside** the block; inside the block only what gets copied into the tool.

````markdown
## Scene 1 · Teras · 20 seconds
Attach: `sari_sheet.png`, `teras_plate.png`
Frame: start `ep01_sc01_start.png` (end: not needed)

```
VIDEO STYLE & FORMAT
...
```
````

Never write a header like `=== PROMPT VIDEO · EP01 ===` **inside** the block — the model can read it as part of the scene / display it as text.

## The eleven blocks, in order (rules first, scene last)

### 1 · VIDEO STYLE & FORMAT
The kind of programme, duration, tempo, acting style, look (from the locked preset), and the mandatory assertion: **one continuous moment covered from many camera positions — NOT a trailer, NOT a montage.** End with a `NOT ...` line for the specific things to avoid (e.g. `NOT sinetron, NO dramatic zooms`; and the genre it is not, if the premise can be misread: `NOT horror, NOT a thriller`). The duration is stated here; **the ratio is never stated** (including the words `vertical`/`horizontal`).

### 2 · LANGUAGE
Six mandatory items:
1. The dialogue language, in capitals (`INDONESIAN (Bahasa Indonesia)`)
2. The register (casual Jakarta, formal, regional — per the brief)
3. `Speak the lines exactly as written: do not translate them, do not paraphrase them, do not invent extra lines.`
4. Numbers are spoken as words in that language
5. `No subtitles, no captions, no on-screen text of any kind burned into the frame.` — the only place the words subtitle/caption may appear in the entire prompt
6. Character names are not spoken unless they are inside dialogue quotation marks

A scene without dialogue still uses this block, in the silent form:
```
LANGUAGE
This scene has NO spoken dialogue — no voices, no narration, no inner monologue, no
whispering. No subtitles, no captions, no on-screen text of any kind burned into the frame.
```
Non-character sounds (notifications, announcements, radio): name the source here, write its line in SHOT BREAKDOWN like dialogue.

### 3 · OPTICS
The scene's base lens + close-up lens + aperture where depth of field matters. Reference: 24mm wide spaces (~74°), 35mm natural (~54°), 50mm neutral (~40°), 85mm face isolation (~24°), 135mm strong compression (~15°). The per-shot lens is written again in SHOT BREAKDOWN. Ban unwanted distortion (`no fisheye, no zoom moves` where applicable).

### 4 · CAMERA
The list of physical positions used + the mandatory sentence: **`Never two consecutive shots from the same position.`** State the rig (dolly, static, breathing handheld) and the eyeline rule if there are looks out of frame. Movement is limited to what is stated here.

### 5 · LIGHTING
Not adjectives. Five mandatory items:
1. **Source** (sun through a window, ceiling fluorescent, a table lamp, a phone screen)
2. **Direction** (camera-left, above, behind)
3. **Colour temperature** (3200K warm / 5600K daylight / etc.)
4. **Contrast & negative fill** (low-key/high-key, the dark side left dark or filled)
5. **One single colour accent**
`dramatic lighting` without a source = no information. It is banned on its own.

### 6 · CRITICAL
The consistency lock. State the **explicit count** of speaking characters + extras. One character only: `ONE character only. Nobody else appears at any point.` Always include: face, hair, clothing exactly from the reference images in every shot; no face swapping/morphing/duplicated faces; accurate lip-sync, only the speaking character's mouth moves. Screen-bearing objects: `screen always angled away from camera, no readable screen`. A functional face mark (if any, from Gate 3) is repeated here, including its side.

### 7 · CHARACTERS
The short form from `cast.md`, **copied**, one line per character with its token. The full physical description is not repeated here.

### 8 · LOCATION
The set block from `set.md` **copied as-is** after a separator, then that scene's properties (plated ones use their token; text-only ones have their block copied in).
**More than one location plate in a single generation** → open with a **reference map**: which plate, which side, which shots it applies to. Its companions must be complete, all three: this map + a location tag on every SHOT + positions in CONTINUITY. One alone is not enough (the character leaks to the wrong side of the door).

### CONTINUITY (optional, between LOCATION and AUDIO)
Used when: >1 location plate, or an object must persist across cuts. One item per character/object: **exactly where it is, from which shot, in which shots it is visible, and in other shots it is only out of frame / behind camera.** Maximum 3 objects. Write it once in simple sentences and stop — an object asserted repeatedly across many blocks is exactly what the model changes.

### 9 · AUDIO
Ambience/room tone, score (or `NO musical score` if it is deliberately silent — deliberate silence is written, not left empty), key sounds per shot, dialogue tempo. The full production cues (OST/TTS/Foley) live in `audio.md` from Gate 7; this block is the summary for the video model.

### 10 · MOVEMENT NOTE
**Always present.**
- 1 character: their body language (`BODY LANGUAGE` in `cast.md`).
- 2 characters: two opposing rhythms, never mirrored.
- >2 people: two main rhythms + **mandatory** splitting of the extras into differing reactions and an explicit ban on synchronised movement (`never a synchronised crowd turn`).

### 11 · SHOT BREAKDOWN
The section heading is exactly `SHOT BREAKDOWN` (not SCREENPLAY/ACTION/SCENE).
Scene line: `SCENE [00:00-00:NN] <LOCATION>` — no scene number; `NN` = the duration from block 1, and the timecode always starts at 00:00.
Shot line anatomy:
```
SHOT <n> (<start>-<end>s), <lens> <SIZE> from <physical position>, <movement>: <action>.
```
- Timecodes run continuously with no gaps/overlaps; the last shot ends exactly at `NN`.
- Dual locations: every shot line gets a **location tag** right after the timecode, on every shot without exception.
- Dialogue: a separate line, name in capitals, the sentence in quotation marks, language per the brief; intonation in parentheses (`SARI (off-screen):`, `SARI (quietly):`).
- A shot without dialogue is written explicitly: `No dialogue — <note on sound/silence>.`
- Closing line: how the clip stops, always on movement — `no freeze frame, no fade to black`.
- **Shots through a gap/glass/from a character's eyes: write only what is visible.** Do not mention the character's name, breath, eyes, words about people, or bans on people (`no face, no head`) in that line — those words plant a face in the frame. The ban on people belongs once, in CRITICAL. The word `POV` is unnecessary; write where the lens sits.
- **Traces/absence of an object are written as a flat surface** (`flat, level with the floor, nothing on it, not an object`), not with contrast words (`darker`, `deeper colour`) — those render as an object.
- Reverse angle: write the camera's position + what is behind the character, once only.

## Banned from prompt blocks

Ratio/resolution/fps/seed/model name · human headers · filenames · episode numbers/series titles · `subtitle`/`caption` outside the LANGUAGE ban · `8k, ultra realistic, masterpiece, award winning` · tool-specific syntax (`--ar`, etc.) · asserting the same object repeatedly across many blocks · asserting an absence with contrast words.

## On handover

One line above the scene list:
> Generate per scene. Attach the files named in the scene heading as references, set the ratio & duration in the tool's settings before generating. Start/end frames (if any) are generated first, from `prompt-aset.md`/this scene's frame prompt.
