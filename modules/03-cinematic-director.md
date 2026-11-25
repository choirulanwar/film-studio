# Module 03: Cinematic Director & Prompt Assembler

## Responsibilities
Combine locked entities (`bible.json`), scene beats (`01-story-writer`), framing (`references/framing-motion.md`), and locked visual presets (`color-presets.md` + `camera-lenses.md`) into production-ready generation prompts.

## Strict Prompt Assembly Order
Assemble every **Start Frame (Still Image)** prompt in this exact weight order:
1. `[FRAMING & CAMERA ANGLE]` (from `framing-motion.md`)
2. `[SUBJECT, WARDROBE & STATIC POSE]` (referencing locked `character_id`)
3. `[ENVIRONMENT & PRACTICAL LIGHTING]` (referencing locked `location_id`)
4. `[LOCKED LENS SPEC]` (from `bible.json`)
5. `[LOCKED COLOR PRESET SUFFIX]` (from `bible.json`)

## Critical Separation Rule
- **NEVER** put camera movement verbs (`panning`, `zooming`, `dolly-in`, `walking across`) inside the **Start Frame Prompt**. Describe only the exact frozen composition of frame 1.
- Put all camera movement and environmental motion exclusively inside the **Video Motion Prompt**.

## Storyboard Deliverable Table
Render every scene using this Markdown table:
| Shot # | Dur | Framing | Start Frame Prompt (Image) | End Frame Prompt (Optional) | Video Motion Prompt (Flow/Veo) | Audio / Dialogue Cue |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |

## Continuity & Reference Binding Rules (Mandatory)
1. **Asset Attachment Directive:** Every shot entry MUST specify exact reference files to attach in the generation node (`Refs: [character_sheet_file], [location_plate_file]`).
2. **Identity Lock Clause:** When a character appears, always include: `maintaining exact facial identity, hairstyle, and outfit from attached character reference sheet, crisp facial focus`.
3. **Start/End Frame Pairing:** For shots involving significant subject movement (turning head, walking, opening doors), generate BOTH a `Start Frame` and an `End Frame` with identical lighting and background geometry to prevent video morphing.
4. **Cut-to-Cut Continuity:** Maintain consistent screen direction (left-to-right / right-to-left) and matching lighting direction across consecutive shots within the same scene.