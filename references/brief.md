# Brief — gerbang 1

Tujuan: mengunci semua keputusan yang mahal kalau berubah di tengah jalan, **sebelum** satu prompt pun ditulis.

## Dua kartu

Alat tanya biasanya maksimal 4 pertanyaan per kartu, jadi brief selalu dua kartu:

- **Kartu 1:** topik/premis awal · format (micro-drama / long-form / music video) · rasio · bahasa dialog
- **Kartu 2:** durasi per container · jumlah container · look (pilih/kustom dari `visual-presets.md`) · tool target (gambar + video yang akan dipakai user/adapter)

Lewati item yang sudah terjawab jelas dari kalimat pertama user. Jangan menanyakan ulang yang sudah diberikan.

## Aturan anti-tebak

- **Semua nilai dikosongkan. Tidak ada default.** v1 mematok 9:16 / 60–90 detik / klip 3–5 detik — itu dicabut. Kalau user belum menjawab, berkas `brief.md` menulis `BELUM DITENTUKAN` dan gerbang berikutnya tidak mulai.
- **Jumlah shot tidak pernah ditanyakan dan tidak dipatok.** Shot lahir dari naskah (gerbang 4).
- **Tool target wajib jelas** karena ia menentukan: satuan durasi satu generate, apakah start/end frame didukung, apakah dialog digenerate di dalam klip atau audio terpisah, dan apakah referensi gambar bisa dilampirkan. Kalau user belum tahu tool-nya, catat `manual / belum dipilih` dan pakai satuan umum 4–30 detik.
- **"Terserah" bukan jawaban.** Kalau user bilang terserah untuk rasio/durasi, tawarkan 2–3 pilihan konkret dengan konsekuensinya (mis. "9:16 = feed vertikal, wajah dominan; 16:9 = ruang lebih lega, cocok YouTube") dan minta ia memilih satu. Jangan memilihkan diam-diam.
- **Jawaban bentrok disebutkan.** Contoh: topik "kurir malam" + look "siang cerah" + preset `jp-blue-hour`. Sebutkan bentroknya, tawarkan resolusi (ubah look, atau memang disengaja sebagai kontras), catat keputusan user di `brief.md`.

## Output: `brief.md`

Gunakan `assets/template/brief.md`. Satu baris per keputusan, plus baris `Keputusan bentrok & resolusinya` bila ada. `brief.md` adalah satu-satunya tempat angka-angka ini hidup; gerbang lain merujuk ke sini, tidak menyalin angka baru.
