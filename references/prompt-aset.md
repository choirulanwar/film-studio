# Prompt aset — gerbang 5

Output `epNN/prompt-aset.md`: hanya aset **baru** di container itu. Aset lama cukup satu baris di kepala berkas:

```
Pakai ulang: sari_sheet.png, teras_plate.png (dari ep01)
```

Judul tiap aset = nama berkas hasil generate-nya. Nama berkas ditulis di judul markdown, **bukan** di dalam blok prompt.

## Sheet karakter — selalu 3 panel + nama

Komposisi baku (jangan diubah-ubah antar tokoh — konsistensi layout membantu user & model):

- **Kiri:** close-up wajah
- **Tengah:** badan penuh dari depan
- **Kanan:** badan penuh dari belakang
- **Nama tokoh tercetak di gambar** (satu-satunya teks yang sengaja diminta, supaya sheet tidak tertukar saat dilampirkan)
- Latar abu-abu netral polos, cahaya studio datar merata, pose netral berdiri

Template (isi dari bentuk panjang di `cast.md`, **disalin**, bukan ditulis ulang):

```
Character reference sheet of <BENTUK PANJANG>, three panels on a plain neutral
light-grey studio background, flat even studio lighting: LEFT panel close-up of the
face, CENTRE panel full body from the front, RIGHT panel full body from the back.
The name "<NAMA>" printed in plain capital letters at the top of the sheet.
Avoid: dramatic lighting, rim light, film grain, blur, bokeh, missing head, cropped
feet, different faces between panels, extra people, text other than the name.
```

Larangan yang dipertahankan dari v1 (benar, jangan dibuang): rim light dramatis, grain berat, mist, bokeh dangkal **di sheet** — semua itu menggeser geometri wajah & detail outfit. Sheet adalah dokumen identitas, bukan still film.
Dilarang juga: sintaks khusus tool (`--ar`, parameter model, dsb.) di dalam prompt. Rasio sheet diatur di tool gambar.

## Plate set

Satu gambar kosong per lokasi, dari **sudut shot wide terpenting** di scene itu — banyak model menyalin komposisi plate, jadi sudut plate = sudut yang paling sering dipakai.

```
Empty location reference plate of <BLOK SET dari set.md, disalin>, eye-level wide
framing from <sudut shot wide terpenting>, <cahaya dasar lokasi>.
Avoid: absolutely no people, no characters, no faces, no text, no logos, no vehicles
unless specified in the set block.
```

Frasa `absolutely no people` wajib ada — plate yang berisi orang akan menanam orang itu ke semua shot.

## Plate properti (hanya yang berpelat)

```
Reference plate of <BLOK PROPERTI dari set.md, disalin>, on a plain neutral
background, three-quarter view, flat even lighting, nothing else in frame.
Avoid: people, hands, text, labels, logos (kecuali larangan itu sudah ada di bloknya — jangan didobel dengan kata berbeda).
```

## Urutan serah

Di akhir berkas, satu baris instruksi untuk user/adapter:

> Generate semua aset di berkas ini dulu, simpan dengan nama berkas persis seperti judulnya, baru generate frame/video. Sheet/plate yang belum digenerate = jangan mulai gerbang 6 untuk shot yang memakainya.
