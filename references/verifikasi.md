# Verification & handover — Gate 8

Almost every AI film failure is a **text** error that only becomes visible after credits are burned. This gate catches it before that.

## Step 1 · Machine checker

```
python assets/tools/check_prompts.py <project folder>
```

What this draft version checks: the eleven blocks exist & are in order · mandatory phrases (`NOT a montage`, `Never two consecutive shots from the same position`, the subtitle ban, `exactly as written` or `NO spoken dialogue`, `no freeze frame`) · banned words inside prompt blocks (ratio, `vertical/horizontal`, `===`, filenames, `SCREENPLAY`, resolution/seed/fps, `8k/masterpiece`) · tokens in prompts have an attachment line · SHOT timecodes run continuously and end at the scene duration.
Fix until it passes. Do not hand over a project that has not passed without saying so.

## Step 2 · Checklist the machine cannot check

- [ ] Copies of cast/set/property blocks are **identical letter for letter** in every file (the draft checker does not fully check this yet — read the two furthest-apart files manually: `cast.md` vs the last prompt)
- [ ] No two consecutive shots from the same camera position
- [ ] `MOVEMENT NOTE` matches the number of people; >2 people split the extras
- [ ] No important beat depends on writing that must be read
- [ ] Hook, arc, set, character motivations do not contradict the premise
- [ ] The cliché detector (`konsep-dan-naskah.md`) has been run on the script
- [ ] The genre it is NOT has been stated in `VIDEO STYLE & FORMAT` if the premise can be misread
- [ ] Screen-bearing objects: `screen always angled away from camera` is in CRITICAL
- [ ] No face marks in character blocks, except story-functional ones
- [ ] Gate 4 risky shots have their decisions recorded in `naskah.md`
- [ ] Shots through gaps/glass do not mention characters/words about people
- [ ] An object's absence is written as a flat surface, without contrast words
- [ ] No object is asserted repeatedly across many blocks
- [ ] LIGHTING states source + direction + temperature, not adjectives alone
- [ ] For the Spaces adapter: sheet/plate references are **actually wired** as inputs to the frame/video nodes, not only mentioned in text

## Symptom → cause (for repair)

| Symptom in the generation result | Most likely cause in the text/wiring |
|---|---|
| Face changes between clips | A character block was paraphrased in one file · the wrong sheet attached (token ≠ filename) · reference not wired (Spaces) / not attached (manual) |
| Strange face: gash, boil, oversized mark | A small mark in the character block exaggerated by the model — remove it if it has no story function |
| Strange text / random letters on screen | A human header got copied in · labels/plates/screens not given a text ban · a screen facing the camera |
| Dialogue language/wording off, added, paraphrased | The LANGUAGE block missing / the `exactly as written` phrase deleted |
| Narration/mumbling in a silent scene | LANGUAGE does not use the `NO spoken dialogue` form |
| Extras moving in unison | MOVEMENT NOTE missing / does not ban it explicitly |
| A stranger appears in an empty place | CRITICAL does not lock the number of people |
| The result feels like a montage/trailer | The `ONE continuous ... NOT a montage` assertion missing from block 1 |
| Monotonous cuts | Two consecutive shots from the same position / the different-position rule not written |
| Flat frame | LIGHTING adjectives without source & direction |
| Object disappears/moves/duplicates between cuts | No CONTINUITY item (exact position + shots visible) |
| Character leaks to the wrong side of a door | >1 plate without reference map + location tags + CONTINUITY together |
| A face appears in a gap/glass shot | That shot's line mentions the character/words about people/a ban on people |
| A door asserted `stays closed` gets opened anyway | The assertion stacked across many blocks — reduce it, write it once in CONTINUITY |
| Sheet body panel headless / faces differ between panels | The sheet's Avoid list incomplete (`missing head`, `different faces between panels`) |
| `ERROR unknown` at session start (Spaces) | The LLM called shell/read/filesystem tools, which do not exist in Spaces — everything must live in chat/text nodes; return to the Spaces adapter rule and continue without file tools |

## After the user generates — repair loop

1. **Dissect first, do not guess.** Match the cut points & video content against the prompt's timecodes; transcribe the dialogue if possible. First make sure the version is right: which prompt version, which model, which ratio, which references.
2. **Separate plot holes from deviations.** A different angle but an intact story = not a problem. A door opening in a "the door never opens" story = a problem.
3. **Fix the 1–2 sentences that target the cause** (use the table above). Save as a new version (`prompt-video-v2.md`), do not overwrite the old one.
4. **Test under identical conditions:** same model, ratio, references.
5. **Worse → roll back.** Do not stack fixes.
6. **Survives 2 rounds = the model's limit, not the text's limit.** Offer a different shot (a risky-shot alternative) or a different model.

## Handover shape

A file list + usage order + **known remaining weaknesses** (a scene whose shots are thin, two wardrobes too similar, a risky shot the user kept). Better the user knows before generating.

```markdown
Done, checker passed. The files:
<project file tree>

Usage order:
1. Generate the assets in `prompt-aset.md`, save them with exactly the filenames in their headings.
2. Generate start/end frames (if any), then the video per scene in `prompt-video.md` with the attachments in the scene headings.
3. Set ratio & duration in the tool before generating.
4. Score/SFX from `audio.md` are added in the edit.
```
