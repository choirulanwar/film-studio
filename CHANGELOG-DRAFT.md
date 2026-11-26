# film-studio v2 — peta perubahan dari v1 (draft 2026-11-26)

Status: **DRAFT — dipush ke github.com/choirulanwar/film-studio pada 2026-11-26 untuk dites dari Spaces.** Belum dinyatakan rilis final: menunggu tes live end-to-end pertama (lihat "Yang belum ada di draft ini").

## Kenapa v1 hasilnya jelek (ringkasan review)

1. Modul stub (35 baris SKILL.md, modul 9–15 baris) → LLM improvisasi, beda tiap shot.
2. Konsistensi dinyatakan (`bible.json`) tapi tidak dipaksa: tidak ada aturan verbatim, token↔nama berkas, atau checker.
3. Default dipatok: rasio, durasi, panjang klip per format.
4. Mengasumsikan runtime Claude Code (file/shell/`bible.json` di disk) → di Spaces tahap referensi diam-diam hilang.
5. Tidak ada contoh, template, verifikasi, atau repair loop.

## Yang berubah di v2

| Area | v1 | v2 |
|---|---|---|
| Arsitektur | Orchestrator yang mengasumsikan bisa mengeksekusi | **Inti** (perancang + penulis prompt, teks saja) + **Adapter** (Manual / Spaces / Claude Code / Flow) — inti tidak mengasumsikan tool apa pun |
| Gerbang | 2 fase, 1 approval | 8 gerbang, 3 approval (konsep, bible, shot list) |
| Brief | tidak ada | Gerbang 1: dua kartu, **tanpa default**, tool target wajib, bentrok jawaban disebutkan |
| Tokoh/Set | Entitas di `bible.json` saja | Blok terkunci **panjang + pendek**, **salin verbatim**, token `[gambar_x]` sejalan nama berkas, tanpa tanda wajah, wardrobe varian, set wajib memuat semua pintu + benda ganjil, properti dikunci |
| Prompt video | Tabel storyboard (start frame + motion) | **Sebelas blok** (STYLE, LANGUAGE, OPTICS, CAMERA, LIGHTING, CRITICAL, CHARACTERS, LOCATION, [CONTINUITY], AUDIO, MOVEMENT NOTE, SHOT BREAKDOWN) + prompt frame terpisah + start/end pairing dipertahankan dari v1 |
| Anti-gagal | tidak ada | Shot berisiko ditandai di gerbang 4 · peta referensi + tag lokasi + CONTINUITY untuk lokasi ganda · aturan shot celah/kaca · larangan menumpuk penegasan · kata terlarang di prompt |
| Audio | Modul 3 bullet | Reference penuh: mode dialog-di-klip vs audio-terpisah (jangan dobel), OST per cue, VO verbatim, Foley per shot |
| Visual preset | 6 preset, semua Japanese, lens 5 one-liner | Keluarga JP dipertahankan + `neutral-log-base`, `sea-warm-daylight`, `urban-night-neon-practical`, `noir-lowkey-bw-lean`; lens preset + acuan FOV per shot |
| Contoh & template | tidak ada | Template kosong semua berkas + `bible.json`; contoh satu scene lengkap yang lolos checker |
| Verifikasi | tidak ada | Checker Python (blok, frasa wajib, kata terlarang, token↔lampiran, timecode) + checklist manual + tabel gejala→penyebab + repair loop 1–2 kalimat, versi baru, rollback |
| Workflows | Angka dipatok per format | Pacing relatif; semua angka dari brief |

## Yang SENGAJA dipertahankan dari v1

- Ide **project bible** sebagai sumber kebenaran tunggal (sekarang: bible teks + `bible.json` sebagai salinan terstrukturnya).
- **Pemisahan prompt frame diam vs prompt video gerak**, dan urutan rakit prompt frame.
- **Start/end frame pairing** untuk shot bergerak besar.
- **Audio sebagai gerbang sendiri** (OST/VO/Foley) — kelebihan v1 atas skill pembanding.
- **Music video** sebagai format pertama, bukan tempelan.
- Keluarga **color preset JP** (gaya khas pemilik skill) — sekarang jadi satu keluarga di antara beberapa.

## Yang belum ada di draft ini (jujur)

- Checker **belum** memeriksa kesamaan verbatim blok cast/set antar berkas secara penuh (baru token↔lampiran, blok, frasa, kata terlarang, timecode). Itu peningkatan checker berikutnya.
- Contoh baru **satu scene** (20 detik, 1 tokoh, 1 lokasi). Contoh multi-episode & lokasi ganda belum dibuat — pola lokasi ganda sudah ditulis aturannya, belum dibuktikan di contoh.
- Belum dites live di Spaces maupun Claude Code. Tes pertama yang disarankan: jalankan contoh "Paket Terakhir" sebagai proyek baru, lalu satu proyek asli Hero, dan catat kegagalan barunya ke tabel gejala→penyebab.
- `LICENSE` & manifest plugin (`.claude-plugin/`) belum disertakan di draft.
