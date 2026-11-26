# Workflow: Long-form — feature films & multi-episode series

Aspect ratio, duration, and number of acts/episodes come from `brief.md`. There are no fixed 16:9 / 2.39:1 / 5–10-second clip defaults like v1 had.

## Working rules

1. **Incremental:** work on one container (act/episode) in a single pass through gates 4–8. Do not write all episodes at once. After one container is finished, update `rolling_summary` and the container status in `bible.json`.
2. **Per-scene overrides, not new entities:** changes in time, weather, or wardrobe are recorded as scene-level overrides (`wardrobe_override`, `lighting_override` in `bible.json`) with the same `character_id`/`location_id`. A wardrobe that recurs across containers is promoted to a wardrobe variant in the bible (gate 3).
3. **Breathing room:** interleave dialogue with establishing shots, inserts of key objects, and atmospheric pauses — marked explicitly in the script as no-dialogue shots, not left blank.
4. **Arc vs container:** `konsep.md` holds the overall arc; every container must move the arc (a character's state or the audience's knowledge changes), not be a filler episode. Check this at gate 4 before the shot list is written.
