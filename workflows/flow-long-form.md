# Workflow: Long-form — film fitur & seri multi-episode

Rasio, durasi, dan jumlah act/episode dari `brief.md`. Tidak ada patok 16:9 / 2.39:1 / klip 5–10 detik seperti v1.

## Aturan kerja

1. **Inkremental:** kerjakan satu container (act/episode) dalam satu lintasan gerbang 4–8. Jangan menulis semua episode sekaligus. Setelah satu container selesai, perbarui `rolling_summary` dan status container di `bible.json`.
2. **Override per scene, bukan entitas baru:** perubahan waktu, cuaca, atau wardrobe dicatat sebagai override di level scene (`wardrobe_override`, `lighting_override` di `bible.json`) dengan `character_id`/`location_id` tetap. Wardrobe yang berulang lintas container naik kelas jadi wardrobe varian di bible (gerbang 3).
3. **Ruang bernapas:** selingi dialog dengan establishing, insert benda kunci, dan jeda atmosferik — ditandai eksplisit di naskah sebagai shot tanpa dialog, bukan dibiarkan kosong.
4. **Arc vs container:** `konsep.md` memegang arc keseluruhan; tiap container wajib menggerakkan arc (keadaan tokoh/pengetahuan penonton berubah), bukan episode pengisi. Cek ini di gerbang 4 sebelum shot list ditulis.
