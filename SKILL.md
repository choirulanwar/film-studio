---
name: film-studio
description: "Merancang film AI live-action end-to-end DAN menulis semua prompt produksinya: konsep, cast/set/properti bible terkunci, naskah, prompt sheet karakter & plate lokasi, prompt frame awal/akhir, prompt video, dan cue audio (OST, VO, SFX). Tiga format: micro-drama vertikal berseri, film/seri long-form, dan music video. Inti skill ini adalah PERANCANG + PENULIS PROMPT: keluaran utamanya berkas teks yang terkunci verbatim. Generate media adalah ADAPTER opsional (Spaces, Flow, Claude Code, atau manual oleh user) — inti tidak pernah mengasumsikan ada shell, filesystem, atau tool generator tertentu. Gunakan saat user minta bikin film AI, micro-drama, short movie, seri, music video, storyboard, sheet karakter, prompt video, atau melanjutkan episode/proyek yang sudah ada."
license: MIT
metadata:
  author: Choirul Anwar
  version: "2.0.0-draft"
  updated: "2026-11-26"
  supersedes: "1.x (orchestrator stub)"
---

# Film Studio v2 — perancang film AI + penulis prompt produksi

**v2.0.0-draft · perubahan besar dari v1. Lihat `CHANGELOG-DRAFT.md` untuk peta perubahan dan alasannya.**

## Pelajaran v1 yang melahirkan v2 (jangan diulangi)

v1 gagal bukan karena idenya salah, tapi karena empat hal:

1. **Modulnya stub.** Aturan penting cuma satu baris, jadi LLM improvisasi — dan improvisasinya beda tiap shot. v2: setiap gerbang punya reference tebal berisi contoh verbatim, daftar larangan, dan mode kegagalan yang sudah diketahui.
2. **Konsistensi cuma dinyatakan, tidak dipaksa.** v1 punya `bible.json` tapi tidak ada aturan salin verbatim, tidak ada token yang sejalan dengan nama berkas, tidak ada checker. v2: blok terkunci disalin **huruf per huruf**, token `[gambar_<nama>]` selalu sejalan dengan nama berkasnya, dan gerbang terakhir menjalankan checker.
3. **Default dipatok.** v1 menghardcode rasio, durasi, dan panjang klip per format. v2: **tidak ada default** — rasio, durasi, jumlah episode/container, bahasa dialog, look, dan tool target selalu ditanyakan di brief.
4. **Mengasumsikan runtime Claude Code.** v1 bertumpu pada langkah file/shell (`bible.json` di disk, `read` module, simpan sheet sebagai file). Di runtime lain (Spaces, chat biasa) langkah itu diam-diam hilang dan tahap referensi diskip. v2 memisahkan **INTI** (selalu jalan, cuma teks) dari **ADAPTER** (cara teks itu dieksekusi di runtime tertentu). Lihat bagian Adapter di bawah.

## Satu mesin, tiga format

| | MICRO-DRAMA | LONG-FORM | MUSIC VIDEO |
|---|---|---|---|
| Bentuk | seri vertikal berepisode | film fitur / seri multi-episode | satu lagu, per section |
| Struktur | hook ≤3 detik, cliffhanger tiap episode | tiga babak / arc per episode, resolusi | section lagu: intro, verse, chorus, bridge, outro |
| Bible dipakai ulang | ya, lintas episode | ya, lintas act/episode | ya, lintas section |
| Audio | dialog di dalam klip + cue SFX | dialog + skor per scene | lagu adalah sumbernya; visual mengikuti lirik/energi |

Tulang belakangnya identik: brief → konsep → bible → naskah → prompt aset → prompt frame/video → audio → verifikasi. Yang berbeda hanya struktur naskah dan pacing (lihat `workflows/`).

## Adapter — inti tidak bergantung pada runtime

Inti skill ini **tidak menggenerate apa pun dan tidak memanggil tool apa pun**. Ia menghasilkan teks terkunci.

Eksekusi dilakukan adapter, dipilih dari konteks sesi (tanyakan kalau tidak jelas):

