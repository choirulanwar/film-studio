# Audio — gerbang 7 (OST, VO, Foley)

Kelebihan v1 yang dipertahankan dan dipertajam. Output: `epNN/audio.md`.

## Kapan audio terpisah, kapan tidak

- Tool video target **menggenerate dialog di dalam klip** (mayoritas tool sekarang): dialog tetap di prompt video (blok LANGUAGE + SHOT BREAKDOWN). `audio.md` hanya berisi **skor & SFX untuk tahap edit**, bukan naskah dialog kedua. Menulis dialog di dua tempat dengan kata berbeda = dua versi kebenaran.
- Adapter **memisahkan audio** (mis. pipeline Spaces: node TTS ElevenLabs + node video tanpa suara): `audio.md` menjadi sumber naskah VO/dialogue untuk node TTS, disalin **verbatim** dari `naskah.md`. Nada pengucapan ditandai di sini, bukan di prompt video.

Catat mode yang dipakai di kepala `audio.md`.

## 1 · Skor / OST (Suno atau sejenisnya)

Per cue, bukan per proyek — satu cue per container atau per perubahan emosi besar:
- `style tags` (≤200 karakter): genre, era, instrumentasi inti, mood — spesifik, bukan "cinematic emotional"
- BPM & dinamika: di mana swell, di mana drop ke hening
- Struktur dengan metatag: `[Intro] [Verse] [Instrumental Swell] [Outro]` mengikuti section/beat cerita
- Larangan: vokal bila cue dimaksudkan instrumental; lirik bila ada ditulis terpisah dan dicek tidak bertabrakan dengan dialog di menit yang sama

## 2 · VO / dialogue TTS (hanya mode audio terpisah)

- Teks **disalin verbatim** dari `naskah.md` — jangan parafrase untuk TTS.
- Tag penyampaian per baris: `[softly]`, `[whispering]`, `[hesitant pause]` — hemat, satu tag per baris maksimal.
- Satu baris = satu unit generate TTS; tandai tokoh + nomor shot asal baris itu supaya sinkronisasi di edit tidak menebak.

## 3 · Foley & ambience per shot

Tabel per shot: `Shot | Ambience bed | Foley kunci | Yang sengaja hening`.
Contoh isian yang benar spesifik: `distant train crossing bell`, `raindrops on vinyl umbrella`, `plastic chair leg scraping tile` — bukan `background sounds`.
Hening yang disengaja ditulis eksplisit (`— hening total, room tone saja`) supaya editor tidak mengisinya.
