# Brief — Gate 1

Purpose: lock every decision that is expensive to change mid-way, **before** a single prompt is written.

## Two cards

Question tools usually allow at most 4 questions per card, so the brief is always two cards:

- **Card 1:** topic/initial premise · format (micro-drama / long-form / music video) · ratio · dialogue language
- **Card 2:** duration per container · number of containers · look (pick/customize from `visual-presets.md`) · target tool (the image + video tools the user/adapter will use)

Skip items already answered clearly in the user's first message. Do not re-ask what has already been given.

## Anti-guessing rules

- **All values are left empty. There are no defaults.** v1 hard-coded 9:16 / 60–90 seconds / 3–5 second clips — that is revoked. If the user has not answered, the `brief.md` file writes `UNDECIDED` and the next gate does not start.
- **Shot count is never asked and never fixed.** Shots are born from the script (Gate 4).
- **The target tool must be clear** because it determines: the duration unit of one generation, whether start/end frames are supported, whether dialogue is generated inside the clip or as separate audio, and whether reference images can be attached. If the user does not know their tool yet, note `manual / not yet chosen` and use the general 4–30 second unit.
- **"Up to you" is not an answer.** If the user says "up to you" for ratio/duration, offer 2–3 concrete options with their consequences (e.g. "9:16 = feed vertikal, wajah dominan; 16:9 = ruang lebih lega, cocok YouTube") and ask them to pick one. Do not choose for them silently.
- **Conflicting answers are stated.** Example: topic "kurir malam" + look "siang cerah" + preset `jp-blue-hour`. State the conflict, offer a resolution (change the look, or keep it deliberately as contrast), and record the user's decision in `brief.md`.
- **If the work location/folder is unclear, ASK — never fill in any default, including a plausible-looking path such as /app/<project-name>/. A value invented at Gate 0 propagates through the whole project.**

## Output: `brief.md`

Use `assets/template/brief.md`. One line per decision, plus a `Keputusan bentrok & resolusinya` ("Conflicts & their resolutions") line if there are any. `brief.md` is the only place these numbers live; other gates refer here — they do not copy in new numbers.
