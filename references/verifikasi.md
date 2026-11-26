# Verifikasi & serah — gerbang 8

Hampir semua kegagalan film AI adalah kesalahan **teks** yang baru ketahuan setelah kredit terbakar. Gerbang ini menangkapnya sebelum itu.

## Langkah 1 · Checker mesin

```
python assets/tools/check_prompts.py <folder proyek>
```

Yang dicek versi draft ini: sebelas blok ada & berurutan · frasa wajib (`NOT a montage`, `Never two consecutive shots from the same position`, larangan subtitle, `exactly as written` atau `NO spoken dialogue`, `no freeze frame`) · kata terlarang di dalam blok prompt (rasio, `vertical/horizontal`, `===`, nama berkas, `SCREENPLAY`, resolusi/seed/fps, `8k/masterpiece`) · token di prompt punya baris lampiran · timecode SHOT bersambung dan berakhir di durasi scene.
Perbaiki sampai lolos. Jangan serahkan proyek yang belum lolos tanpa menyebutkannya.

## Langkah 2 · Checklist yang tidak bisa dicek mesin

- [ ] Salinan blok cast/set/properti **identik huruf per huruf** di semua berkas (checker draft belum memeriksa ini penuh — baca manual dua berkas yang paling jauh: `cast.md` vs prompt terakhir)
- [ ] Tidak ada dua shot berurutan dari posisi kamera yang sama
- [ ] `MOVEMENT NOTE` sesuai jumlah orang; >2 orang memecah figuran
- [ ] Tidak ada beat penting bergantung pada tulisan yang harus dibaca
- [ ] Hook, arc, set, alasan tokoh tidak bertentangan dengan premis
- [ ] Detektor klise (`konsep-dan-naskah.md`) sudah dijalankan ke naskah
- [ ] Genre yang bukan sudah disebut di `VIDEO STYLE & FORMAT` bila premis bisa disalahbaca
- [ ] Benda berlayar: `screen always angled away from camera` ada di CRITICAL
- [ ] Tidak ada tanda wajah di blok tokoh, kecuali yang berfungsi cerita
- [ ] Shot berisiko gerbang 4 tercatat keputusannya di `naskah.md`
- [ ] Shot lewat celah/kaca tidak menyebut tokoh/kata orang
- [ ] Ketiadaan benda ditulis sebagai permukaan rata, tanpa kata kontras
- [ ] Tidak ada benda yang ditegaskan berulang di banyak blok
- [ ] LIGHTING menyebut sumber + arah + suhu, bukan kata sifat saja
- [ ] Untuk adapter Spaces: referensi sheet/plate **benar-benar ter-wire** sebagai input node frame/video, bukan hanya disebut di teks

## Gejala → penyebab (untuk repair)

| Gejala di hasil generate | Penyebab paling mungkin di teks/wiring |
|---|---|
| Wajah berubah antar klip | Blok tokoh diparafrase di satu berkas · sheet salah lampir (token ≠ nama berkas) · referensi tidak ter-wire (Spaces) / tidak dilampirkan (manual) |
| Wajah aneh: codet, bisul, tanda besar | Tanda kecil di blok tokoh dilebih-lebihkan model — hapus bila tak berfungsi cerita |
| Teks aneh / huruf acak di layar | Header manusia ikut ke-copy · label/plat/layar tidak diberi larangan teks · layar menghadap kamera |
| Dialog bahasa/diksi meleset, ditambah, diparafrase | Blok LANGUAGE hilang / frasa `exactly as written` terhapus |
| Narasi/gumaman di scene hening | LANGUAGE tidak memakai bentuk `NO spoken dialogue` |
| Figuran gerak serempak | MOVEMENT NOTE hilang / tidak melarang eksplisit |
| Orang asing muncul di tempat sepi | CRITICAL tidak mengunci jumlah orang |
| Hasil terasa montase/trailer | Penegasan `ONE continuous ... NOT a montage` hilang dari blok 1 |
| Potongan monoton | Dua shot seposisi berurutan / aturan posisi beda tidak ditulis |
| Frame datar | LIGHTING kata sifat tanpa sumber & arah |
| Benda hilang/pindah/dobel antar potongan | Tidak ada butir CONTINUITY (posisi persis + shot terlihat) |
| Tokoh bocor ke sisi pintu yang salah | >1 plate tanpa peta referensi + tag lokasi + CONTINUITY sekaligus |
| Wajah muncul di shot celah/kaca | Baris shot itu menyebut tokoh/kata orang/larangan orang |
| Pintu yang ditegaskan `stays closed` malah dibuka | Penegasan ditumpuk di banyak blok — kurangi, tulis sekali di CONTINUITY |
| Sheet panel badan tanpa kepala / wajah beda antar panel | Daftar Avoid sheet tidak lengkap (`missing head`, `different faces between panels`) |

## Setelah user generate — repair loop

1. **Bedah dulu, jangan menebak.** Cocokkan titik potong & isi video dengan timecode prompt; transkrip dialog bila bisa. Pastikan dulu versinya benar: prompt versi mana, model apa, rasio apa, referensi apa.
2. **Pisahkan plot hole dari penyimpangan.** Sudut beda tapi cerita utuh = bukan masalah. Pintu terbuka di cerita "pintu tak pernah dibuka" = masalah.
3. **Perbaiki 1–2 kalimat yang menyasar penyebab** (pakai tabel di atas). Simpan sebagai versi baru (`prompt-video-v2.md`), jangan timpa yang lama.
4. **Uji dengan syarat sama:** model, rasio, referensi sama.
5. **Memburuk → rollback.** Jangan menumpuk perbaikan.
6. **Bertahan 2 putaran = batas model, bukan batas teks.** Tawarkan ganti shot (alternatif shot berisiko) atau ganti model.

## Bentuk serah

Daftar berkas + urutan pakai + **kelemahan yang masih diketahui** (scene yang shot-nya tipis, dua wardrobe terlalu mirip, shot berisiko yang dipertahankan user). Lebih baik user tahu sebelum generate.

```markdown
Selesai, checker lolos. Berkasnya:
<pohon berkas proyek>

Urutan pakai:
1. Generate aset `prompt-aset.md`, simpan persis dengan nama berkas di judulnya.
2. Generate frame start/end (bila ada), lalu video per scene di `prompt-video.md` dengan lampiran di judul scene.
3. Atur rasio & durasi di tool sebelum generate.
4. Skor/SFX dari `audio.md` dipasang di edit.
```