| Adapter | Cara eksekusi | Yang wajib dijaga |
|---|---|---|
| **Manual** (default) | User copy prompt ke tool gambar/video pilihannya | Nama berkas di judul markdown, di luar blok prompt |
| **Spaces** | Teks bible menjadi node: 1 node image per sheet/plate (referensi), 1 node image per start/end frame dengan **referensi ter-wire dari node sheet/plate**, 1 node video per scene dengan frame/referensi ter-wire. Jangan pernah mengandalkan `shell`/`read`/file di Spaces. Deskripsi tokoh TIDAK diparafrase di prompt node — pakai blok pendek + referensi ter-wire. | Referensi harus benar-benar terhubung sebagai input node, bukan cuma disebut di teks prompt |
| **Claude Code / filesystem** | Berkas proyek ditulis ke folder proyek; `bible.json` adalah salinan terstruktur dari bible teks yang sama | Bible teks adalah sumber kebenaran; `bible.json` jangan sampai beda isi |
| **Flow / Veo langsung** | Start/end frame dipakai sebagai frame slot; video prompt dipisah dari prompt frame | Lihat `references/prompt-video.md` bagian mode frame |

Kalau adapter tidak punya cara menempelkan gambar referensi, **katakan itu di awal** dan turunkan ekspektasi konsistensi wajah — jangan berpura-pura referensi terpakai hanya karena disebut di teks.

## Alur kerja — delapan gerbang, jangan dilompati

### 0 · Tempat kerja & deteksi lanjutan
- Tanyakan folder proyek / flow / ruang kerja kalau belum jelas. Jangan hardcode lokasi mana pun.
- Proyek baru: salin `assets/template/` sebagai kerangka.
- Lanjutan: baca bible yang sudah ada (`cast.md`, `set.md`, `bible.json`) lalu **pakai apa adanya**. Jangan ditulis ulang — itu yang menjaga konsistensi. Tokoh/lokasi baru ditambahkan di bawah yang lama.

### 1 · BRIEF — tanya dulu, jangan menebak
Baca `references/brief.md`. Dua kartu pertanyaan (maksimal 4 per kartu):
- **Kartu 1:** topik · format · rasio · bahasa dialog
- **Kartu 2:** durasi per container · jumlah container · look/visual preset · tool target (menentukan satuan generate & mode frame)

Semua nilai dikosongkan — **tidak ada default**. Lewati yang sudah terjawab dari kalimat pertama user. Kalau jawaban bentrok (topik "tiap malam" vs look "siang cerah"), sebutkan bentroknya, jangan diam-diam memilih.
**Jumlah shot tidak pernah ditanyakan.** Shot ditentukan naskah.
**Output:** `brief.md`

### 2 · KONSEP → minta persetujuan
Baca `references/konsep-dan-naskah.md` dan bagian anti-klise di dalamnya.
**Output:** `konsep.md` — logline, premis 3 baris (termasuk satu detail meleset dan satu aturan tokoh), arc per container, **3 hook alternatif dengan rumus berbeda**.
Periksa sebelum setor: hook & arc tidak bertentangan dengan premis; tidak ada beat penting yang bergantung pada tulisan yang harus dibaca di layar.
**Berhenti.** User memilih hook dan menyetujui konsep dulu.

### 3 · BIBLE: CAST, SET & PROPERTI → minta persetujuan
Baca `references/cast-set-properti.md`.
**Output:** `cast.md`, `set.md`, dan `bible.json` (salinan terstruktur dari isi yang sama).
- Tokoh: satu blok terkunci dalam dua bentuk — **panjang** (prompt sheet) dan **pendek** (blok CHARACTERS prompt video). **Tanpa tanda di wajah** (bekas luka/tahi lalat/tato) kecuali tanda itu punya fungsi cerita.
- Set: satu blok per lokasi, termasuk **semua pintu dan jalan masuk** yang dipakai arc, material lantai, dan satu benda ganjil penanda ruangan.
- Properti berulang: dikunci seperti tokoh (berpelat atau teks saja).
- Tiap tokoh/set/properti berpelat dapat token `[gambar_<nama>]` yang sejalan dengan nama berkasnya.
- Kunci tepat **satu** color preset dan **satu** lens preset dari `references/visual-presets.md` ke dalam bible.
**Berhenti.** Mengganti deskripsi tokoh setelah prompt ditulis = menulis ulang semuanya.

