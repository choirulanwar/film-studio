# Workflow: Long-Form Feature Film & Multi-Episode Series

## Target Specifications
- **Default Aspect Ratio:** `16:9` or `2.39:1`
- **Container Structure:** Acts (Act I, II, III) for features, or Episodes (`ep_01..ep_N`) for series
- **Clip Unit Duration:** 5–10 seconds per shot

## Continuity & Scalability Rules
1. **Incremental Expansion:** Never script all episodes in one pass. Develop one container/act at a time while updating `rolling_summary` in `bible.json`.
2. **Continuity State Overrides:** When time of day, weather, or wardrobe changes across scenes, keep the base `character_id` and `location_id` intact while applying explicit scene-level overrides (`wardrobe_override`, `lighting_override`).
3. **Dramatic Breathing Room:** Balance dialogue scenes with establishing wide shots, insert details, and contemplative atmospheric pauses.