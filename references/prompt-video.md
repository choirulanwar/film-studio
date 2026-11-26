# Prompt frame & video — gerbang 6

Berkas terpenting skill ini. Output: `epNN/prompt-video.md`.

## Dua jenis prompt, jangan dicampur

| | Prompt FRAME (gambar diam) | Prompt VIDEO (gerakan) |
|---|---|---|
| Untuk | start frame, end frame, still storyboard | satu kali generate video |
| Isi | komposisi beku satu frame: framing, pose statis, lingkungan, cahaya, preset terkunci | sebelas blok di bawah; gerakan hanya di sini |
| Dilarang | kata kerja gerakan kamera/subjek berjalan (`panning`, `walking across`, `dolly-in`) | deskripsi frame yang bertentangan dengan frame referensinya |

**Urutan rakit prompt frame** (dipertahankan dari v1, ini benar):
1. Framing & sudut kamera
2. Subjek + wardrobe + pose statis (blok pendek tokoh)
3. Lingkungan & cahaya praktis (blok set)
4. Lens preset terkunci
5. Color preset terkunci (suffix)

**Start/end pairing:** shot dengan gerakan subjek besar (berjalan, membuka pintu, menoleh jauh, berdiri dari duduk) wajib pasangan start + end frame dengan cahaya, geometri latar, dan preset **identik** — hanya pose subjek yang beda. Shot statis/dialog cukup start frame saja (atau tanpa frame, bila tool target text-to-video).

**Mode adapter:**
- Tool dengan slot frame (Flow/Veo I2V, Kling first/last): frame dilampirkan sebagai slot, prompt video tetap sebelas blok.
- Tool reference-only (Omni R2V dsb.): frame dipakai sebagai gambar referensi; tulis di judul markdown frame mana untuk shot mana. Jangan mengklaim start/end "terkunci" — di mode ini ia hanya acuan lunak.
- Spaces: frame = output node image; node video me-wire frame + sheet/plate sebagai input. Sebut wiring itu di judul scene, bukan di blok prompt.

## Bentuk berkas

Judul markdown + catatan lampiran **di luar** blok; di dalam blok hanya yang di-copy ke tool.

````markdown
## Scene 1 · Teras · 20 detik
Lampirkan: `sari_sheet.png`, `teras_plate.png`
Frame: start `ep01_sc01_start.png` (end: tidak perlu)

```
VIDEO STYLE & FORMAT
...
```
````

Jangan pernah menulis header seperti `=== PROMPT VIDEO · EP01 ===` **di dalam** blok — model bisa membacanya sebagai bagian adegan / menampilkannya sebagai teks.

## Sebelas blok, berurutan (aturan dulu, adegan terakhir)

### 1 · VIDEO STYLE & FORMAT
Jenis tontonan, durasi, tempo, gaya akting, look (dari preset terkunci), dan penegasan wajib: **satu momen berkelanjutan yang diliput dari banyak posisi kamera — NOT a trailer, NOT a montage.** Akhiri dengan baris `NOT ...` untuk hal khas yang harus dihindari (mis. `NOT sinetron, NO dramatic zooms`; dan genre yang bukan bila premis bisa disalahbaca: `NOT horror, NOT a thriller`). Durasi disebut di sini; **rasio tidak pernah disebut** (termasuk kata `vertical`/`horizontal`).

### 2 · LANGUAGE
Enam hal wajib:
1. Bahasa dialog, kapital (`INDONESIAN (Bahasa Indonesia)`)
2. Register (Jakarta kasual, baku, daerah — sesuai brief)
3. `Speak the lines exactly as written: do not translate them, do not paraphrase them, do not invent extra lines.`
4. Angka diucapkan sebagai kata dalam bahasa itu
5. `No subtitles, no captions, no on-screen text of any kind burned into the frame.` — satu-satunya tempat kata subtitle/caption boleh muncul di seluruh prompt
6. Nama tokoh tidak diucapkan kecuali ada di dalam tanda kutip dialog

Scene tanpa dialog tetap pakai blok ini, bentuk hening:
```
LANGUAGE
This scene has NO spoken dialogue — no voices, no narration, no inner monologue, no
whispering. No subtitles, no captions, no on-screen text of any kind burned into the frame.
```
Suara bukan tokoh (notifikasi, pengumuman, radio): sebut sumbernya di sini, tulis barisnya di SHOT BREAKDOWN seperti dialog.

### 3 · OPTICS
Lensa dasar scene + lensa close-up + bukaan bila kedalaman ruang penting. Acuan: 24mm ruang luas (~74°), 35mm natural (~54°), 50mm netral (~40°), 85mm isolasi wajah (~24°), 135mm kompresi kuat (~15°). Lensa per shot ditulis ulang di SHOT BREAKDOWN. Larang distorsi yang tidak diinginkan (`no fisheye, no zoom moves` bila berlaku).

### 4 · CAMERA
Daftar posisi fisik yang dipakai + kalimat wajib: **`Never two consecutive shots from the same position.`** Sebut rig (dolly, statis, handheld napas) dan aturan eyeline bila ada tatapan keluar frame. Gerakan dibatasi yang disebut di sini saja.

### 5 · LIGHTING
Bukan kata sifat. Lima hal wajib:
1. **Sumber** (matahari lewat jendela, fluorescent plafon, lampu meja, layar HP)
2. **Arah** (camera-left, atas, belakang)
3. **Suhu warna** (3200K hangat / 5600K siang / dst.)
4. **Kontras & negative fill** (low-key/high-key, sisi gelap dibiarkan/diisi)
5. **Satu aksen warna tunggal**
`dramatic lighting` tanpa sumber = tidak memberi informasi. Dilarang berdiri sendiri.

