"""FFmpeg helpers for faceless Vox/Explained prep: trim silence and normalize to -14 LUFS."""

import argparse
from pathlib import Path
import subprocess


def run_ffmpeg(cmd: list[str]) -> None:
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        raise SystemExit(f"FFmpeg falhou:\n{proc.stderr[-1000:]}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Prepare voiceover/video with FFmpeg.")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_clean = sub.add_parser("clean-voice", help="Extract/clean voiceover: remove long silences and normalize -14 LUFS")
    p_clean.add_argument("input", help="Input audio/video (e.g. raw/narracao.mp3)")
    p_clean.add_argument("-o", "--output", default="audio/voiceover.wav", help="Output WAV path")
    p_clean.add_argument("--threshold", default="-35dB", help="Silence threshold (default: -35dB)")
    p_clean.add_argument("--min-silence", type=float, default=0.45, help="Max silence duration in seconds (default: 0.45)")

    p_broll = sub.add_parser("prep-broll", help="Convert b-roll to muted 1080p 30fps MP4 ready for HyperFrames")
    p_broll.add_argument("input", help="Input video file")
    p_broll.add_argument("-o", "--output", required=True, help="Output MP4 path in assets/broll/")

    args = parser.parse_args()
    src = Path(args.input)
    if not src.exists():
        raise SystemExit(f"Arquivo não encontrado: {src}")

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)

    if args.cmd == "clean-voice":
        # Remove silêncios longos mantendo ritmo natural e normaliza para YouTube (-14 LUFS).
        af = (
            f"silenceremove=start_periods=1:start_silence=0.1:start_threshold={args.threshold},"
            f"areverse,silenceremove=start_periods=1:start_silence=0.1:start_threshold={args.threshold},areverse,"
            f"silenceremove=stop_periods=-1:stop_duration={args.min_silence}:stop_threshold={args.threshold},"
            "loudnorm=I=-14:TP=-1.5:LRA=11"
        )
        run_ffmpeg(["ffmpeg", "-y", "-i", str(src), "-vn", "-af", af, "-ar", "48000", "-ac", "1", str(out)])
        print(f"OK: voz limpa e normalizada em {out}")

    elif args.cmd == "prep-broll":
        vf = "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=30,format=yuv420p"
        run_ffmpeg(["ffmpeg", "-y", "-i", str(src), "-an", "-vf", vf, "-c:v", "libx264", "-preset", "fast", "-crf", "18", str(out)])
        print(f"OK: b-roll preparado em {out}")


if __name__ == "__main__":
    main()
