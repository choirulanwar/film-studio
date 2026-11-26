# Film Studio v2 (DRAFT)

Perancang film AI live-action + penulis prompt produksi: micro-drama, film/seri long-form, dan music video.

**Status: draft v2 — dipush untuk dites dari Spaces, belum rilis final.** Titik masuk skill: [`SKILL.md`](SKILL.md). Peta perubahan dari v1 dan alasannya: [`CHANGELOG-DRAFT.md`](CHANGELOG-DRAFT.md).

## Cara membaca draft ini

1. `SKILL.md` — gerbang, aturan wajib, tabel adapter (Manual / Spaces / Claude Code / Flow).
2. `references/` — isi tebal per gerbang (brief, konsep & naskah, cast/set/properti, prompt aset, prompt video, audio, visual presets, verifikasi).
3. `workflows/` — pacing per format, tanpa angka patok.
4. `assets/template/` — kerangka berkas proyek baru.
5. `assets/contoh/satu-scene/` — satu scene lengkap ("Paket Terakhir") yang lolos checker:

```
python assets/tools/check_prompts.py assets/contoh/satu-scene
```

## Prinsip v2 dalam satu kalimat

Tulis sekali, salin verbatim, kunci dengan token yang sejalan dengan nama berkas, verifikasi sebelum serah — dan jangan pernah mengasumsikan runtime tempat skill ini berjalan.
