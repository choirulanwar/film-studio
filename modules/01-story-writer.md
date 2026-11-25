# Module 01: Story Writer & Beat Breakdown

## Responsibilities
1. **Pre-Production:** Write the logline, character bios, world rules, and dynamic container outline.
2. **Scene Breakdown:** Convert an active scene into sequential **Beats** matching `pacing_profile.clip_unit_sec` from `bible.json`.

## Beat Output Format
For each beat, specify:
- `beat_id`: e.g., `ep01_sc01_b01`
- `duration_sec`: Target clip length
- `location_id` & `time_of_day`
- `characters_present`: List of IDs from `bible.json`
- `visual_action`: Concrete, filmable physical action (avoid abstract internal thoughts; show emotion through posture, gaze, and environment)
- `dialogue_or_vo`: Spoken lines or `[SILENT ATMOSPHERIC BEAT]`