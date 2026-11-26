# Visual presets — color & lens terkunci

Pilih tepat **satu** color preset + **satu** lens preset (lensa dasar) di gerbang 3, kunci `preset_id`-nya di bible. Suffix preset disalin verbatim ke prompt frame; di prompt video, look diringkas di blok `VIDEO STYLE & FORMAT` + `LIGHTING` — jangan menempel suffix foto ke semua blok.

v1 hanya punya keluarga Japanese. v2 mempertahankannya (itu gaya khas proyek pemilik skill) dan menambah keluarga netral/regional supaya skill tidak mengunci semua proyek ke satu look.

## Color presets

### Keluarga JP (dari v1, dipertahankan)
- `jp-melancholic-rainy` — Japanese indie 35mm overcast: desaturated slate-blue & muted teal, lifted milky shadows, low contrast, satu aksen warna selektif. Suffix: `shot on 35mm analog film, Japanese indie cinema aesthetic, melancholic rainy overcast atmosphere, desaturated slate-blue and muted teal color grading, lifted milky shadows, soft rolled-off highlights, low contrast, natural diffused lighting, Fujifilm Superia 400 look, fine film grain`
- `jp-airy-portra-overexposed` — dreamy daylight slice-of-life: high-key +1 stop, Black Pro-Mist bloom, ivory/beige krem. Suffix: `Japanese airy photography, Kodak Portra 400 overexposed +1 stop, heavy Black Pro-Mist diffusion filter, dreamy soft focus, blooming highlights, creamy ivory and muted beige color palette, warm lifted shadows, ultra-low contrast, translucent Japanese magazine aesthetic, fine analog film grain`
- `jp-cyan-winter-daylight` — cerulean dingin + kulit peach: `Japanese airy photography, cool cerulean blue and soft peach color grading, Fujifilm Classic Chrome look, lifted blue-tinted shadows, clean bright highlights, low contrast, diffused winter daylight, soft film grain`
- `jp-sun-drenched-portrait` — matahari emas + bayangan biru: `Japanese sun-drenched portrait photography, Kodak Portra 400 film aesthetic, warm sunlight with cool blue shadows, soft blooming highlights, dreamy Black Pro-Mist diffusion glow, translucent porcelain-peach skin tones, dappled tree shadows, fine analog film grain`
- `jp-blue-hour-cinestill` — senja teal + tungsten hangat: `Japanese blue hour cinema photography, CineStill 800T film aesthetic, deep cool slate-blue shadows contrasting with warm golden tungsten glow, rich cinematic contrast, twilight sky gradient, subtle halation around lights, fine 35mm film grain`

### Keluarga umum (baru di v2)
- `neutral-log-base` — basis bersih untuk grading manual: `natural balanced film photography, Kodak Vision3 250D neutral color profile, accurate skin tones, wide dynamic range, soft natural lighting, minimal color cast, fine 35mm film grain`
- `sea-warm-daylight` — tropis Asia Tenggara, siang keras: `warm tropical daylight, honest midday sun, saturated greens and warm skin tones, clear blue-white sky, light haze, natural contrast, fine film grain` — untuk cerita keseharian Indonesia/Malaysia di luar ruangan.
- `urban-night-neon-practical` — malam kota, sumber praktis: `night city photography lit by practical sources only — shop signs, street lamps, phone screens — deep shadows, mixed colour temperatures kept separate, no global colour wash, fine film grain`
- `noir-lowkey-bw-lean` — low-key condong desaturasi berat: `low-key lighting, deep uncorrected shadows, heavily desaturated colour leaning toward monochrome, single hard source per scene, high contrast, fine film grain`

Preset kustom boleh dibuat user: tulis `preset_id` baru + suffix satu baris dengan format sama (stock/estetika, palet, kontras, cahaya, grain) dan kunci di bible. Jangan mencampur dua preset dalam satu proyek.

## Lens presets (lensa dasar)

- `24mm-wide-establishing` — `24mm f/2.8 wide-angle lens, deep depth of field, crisp architectural lines`
- `35mm-prime-natural` — `35mm f/2.0 prime lens, natural environmental perspective, moderate depth of field`
- `50mm-standard-bokeh` — `50mm f/1.4 prime lens, shallow depth of field, creamy background bokeh`
- `85mm-intimate-portrait` — `85mm f/1.4 telephoto portrait lens, compressed background, razor-thin shallow depth of field, dreamy bokeh`
- `anamorphic-cinema` — `40mm T2.0 anamorphic cinema lens, oval bokeh, subtle horizontal lens flare, widescreen cinematic framing`

Lens preset adalah lensa **dasar**. Lensa per shot tetap ditentukan SHOT BREAKDOWN (blok OPTICS memberi acuan FOV) — preset tidak melarang close-up 85mm di proyek berlensa dasar 35mm.
