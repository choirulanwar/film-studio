# Cast, set & property bible — Gate 3

This gate decides whether faces, rooms, and objects stay consistent across the whole project or not. The mechanism is not magic: **one text written once, then copied identically everywhere it is used.**

## The verbatim-copy rule (the core of v2)

> Write it once in `cast.md` / `set.md`, then **copy it — do not retype it, do not shorten it, do not paraphrase it.**
> "Rambut cepak hitam" and "rambut pendek hitam" are two different people to the model.
> The Gate 8 checker rejects projects whose copies are not identical.

`bible.json` is a structured copy of the same content (id, token, filename, locked presets) for adapters that need it. If the text bible and `bible.json` differ, **the text bible is correct**.

## Characters — two forms

### Long form (for the sheet prompt, Gate 5)

Mandatory order:
1. Nationality & gender
2. Age & height
3. Skin tone
4. Hair: length, colour, styling
5. Face/jaw shape
6. Build

Then `WARDROBE:` item by item (colour + material + distinguishing detail), then `BODY LANGUAGE:` — one sentence on how they stand/move (reused in `MOVEMENT NOTE`). In the Indonesian worked example below this label appears as `NADA TUBUH:` — same field.

```
[SARI] — bentuk panjang
Indonesian woman, 34 years old, 160 cm, medium brown skin, shoulder-length black hair
tied in a low ponytail, oval face, soft build.
WARDROBE: faded mustard-yellow courier vest over a grey long-sleeve t-shirt, black
cargo trousers, worn white sneakers, a small black waist pouch.
NADA TUBUH: cepat dan hemat gerak, selalu berdiri miring siap berangkat, jarang diam lebih dari dua detik.
```

### No marks on the face

Do not give a character scars, moles, tattoos, piercings, or other small marks as an "anchor". The model always exaggerates them (a 1 cm scar becomes a gash) and the mark changes sides between generations. The face is locked by the **sheet image**; characters are distinguished by age, height, hair, build, glasses, and above all wardrobe.
The single exception: a mark that **has a story function** (planted and paid off in the script). Requirements: written small/faint (`a small, faint ...`), its side stated, and repeated explicitly in the `CRITICAL` block of the video prompt.

### Short form (for the CHARACTERS block of the video prompt)

One line: name, token, age, condensed wardrobe, activity in this scene. The full physical description is **not** repeated — the reference image locks the face; repeating a long description can collide with the image.

```
SARI [gambar_sari] — 34, faded mustard-yellow courier vest over a grey long-sleeve
t-shirt, black cargo trousers, holding a small cardboard package at the gate.
```

The activity part changes per scene; the wardrobe part does not, except for the variants below.

### Wardrobe variants

A character changes clothes in another container: do not overwrite. Add `WARDROBE B (ep 4-6): ...`, make a new sheet, distinguish the token `[gambar_sari_b]`.

## Tokens & filenames (must line up)

| Entity | Token | Filename |
|---|---|---|
| Character Sari | `[gambar_sari]` | `sari_sheet.png` |
| Location Teras | `[gambar_teras]` | `teras_plate.png` |
| Property Motor | `[gambar_motor]` | `motor_plate.png` |

Pattern: `<name>_sheet.png` (characters) / `<name>_plate.png` (sets & properties), where `<name>` is exactly the token after `gambar_`. The user finds files from the token; if they differ, the wrong file gets attached and faces get swapped.

## Sets — one block per location

Must contain:
1. Room type & where it is
2. One large architectural element that determines the composition
3. Main furniture (+ counts where they matter)
4. Floor material (it determines how light reflects)
5. **One odd object** that marks that room
6. **Every door & entry point characters use in the arc** — who enters/exits from where. A door that is not written down will be invented by the model, differently in every clip.

```
[TERAS] [gambar_teras]
Front terrace of a small suburban house in Bekasi. One frosted-glass sliding door
facing a low iron fence and a narrow residential lane. Cracked cream ceramic tile
floor. A single plastic chair and a dry potted plant beside the door. Entry points:
the sliding door (from the living room) and the fence gate (from the lane).
```

## Properties — locked like characters

Objects/vehicles that appear in >1 shot and could change shape between clips.

| Type | When | Form |
|---|---|---|
| With a plate | complex shapes: vehicles, distinctive furniture | text block + token + plate prompt (Gate 5) |
| Text only | small simple objects: a box, a glass, a photo | text block only, copied identically |

For objects that carry writing in the real world (package labels, licence plates, brands): write the ban **inside their block** — `no labels, no printed text, no logos`, `licence plate blank`.

```
[PAKET] — teks saja
small brown cardboard box, roughly shoebox size, wrapped in clear packing tape, no
labels, no printed text, no logos
```

In the video prompt, properties are written in the `LOCATION` block after their location; ones that must persist across cuts move up into `CONTINUITY`.

## Visual lock

At this gate, also lock, from `references/visual-presets.md`:
- exactly **one** `color_preset_id`
- exactly **one** `lens_preset_id` (the base lens; the per-shot lens is still written in SHOT BREAKDOWN)

Write both in `cast.md`/`bible.json`. Presets are not changed mid-project without recording it as a bible revision and rewriting the prompts already made.

## Continuing an old project

Read the existing bible, use it as-is. Add characters/locations below the old ones. Never rewrite an old block — rewriting = a new face.
