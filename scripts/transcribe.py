"""Transcribe audio/video with Whisper and export word-level JSON, SRT, and TXT."""

import argparse
import json
from pathlib import Path
import whisper


def format_srt_time(seconds: float) -> str:
    ms = int(round(seconds * 1000))
    hrs, rem = divmod(ms, 3_600_000)
    mins, rem = divmod(rem, 60_000)
    secs, millis = divmod(rem, 1000)
    return f"{hrs:02d}:{mins:02d}:{secs:02d},{millis:03d}"


def main() -> None:
    parser = argparse.ArgumentParser(description="Transcribe media to word-level JSON + SRT.")
    parser.add_argument("input", help="Path to audio or video file (e.g. raw/voice.mp3)")
    parser.add_argument("--model", default="small", help="Whisper model (tiny, base, small, medium, large)")
    parser.add_argument("--language", default="pt", help="Language code (e.g. pt, en)")
    parser.add_argument("--out-dir", default="transcripts", help="Output directory")
    args = parser.parse_args()

    src = Path(args.input)
    if not src.exists():
        raise SystemExit(f"Arquivo não encontrado: {src}")

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = src.stem

    model = whisper.load_model(args.model)
    result = model.transcribe(str(src), language=args.language, word_timestamps=True, verbose=False)

    words = []
    srt_lines = []
    for idx, seg in enumerate(result.get("segments", []), start=1):
        srt_lines.append(f"{idx}\n{format_srt_time(seg['start'])} --> {format_srt_time(seg['end'])}\n{seg['text'].strip()}\n")
        for w in seg.get("words", []):
            words.append({"word": w["word"].strip(), "start": round(w["start"], 3), "end": round(w["end"], 3)})

    payload = {
        "language": result.get("language", args.language),
        "text": result.get("text", "").strip(),
        "segments": [
            {"id": s["id"], "start": round(s["start"], 3), "end": round(s["end"], 3), "text": s["text"].strip()}
            for s in result.get("segments", [])
        ],
        "words": words,
    }

    (out_dir / f"{stem}.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    (out_dir / f"{stem}.srt").write_text("\n".join(srt_lines), encoding="utf-8")
    (out_dir / f"{stem}.txt").write_text(payload["text"] + "\n", encoding="utf-8")
    print(f"OK: {out_dir / stem}.json ({len(words)} palavras), .srt, .txt")


if __name__ == "__main__":
    main()
