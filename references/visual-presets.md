# Visual presets — locked color & lens

Pick exactly **one** color preset + **one** lens preset (the base lens) at Gate 3, lock their `preset_id` in the bible. The preset suffix is copied verbatim into frame prompts; in video prompts, the look is summarised in the `VIDEO STYLE & FORMAT` + `LIGHTING` blocks — do not paste the photo suffix into every block.

v1 only had the Japanese family. v2 keeps it (it is the signature style of this skill's owner's projects) and adds a neutral/regional family so the skill does not lock every project to one look.

## Color presets

### JP family (from v1, kept)
- `jp-melancholic-rainy` — Japanese indie 35mm overcast: desaturated slate-blue & muted teal, lifted milky shadows, low contrast, one selective colour accent. Suffix: `shot on 35mm analog film, Japanese indie cinema aesthetic, melancholic rainy overcast atmosphere, desaturated slate-blue and muted teal color grading, lifted milky shadows, soft rolled-off highlights, low contrast, natural diffused lighting, Fujifilm Superia 400 look, fine film grain`
- `jp-airy-portra-overexposed` — dreamy daylight slice-of-life: high-key +1 stop, Black Pro-Mist bloom, ivory/creamy beige. Suffix: `Japanese airy photography, Kodak Portra 400 overexposed +1 stop, heavy Black Pro-Mist diffusion filter, dreamy soft focus, blooming highlights, creamy ivory and muted beige color palette, warm lifted shadows, ultra-low contrast, translucent Japanese magazine aesthetic, fine analog film grain`
- `jp-cyan-winter-daylight` — cold cerulean + peach skin: `Japanese airy photography, cool cerulean blue and soft peach color grading, Fujifilm Classic Chrome look, lifted blue-tinted shadows, clean bright highlights, low contrast, diffused winter daylight, soft film grain`
- `jp-sun-drenched-portrait` — golden sun + blue shadows: `Japanese sun-drenched portrait photography, Kodak Portra 400 film aesthetic, warm sunlight with cool blue shadows, soft blooming highlights, dreamy Black Pro-Mist diffusion glow, translucent porcelain-peach skin tones, dappled tree shadows, fine analog film grain`
- `jp-blue-hour-cinestill` — teal dusk + warm tungsten: `Japanese blue hour cinema photography, CineStill 800T film aesthetic, deep cool slate-blue shadows contrasting with warm golden tungsten glow, rich cinematic contrast, twilight sky gradient, subtle halation around lights, fine 35mm film grain`

### General family (new in v2)
- `neutral-log-base` — a clean base for manual grading: `natural balanced film photography, Kodak Vision3 250D neutral color profile, accurate skin tones, wide dynamic range, soft natural lighting, minimal color cast, fine 35mm film grain`
- `sea-warm-daylight` — Southeast Asian tropics, hard midday: `warm tropical daylight, honest midday sun, saturated greens and warm skin tones, clear blue-white sky, light haze, natural contrast, fine film grain` — for Indonesian/Malaysian everyday outdoor stories.
- `urban-night-neon-practical` — city night, practical sources: `night city photography lit by practical sources only — shop signs, street lamps, phone screens — deep shadows, mixed colour temperatures kept separate, no global colour wash, fine film grain`
- `noir-lowkey-bw-lean` — low-key leaning to heavy desaturation: `low-key lighting, deep uncorrected shadows, heavily desaturated colour leaning toward monochrome, single hard source per scene, high contrast, fine film grain`

Users may create custom presets: write a new `preset_id` + a one-line suffix in the same format (stock/aesthetic, palette, contrast, light, grain) and lock it in the bible. Never mix two presets in one project.

## Lens presets (base lens)

- `24mm-wide-establishing` — `24mm f/2.8 wide-angle lens, deep depth of field, crisp architectural lines`
- `35mm-prime-natural` — `35mm f/2.0 prime lens, natural environmental perspective, moderate depth of field`
- `50mm-standard-bokeh` — `50mm f/1.4 prime lens, shallow depth of field, creamy background bokeh`
- `85mm-intimate-portrait` — `85mm f/1.4 telephoto portrait lens, compressed background, razor-thin shallow depth of field, dreamy bokeh`
- `anamorphic-cinema` — `40mm T2.0 anamorphic cinema lens, oval bokeh, subtle horizontal lens flare, widescreen cinematic framing`

A lens preset is the **base** lens. The per-shot lens is still determined by SHOT BREAKDOWN (the OPTICS block gives the FOV reference) — the preset does not ban an 85mm close-up in a project whose base lens is 35mm.
