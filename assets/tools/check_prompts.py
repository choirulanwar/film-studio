#!/usr/bin/env python3
"""film-studio v2 — gate-8 checker (draft).

Usage: python check_prompts.py <project-folder>
Checks every prompt-video.md under the folder:
  - eleven blocks present and in order (CONTINUITY optional, between LOCATION and AUDIO)
  - required phrases
  - banned words inside prompt blocks
  - tokens used in a prompt have a matching file on an 'Attach:' line above it (legacy 'Lampirkan:' also accepted)
  - SHOT timecodes are contiguous and end at the scene duration
Exit code 0 when all checks pass, 1 otherwise. No dependencies.
"""
import re
import sys
from pathlib import Path

BLOCKS = ["VIDEO STYLE & FORMAT", "LANGUAGE", "OPTICS", "CAMERA", "LIGHTING",
          "CRITICAL", "CHARACTERS", "LOCATION", "AUDIO", "MOVEMENT NOTE",
          "SHOT BREAKDOWN"]
REQUIRED_PHRASES = ["NOT a montage",
                    "Never two consecutive shots from the same position",
                    "No subtitles, no captions, no on-screen text",
                    "no freeze frame"]
LANGUAGE_ALTERNATIVES = ["exactly as written", "NO spoken dialogue"]
BANNED = [r"\b9:16\b", r"\b16:9\b", r"\bvertical\b", r"\bhorizontal\b", r"===",
          r"\.png\b", r"\.jpg\b", r"\bSCREENPLAY\b", r"\b\d{3,4}p\b", r"\bseed\b",
          r"\bfps\b", r"\b8k\b", r"\bmasterpiece\b", r"--ar\b"]


def check_file(path: Path, errors: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    # split into scene sections by markdown headings, keep Lampirkan context
    sections = re.split(r"(?m)^## ", text)
    for section in sections[1:]:
        blocks = re.findall(r"```(.*?)```", section, re.S)
        lampirkan = " ".join(re.findall(r"(?:Attach|Lampirkan):(.*)", section))
        for block in blocks:
            if "VIDEO STYLE & FORMAT" not in block:
                continue
            where = f"{path}: scene '{section.splitlines()[0][:40]}'"
            # block order (CONTINUITY allowed between LOCATION and AUDIO)
            positions = []
            for name in BLOCKS:
                idx = block.find("\n" + name + "\n") if not block.startswith(name) else 0
                if idx < 0:
                    errors.append(f"{where}: blok hilang: {name}")
                positions.append(idx)
            if positions == sorted(positions) and -1 not in positions:
                cont = block.find("\nCONTINUITY\n")
                if cont >= 0 and not (positions[7] < cont < positions[8]):
                    errors.append(f"{where}: CONTINUITY harus di antara LOCATION dan AUDIO")
            flat = re.sub(r"\s+", " ", block)
            for phrase in REQUIRED_PHRASES:
                if phrase not in flat:
                    errors.append(f"{where}: frasa wajib hilang: '{phrase}'")
            if not any(alt in flat for alt in LANGUAGE_ALTERNATIVES):
                errors.append(f"{where}: LANGUAGE wajib memuat 'exactly as written' atau 'NO spoken dialogue'")
            for pat in BANNED:
                if re.search(pat, block, re.I):
                    errors.append(f"{where}: kata terlarang di dalam blok prompt: /{pat}/")
            for token in re.findall(r"\[gambar_([a-z0-9_]+)\]", block):
                expected_sheet = f"{token}_sheet"
                expected_plate = f"{token}_plate"
                if expected_sheet not in lampirkan and expected_plate not in lampirkan:
                    errors.append(f"{where}: token [gambar_{token}] tidak punya berkas lampiran yang sejalan")
            # timecodes
            m = re.search(r"(\d+)-second scene", block)
            scene = re.search(r"SCENE \[00:00-00:(\d+)\]", block)
            shots = re.findall(r"SHOT \d+ \((\d+)-(\d+)s\)", block)
            if not m or not scene:
                errors.append(f"{where}: durasi scene tidak ditemukan / tidak sepakat (blok 1 vs baris SCENE)")
                continue
            duration = int(m.group(1))
            if int(scene.group(1)) != duration:
                errors.append(f"{where}: durasi blok 1 ({duration}) != baris SCENE ({scene.group(1)})")
            if not (4 <= duration <= 30):
                errors.append(f"{where}: durasi {duration} di luar satuan umum 4-30 detik (cek brief/tool target)")
            expected_start = 0
            for start, end in shots:
                if int(start) != expected_start:
                    errors.append(f"{where}: timecode SHOT tidak bersambung di {start}s (harusnya {expected_start}s)")
                expected_start = int(end)
            if shots and expected_start != duration:
                errors.append(f"{where}: shot terakhir berakhir di {expected_start}s, harusnya {duration}s")


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    root = Path(sys.argv[1])
    files = sorted(root.rglob("prompt-video.md"))
    if not files:
        print(f"Tidak ada prompt-video.md di {root}")
        return 1
    errors: list[str] = []
    for f in files:
        check_file(f, errors)
    if errors:
        print("GAGAL:")
        for e in errors:
            print(" -", e)
        return 1
    print(f"Semua cek lolos. ({len(files)} berkas prompt-video diperiksa)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
