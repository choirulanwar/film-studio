# Workflow: Music video & song visualizer

Rasio dan platform tujuan dari `brief.md`. Struktur container = struktur lagu: `Intro, Verse 1, Chorus 1, Verse 2, Chorus 2, Bridge, Outro` (sesuaikan dengan lagu aktual user; jangan mengarang section yang tidak ada).

## Aturan

1. **Lagu adalah sumbernya.** Minta lirik / file / struktur lagu di brief (kartu 2 boleh diganti: durasi lagu · section yang ada · apakah ada performer/tokoh · tool target). Visual dipetakan ke lirik & energi section, bukan sebaliknya.
2. **Pemetaan lirik:** tiap section dapat satu baris pemetaan di `konsep.md`: citra lirik → adegan visual → tokoh/lokasi bible yang dipakai. Citra yang sama di chorus yang berulang memakai **adegan/lokasi yang sama** (pengulangan adalah struktur MV, bukan kesalahan).
3. **Eskalasi chorus:** gerakan kamera & kontras cahaya paling dinamis disimpan untuk Chorus & Bridge; Verse lebih statis/atmosferik. Catat level energi per section (1–3) di naskah supaya prompt videonya konsisten.
4. **Dialog:** MV umumnya tanpa dialog — blok LANGUAGE memakai bentuk `NO spoken dialogue`, kecuali user memang meminta adegan dialog. Nyanyian/lip-sync lagu: sebut di LANGUAGE baris lagu yang dinyanyikan persis, atau larang lip-sync bila performer tidak menyanyi di kamera (keputusan brief).
5. **Loop & dissolve:** bila MV dimaksudkan loop (Shorts/Reels), shot pertama dan terakhir dirancang bisa disambung dissolve: posisi subjek & arah cahaya dicatat di CONTINUITY scene terakhir.
6. **Audio:** gerbang 7 untuk MV berisi pemetaan section→timecode lagu dan cue edit, bukan OST baru — lagunya sudah ada. OST/Suno hanya bila user memang belum punya lagu dan memintanya dibuatkan prompt-nya.
