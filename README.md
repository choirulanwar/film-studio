# Film Studio v2

Live-action AI film designer + production prompt writer: micro-drama, long-form film/series, and music video.

**Status: v2.1 — pushed for testing from Spaces, not a final release.** Live-tested via an LLM-node discussion in Spaces on 2026-11-26 (the LLM followed the gates in order and created 30 nodes itself); a real generation test is still pending. Entry point of the skill: [`SKILL.md`](SKILL.md). Change map from v1 and the reasoning behind it: [`CHANGELOG-DRAFT.md`](CHANGELOG-DRAFT.md).

## How to read this version

1. `SKILL.md` — gates, mandatory rules, adapter table (Manual / Spaces / Claude Code / Flow).
2. `references/` — the thick content per gate (brief, concept & script, cast/set/props, asset prompts, video prompts, audio, visual presets, verification).
3. `workflows/` — pacing per format, with no fixed numbers.
4. `assets/template/` — skeletons for a new project.
5. `assets/contoh/satu-scene/` — one complete scene ("Paket Terakhir") that passes the checker:

```
python assets/tools/check_prompts.py assets/contoh/satu-scene
```

## The v2 principle in one sentence

Write once, copy verbatim, lock it with tokens aligned to filenames, verify before handover — and never assume the runtime this skill runs in.