### 4 · NASKAH + SHOT LIST → minta persetujuan
Baca `references/konsep-dan-naskah.md` bagian naskah.
**Output:** `epNN/naskah.md` (atau `actNN/` / section MV) — dialog lengkap yang bisa dibaca sebagai cerita, rundown per shot, pembagian scene.
- Satu scene = satu prompt video = satu kali generate. Panjang satuan generate mengikuti **tool target dari brief** (umumnya 4–30 detik; adapter sempit seperti Omni 3–15 detik memecah lebih kecil). Jangan memecah di tengah dialog. Pindah lokasi = scene baru.
- Cek total durasi ke `brief.md`. Kalau lewat, lapor dan tawarkan yang dipotong — jangan memotong diam-diam.
- **Shot berisiko ditandai dan dilaporkan** (daftar di `references/konsep-dan-naskah.md`): tempat sama dari dua sisi, shot lewat celah/kaca, sudut yang tidak ada di plate, benda yang harus bertahan antar potongan, close-up tanpa wajah dekat dialog. User yang memutuskan.
**Berhenti.**

### 5 · PROMPT ASET
Baca `references/prompt-aset.md`.
**Output:** `epNN/prompt-aset.md` — hanya aset **baru** di container itu, plus satu baris "pakai ulang" untuk aset lama.
Sheet karakter selalu: **close-up kiri, badan depan tengah, badan belakang kanan, nama tercetak di gambar**, latar abu netral, cahaya studio datar. Dilarang: rim light dramatis, grain berat, bokeh, sintaks khusus tool (mis. `--ar`) di dalam prompt — rasio diatur di tool, bukan di prompt.

### 6 · PROMPT FRAME & VIDEO
Baca `references/prompt-video.md`. Berkas terpenting skill ini.
**Output:** `epNN/prompt-video.md`.
- **Prompt frame (gambar diam)** dan **prompt video (gerakan)** selalu terpisah. Frame: hanya komposisi beku frame itu, tanpa kata kerja gerakan kamera. Video: sebelas blok berurutan — `VIDEO STYLE & FORMAT, LANGUAGE, OPTICS, CAMERA, LIGHTING, CRITICAL, CHARACTERS, LOCATION, [CONTINUITY], AUDIO, MOVEMENT NOTE, SHOT BREAKDOWN`.
- Untuk shot dengan gerakan subjek besar (berjalan, membuka pintu, menoleh jauh), buat **pasangan start frame + end frame** dengan cahaya & geometri latar identik.
- Setiap entri shot menyebut referensi yang dilampirkan/di-wire: `Lampirkan: <nama berkas>` di judul markdown, **di luar** blok prompt.

### 7 · AUDIO
Baca `references/audio.md`.
**Output:** `epNN/audio.md` — cue skor/OST (style tag, BPM, instrumentasi, struktur), naskah VO/dialogue cadangan untuk TTS bila adapter memisahkan audio, dan daftar Foley/ambience per shot.
Catatan: bila tool video target menggenerate dialog di dalam klip, audio.md bersifat pelengkap (skor & SFX untuk editor), **bukan** berkas dialogue terpisah yang menggantikan dialog di prompt video. Jangan dobel.

### 8 · VERIFIKASI & SERAH
Baca `references/verifikasi.md`.
Jalankan checker (bila Python tersedia): `python assets/tools/check_prompts.py <folder proyek>` — memeriksa salinan verbatim, sebelas blok, token vs lampiran, durasi/timecode, kata terlarang. Perbaiki sampai lolos, lalu checklist manual, lalu serahkan daftar berkas + cara pakai + kelemahan yang masih diketahui.
**Repair loop:** kalau user kembali dengan hasil generate yang salah, bedah dulu, perbaiki **satu atau dua kalimat** yang menyasar penyebab, simpan sebagai versi baru, rollback kalau memburuk. Prompt yang makin panjang tidak membuat model makin patuh.

