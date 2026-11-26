# Asset prompts — Gate 5

Output `epNN/prompt-aset.md`: only **new** assets in that container. Old assets get a single line at the head of the file:

```
Reuse: sari_sheet.png, teras_plate.png (from ep01)
```

Each asset's heading = the filename of its generation result. The filename is written in the markdown heading, **not** inside the prompt block.

## Character sheets — always 3 panels + name

Standard composition (do not vary it between characters — layout consistency helps the user & the model):

- **Left:** close-up of the face
- **Centre:** full body from the front
- **Right:** full body from the back
- **The character's name printed in the image** (the only text deliberately requested, so sheets do not get mixed up when attached)
- Plain neutral grey background, flat even studio lighting, neutral standing pose

Template (fill from the long form in `cast.md`, **copied**, not rewritten):

```
Character reference sheet of <BENTUK PANJANG>, three panels on a plain neutral
light-grey studio background, flat even studio lighting: LEFT panel close-up of the
face, CENTRE panel full body from the front, RIGHT panel full body from the back.
The name "<NAMA>" printed in plain capital letters at the top of the sheet.
Avoid: dramatic lighting, rim light, film grain, blur, bokeh, missing head, cropped
feet, different faces between panels, extra people, text other than the name.
```

Bans kept from v1 (correct, do not drop them): dramatic rim light, heavy grain, mist, shallow bokeh **in the sheet** — all of these shift facial geometry & outfit detail. A sheet is an identity document, not a film still.
Also banned: tool-specific syntax (`--ar`, model parameters, etc.) inside the prompt. The sheet's ratio is set in the image tool.

## Set plates

One empty image per location, from **the most important wide shot angle** in that scene — many models copy the plate's composition, so the plate angle = the most frequently used angle.

```
Empty location reference plate of <SET BLOCK from set.md, copied verbatim>, eye-level wide
framing from <the most important wide shot angle>, <the location's base lighting>.
Avoid: absolutely no people, no characters, no faces, no text, no logos, no vehicles
unless specified in the set block.
```

The phrase `absolutely no people` is mandatory — a plate containing a person will plant that person into every shot.

## Property plates (plated ones only)

```
Reference plate of <PROP BLOCK from set.md, copied verbatim>, on a plain neutral
background, three-quarter view, flat even lighting, nothing else in frame.
Avoid: people, hands, text, labels, logos (unless that prohibition is already in its block — do not duplicate it in different words).
```

## Handover order

At the end of the file, one line of instruction for the user/adapter:

> Generate all assets in this file first, save them with exactly the filenames in their headings, then generate frames/video. A sheet/plate that has not been generated yet = do not start Gate 6 for shots that use it.
