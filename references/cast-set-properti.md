# Cast, set & properti bible — gerbang 3

Gerbang ini menentukan konsisten atau tidaknya wajah, ruangan, dan benda di seluruh proyek. Mekanismenya bukan sihir: **satu teks ditulis sekali, lalu disalin identik ke mana pun ia dipakai.**

## Aturan salin verbatim (inti v2)

> Tulis sekali di `cast.md` / `set.md`, lalu **salin — jangan ketik ulang, jangan ringkas, jangan parafrase.**
> "Rambut cepak hitam" dan "rambut pendek hitam" adalah dua orang berbeda bagi model.
> Checker gerbang 8 menolak proyek yang salinannya tidak identik.

`bible.json` adalah salinan terstruktur dari isi yang sama (id, token, nama berkas, preset terkunci) untuk adapter yang membutuhkannya. Kalau bible teks dan `bible.json` beda, **bible teks yang benar**.

## Tokoh — dua bentuk

### Bentuk panjang (untuk prompt sheet, gerbang 5)

Urutan wajib:
1. Kebangsaan & jenis kelamin
2. Usia & tinggi
3. Warna kulit
4. Rambut: panjang, warna, tatanan
5. Bentuk wajah/rahang
6. Bangun badan

Lalu `WARDROBE:` per item (warna + bahan + detail pembeda), lalu `NADA TUBUH:` satu kalimat cara ia berdiri/bergerak (dipakai ulang di `MOVEMENT NOTE`).

```
[SARI] — bentuk panjang
Indonesian woman, 34 years old, 160 cm, medium brown skin, shoulder-length black hair
tied in a low ponytail, oval face, soft build.
WARDROBE: faded mustard-yellow courier vest over a grey long-sleeve t-shirt, black
cargo trousers, worn white sneakers, a small black waist pouch.
NADA TUBUH: cepat dan hemat gerak, selalu berdiri miring siap berangkat, jarang diam lebih dari dua detik.
```

### Tanpa tanda di wajah

Jangan beri tokoh bekas luka, tahi lalat, tato, tindik, atau tanda kecil lain sebagai "jangkar". Model selalu melebih-lebihkannya (luka 1 cm jadi codet) dan tandanya berpindah sisi antar generate. Wajah dikunci **gambar sheet**; tokoh dibedakan lewat usia, tinggi, rambut, bangun badan, kacamata, dan terutama wardrobe.
Pengecualian tunggal: tanda yang **punya fungsi cerita** (ditanam dan dibayar di naskah). Syarat: ditulis kecil/halus (`a small, faint ...`), sisinya disebut, dan diulang eksplisit di blok `CRITICAL` prompt video.

### Bentuk pendek (untuk blok CHARACTERS prompt video)

Satu baris: nama, token, usia, wardrobe ringkas, aktivitas di scene itu. Deskripsi fisik lengkap **tidak** diulang — gambar referensi yang mengunci wajah; mengulang deskripsi panjang bisa bertabrakan dengan gambarnya.

```
SARI [gambar_sari] — 34, faded mustard-yellow courier vest over a grey long-sleeve
t-shirt, black cargo trousers, holding a small cardboard package at the gate.
```

Bagian aktivitas berubah per scene; bagian wardrobe tidak, kecuali varian di bawah.

### Wardrobe varian

Tokoh ganti baju di container lain: jangan timpa. Tambahkan `WARDROBE B (ep 4-6): ...`, buat sheet baru, token dibedakan `[gambar_sari_b]`.

## Token & nama berkas (harus sejalan)

| Entitas | Token | Nama berkas |
|---|---|---|
| Tokoh Sari | `[gambar_sari]` | `sari_sheet.png` |
| Lokasi Teras | `[gambar_teras]` | `teras_plate.png` |
| Properti Motor | `[gambar_motor]` | `motor_plate.png` |

Pola: `<nama>_sheet.png` (tokoh) / `<nama>_plate.png` (set & properti), `<nama>` sama persis dengan token setelah `gambar_`. User mencari berkas dari token; kalau beda, salah lampir, wajah tertukar.

## Set — satu blok per lokasi

Wajib memuat:
1. Jenis ruang & di mana
2. Satu elemen arsitektur besar penentu komposisi
3. Furnitur utama (+ jumlah bila penting)
4. Material lantai (menentukan pantulan cahaya)
5. **Satu benda ganjil** penanda ruangan itu
6. **Semua pintu & jalan masuk yang dipakai tokoh di arc** — siapa masuk/keluar dari mana. Pintu yang tidak tertulis akan dikarang model, berbeda tiap klip.

```
[TERAS] [gambar_teras]
Front terrace of a small suburban house in Bekasi. One frosted-glass sliding door
facing a low iron fence and a narrow residential lane. Cracked cream ceramic tile
floor. A single plastic chair and a dry potted plant beside the door. Entry points:
the sliding door (from the living room) and the fence gate (from the lane).
```

## Properti — dikunci seperti tokoh

Benda/kendaraan yang muncul di >1 shot dan bisa berubah bentuk antar klip.

| Jenis | Kapan | Bentuk |
|---|---|---|
| Berpelat | bentuk rumit: kendaraan, perabot khas | blok teks + token + prompt plate (gerbang 5) |
| Teks saja | benda kecil sederhana: kardus, gelas, foto | blok teks saja, disalin identik |

Untuk benda yang di dunia nyata bertulisan (label paket, plat nomor, merek): tulis larangannya **di dalam bloknya** — `no labels, no printed text, no logos`, `licence plate blank`.

```
[PAKET] — teks saja
small brown cardboard box, roughly shoebox size, wrapped in clear packing tape, no
labels, no printed text, no logos
```

Di prompt video, properti ditulis di blok `LOCATION` setelah lokasinya; yang harus bertahan antar potongan naik ke `CONTINUITY`.

## Visual lock

Di gerbang ini juga kunci, dari `references/visual-presets.md`:
- tepat **satu** `color_preset_id`
- tepat **satu** `lens_preset_id` (lensa dasar; lensa per shot tetap ditulis di SHOT BREAKDOWN)

Tulis keduanya di `cast.md`/`bible.json`. Preset tidak diganti di tengah proyek tanpa mencatatnya sebagai revisi bible dan menulis ulang prompt yang sudah jadi.

## Melanjutkan proyek lama

Baca bible yang ada, pakai apa adanya. Tambah tokoh/lokasi di bawah yang lama. Jangan pernah menulis ulang blok lama — penulisan ulang = wajah baru.
