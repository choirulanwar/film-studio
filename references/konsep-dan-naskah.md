# Konsep & naskah — gerbang 2 dan 4

## Gerbang 2 · Konsep

Output `konsep.md` wajib memuat:

1. **Logline** — satu kalimat: siapa, mau apa, apa halangannya, apa taruhannya.
2. **Premis 3 baris** — baris ke-3 wajib memuat **satu detail meleset** (sesuatu yang tidak pas dan bikin penasaran) dan **satu aturan tokoh** (kebiasaan/larangan tokoh yang akan menghasilkan adegan, bukan sekadar sifat).
3. **Arc per container** — untuk seri: satu baris per episode (keadaan awal → peristiwa → cliffhanger). Untuk long-form: per babak. Untuk MV: per section lagu.
4. **3 hook alternatif dengan rumus berbeda** — contoh rumus: (a) pertanyaan visual yang belum terjawab, (b) tindakan yang konsekuensinya belum terlihat, (c) kedatangan/kepergian yang mengubah status quo. User memilih satu; jangan menggabungkan ketiganya jadi satu hook yang ramai.

### Cek sebelum setor (wajib, diam-diam)

- Hook dan arc **tidak bertentangan** dengan premis (tokoh yang "tidak pernah membuka pintu" tidak boleh membuka pintu di arc ep.1 tanpa itu memang titik ceritanya).
- **Tidak ada beat penting yang bergantung pada tulisan yang harus dibaca** — nama di label paket, chat di layar HP, papan nama. AI video tidak bisa merender tulisan dengan andal dan prompt kita melarang teks layar. Sampaikan beat itu lewat gambar, benda, atau suara.
- Genre yang bukan: kalau premis bisa disalahbaca model (rumah sepi, mengintip, orang tua diam) catat di konsep genre yang harus dilarang nanti di blok `VIDEO STYLE & FORMAT` (mis. `NOT horror`).

### Anti-generik (detektor klise)

Tolak dan tulis ulang bila konsep/naskah mengandung salah satu ini tanpa putaran baru:

- Tokoh "menyimpan rahasia besar" yang tidak pernah dispesifikkan di konsep.
- Dialog penjelasan: tokoh mengucapkan hal yang kedua tokoh sudah tahu, demi penonton.
- Dialog sinetron: seruan berulang, panggilan nama di tiap baris, ancaman yang diucapkan bukan dilakukan.
- Kebetulan yang menyelesaikan masalah (yang menolong boleh kebetulan; yang menyelesaikan tidak).
- Montase "waktu berlalu" sebagai pengganti adegan.
- Akhir episode berupa tokoh menatap kamera / membelalak saja, tanpa perubahan keadaan.

Uji dialog: baca keras-keras. Kalau satu baris bisa diucapkan tokoh mana pun di cerita mana pun, baris itu generik — tulis ulang dengan detail milik tokoh ini (pekerjaannya, benda di tangannya, alamatnya).

## Gerbang 4 · Naskah + shot list

Output `epNN/naskah.md` (long-form: `actNN/` boleh digabung per episode; MV: per section):

1. **Naskah dialog lengkap** — bisa dibaca sebagai cerita tanpa melihat prompt-nya.
2. **Rundown per shot** — nomor shot, durasi, ukuran/lensa, posisi kamera fisik, aksi, dialog (atau keterangan eksplisit tanpa dialog).
3. **Pembagian scene** — satu scene = satu prompt video = satu kali generate.

### Pemecahan scene

- Satuan durasi mengikuti tool target di `brief.md`. Tanpa tool spesifik: **4–30 detik** per generate.
- Episode/container lebih panjang dari satuan itu dipecah **mengikuti beat** (mis. 60 detik → 30+30, atau 20+20+20), **tidak pernah di tengah dialog**, dan **pindah lokasi selalu scene baru**.
- Timecode tiap prompt selalu mulai dari `00:00` — tiap generate berdiri sendiri.
- Total durasi dicek ke `brief.md`. Kelebihan dilaporkan dengan tawaran shot yang dipotong; jangan memotong diam-diam.

### Shot berisiko — tandai, laporkan, user yang memutuskan

| Risiko | Kenapa gagal | Alternatif yang ditawarkan |
|---|---|---|
| Tempat yang sama dari dua sisi (pintu, pagar, jendela) | Tokoh bocor ke sisi yang salah | Satu sisi saja + suara dari sisi lain; atau peta referensi + tag lokasi + CONTINUITY (gerbang 6) |
| Shot lewat celah, kaca, jendela | Model menanam wajah/benda di celah; kaca jadi bening | Tulis hanya yang terlihat; plate dari sudut celah itu sendiri |
| Sudut kamera yang tidak ada di plate | Model mengarang geometri ruangan | Buat plate tambahan dari sudut itu, atau ubah posisi kamera ke sudut plate |
| Benda harus bertahan antar potongan | Benda hilang/pindah/dobel | Blok CONTINUITY (maks. 3 benda) |
| Close-up tanpa wajah dekat momen dialog | Model menambah baris dialog / mulut dari tokoh lain | Geser dialog ke shot dengan wajah, atau tandai shot itu eksplisit tanpa dialog |
| Kerumunan bereaksi bersama | Gerak serempak seperti paduan suara | MOVEMENT NOTE memecah reaksi (gerbang 6) |
| Tulisan harus terbaca | Render jadi huruf acak | Ubah beat: tulisan disampaikan lewat suara/gambar |

Daftar shot berisiko ditulis di akhir `naskah.md` beserta keputusan user (dipertahankan / diganti).

### Blocking vs set

Kalau blocking butuh pintu, jendela, atau elemen ruang yang belum ada di `set.md`, **tambahkan sekarang** (penambahan saja, jangan ubah blok lama) dan catat sebagai revisi di `set.md` — sebelum prompt ditulis.