### 6 · CRITICAL
Kunci konsistensi. Sebut **jumlah eksplisit** tokoh bicara + figuran. Satu tokoh saja: `ONE character only. Nobody else appears at any point.` Selalu sertakan: wajah, rambut, pakaian persis dari gambar referensi di semua shot; no face swapping/morphing/duplicated faces; lip-sync akurat, hanya mulut tokoh yang bicara yang bergerak. Benda berlayar: `screen always angled away from camera, no readable screen`. Tanda wajah fungsional (bila ada, dari gerbang 3) diulang di sini termasuk sisinya.

### 7 · CHARACTERS
Bentuk pendek dari `cast.md`, **disalin**, satu baris per tokoh dengan tokennya. Deskripsi fisik lengkap tidak diulang di sini.

### 8 · LOCATION
Blok set dari `set.md` **disalin apa adanya** setelah tanda pisah, lalu properti scene itu (berpelat pakai token; teks saja disalin bloknya).
**Lebih dari satu plate lokasi dalam satu generate** → buka dengan **peta referensi**: plate mana, sisi mana, berlaku shot berapa. Pasangannya wajib lengkap tiga-tiganya: peta ini + tag lokasi tiap SHOT + posisi di CONTINUITY. Satu saja tidak cukup (tokoh bocor ke sisi pintu yang salah).

### CONTINUITY (opsional, di antara LOCATION dan AUDIO)
Dipakai bila: >1 plate lokasi, atau benda harus bertahan antar potongan. Satu butir per tokoh/benda: **di mana persisnya, sejak shot berapa, terlihat di shot mana, dan di shot lain ia hanya di luar frame / behind camera.** Maksimal 3 benda. Tulis sekali dengan kalimat sederhana lalu berhenti — benda yang ditegaskan berulang-ulang di banyak blok justru diubah model.

### 9 · AUDIO
Ambience/room tone, skor (atau `NO musical score` bila memang hening — hening yang disengaja ditulis, bukan ditinggal kosong), bunyi kunci per shot, tempo dialog. Detail cue produksi (OST/TTS/Foley lengkap) hidup di `audio.md` gerbang 7; blok ini ringkasannya untuk model video.

### 10 · MOVEMENT NOTE
**Selalu ada.**
- 1 tokoh: nada tubuhnya dari `cast.md`.
- 2 tokoh: dua ritme berlawanan, tidak pernah cermin.
- >2 orang: dua ritme utama + **wajib** pecah figuran jadi reaksi berbeda-beda dan larang eksplisit gerakan serempak (`never a synchronised crowd turn`).

### 11 · SHOT BREAKDOWN
Judul bagiannya persis `SHOT BREAKDOWN` (bukan SCREENPLAY/ACTION/SCENE).
Baris scene: `SCENE [00:00-00:NN] <LOKASI>` — tanpa nomor scene; `NN` = durasi blok 1, dan timecode selalu mulai 00:00.
Anatomi baris shot:
```
SHOT <n> (<mulai>-<selesai>s), <lensa> <UKURAN> from <posisi fisik>, <gerakan>: <aksi>.
```
- Timecode bersambung tanpa celah/tumpang tindih; shot terakhir berakhir tepat di `NN`.
- Lokasi ganda: tiap baris shot diberi **tag lokasi** tepat setelah timecode, di semua shot tanpa kecuali.
- Dialog: baris terpisah, nama kapital, kalimat dalam tanda kutip, bahasa sesuai brief; intonasi dalam kurung (`SARI (off-screen):`, `SARI (quietly):`).
- Shot tanpa dialog ditulis eksplisit: `No dialogue — <keterangan bunyi/hening>.`
- Baris penutup: bagaimana klip berhenti, selalu pada gerakan — `no freeze frame, no fade to black`.
- **Shot lewat celah/kaca/dari mata tokoh: tulis hanya apa yang terlihat.** Jangan sebut nama tokoh, napas, mata, kata tentang orang, atau larangan orang (`no face, no head`) di baris itu — kata itu menanam wajah di frame. Larangan orang cukup sekali di CRITICAL. Kata `POV` tidak perlu; tulis letak lensanya.
- **Bekas/ketiadaan benda ditulis sebagai permukaan rata** (`flat, level with the floor, nothing on it, not an object`), jangan dengan kata kontras (`darker`, `deeper colour`) — itu dirender jadi benda.
- Sudut balik: tulis letak kamera + apa di belakang tokoh, sekali saja.

## Dilarang masuk blok prompt

Rasio/resolusi/fps/seed/nama model · header manusia · nama berkas · nomor episode/judul seri · `subtitle`/`caption` di luar larangan LANGUAGE · `8k, ultra realistic, masterpiece, award winning` · sintaks khusus tool (`--ar`, dsb.) · menegaskan benda yang sama berulang-ulang di banyak blok · menegaskan ketiadaan dengan kata kontras.

## Saat menyerahkan

Satu baris di atas daftar scene:
> Generate per scene. Lampirkan berkas yang disebut di judul scene sebagai referensi, atur rasio & durasi di pengaturan tool sebelum generate. Frame start/end (bila ada) digenerate lebih dulu dari `prompt-aset.md`/prompt frame scene ini.