## Aturan wajib (ringkasan — versi penuh di references)

1. **Blok cast/set/properti ditulis identik, huruf per huruf, di mana pun muncul.** Jangan meringkas, jangan memparafrase. Satu kata berubah, wajah berubah.
2. **Tidak ada default** untuk rasio, durasi, jumlah container, bahasa, look, tool target. Semuanya dari brief.
3. **Rasio, resolusi, seed, nama model, dan header manusia TIDAK masuk ke dalam blok prompt.** Itu pengaturan tool / judul markdown di luar blok.
4. **Dialog ditanam di prompt video** dan diucapkan persis seperti tertulis (blok `LANGUAGE`). Tidak ada subtitle/caption/teks layar — kata itu hanya boleh muncul sebagai larangan di `LANGUAGE`.
5. **Beat penting tidak bergantung pada tulisan yang harus dibaca.** Sampaikan lewat gambar atau suara.
6. **Tokoh tidak diberi tanda wajah** sebagai jangkar. Wajah dikunci gambar sheet; bedakan tokoh lewat usia, rambut, bangun badan, wardrobe.
7. **`MOVEMENT NOTE` selalu ada.** >2 orang di frame: wajib pecah gerak figuran dan larang gerakan serempak.
8. **Lighting ditulis sebagai sumber + arah + suhu warna + kontras**, bukan kata sifat (`dramatic lighting` dilarang berdiri sendiri).
9. **Lebih dari satu plate lokasi dalam satu generate** wajib tiga hal sekaligus: peta referensi di awal `LOCATION`, tag lokasi di tiap baris SHOT, dan posisi tokoh/benda di `CONTINUITY`.
10. **Benda yang harus bertahan antar potongan** dikunci di `CONTINUITY`: di mana persisnya, sejak shot berapa, terlihat di shot mana, dan di shot lain hanya di luar frame. Maksimal 3 benda; jangan menegaskan benda yang sama berulang-ulang di banyak blok.
11. **Shot lewat celah/kaca/mata tokoh: tulis hanya yang terlihat.** Jangan sebut tokoh, napas, mata, atau larangan orang di baris shot itu — kata itu menanam wajah di frame.
12. **Tiga gerbang persetujuan tidak dilompati:** konsep, bible, shot list.
13. **Shot berisiko dilaporkan, tidak disembunyikan dan tidak diganti diam-diam.**
14. **Prompt ditulis general** (Inggris; dialog dalam bahasa pilihan user), tidak diikat sintaks satu tool.

## Struktur skill

| Berkas | Isi |
|---|---|
| `references/brief.md` | gerbang 1: dua kartu, anti-tebak, bentrok jawaban |
| `references/konsep-dan-naskah.md` | gerbang 2 & 4: struktur per format, hook, anti-klise, shot list, shot berisiko, pemecahan scene |
| `references/cast-set-properti.md` | gerbang 3: blok terkunci panjang/pendek, token, set, properti, wardrobe varian |
| `references/prompt-aset.md` | gerbang 5: sheet 3 panel, plate set/properti, daftar Avoid |
| `references/prompt-video.md` | gerbang 6: prompt frame vs video, sebelas blok, CONTINUITY, peta referensi, start/end pairing |
| `references/audio.md` | gerbang 7: OST/Suno, VO/TTS, Foley per shot |
| `references/visual-presets.md` | color & lens preset terkunci (termasuk keluarga JP dari v1, diperluas) |
| `references/verifikasi.md` | gerbang 8: checker, checklist manual, gejala → penyebab, repair loop |
| `workflows/flow-micro-drama.md` | pacing micro-drama (tanpa default terkunci) |
| `workflows/flow-long-form.md` | pacing long-form |
| `workflows/flow-music-video.md` | pemetaan section lagu → visual |
| `assets/template/` | kerangka kosong tiap berkas keluaran + `bible.json` |
| `assets/contoh/satu-scene/` | satu scene lengkap yang lolos checker (acuan bentuk, bukan cerita untuk ditiru mentah) |
| `assets/tools/check_prompts.py` | checker gerbang 8 — Python 3, tanpa dependensi |
