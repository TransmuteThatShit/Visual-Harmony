import argparse
import os
import sys
from pathlib import Path

# Import your main pipeline function
from 0 import main as run_pipeline  # If 0.py is in repo root. Otherwise, update import.

def parse_args():
    parser = argparse.ArgumentParser(
        description="Visual-Harmony Lyric Sync & Vocal Processing CLI"
    )
    parser.add_argument("input", help="Input audio file or folder")
    parser.add_argument("output_dir", help="Output directory")
    parser.add_argument("--api-keys", required=True, help="Comma-separated Stability API keys")
    parser.add_argument("--filter-threshold", type=float, default=0.5, help="Confidence filter threshold")
    parser.add_argument("--presets", nargs="*", help="Tagging preset(s) to use")
    parser.add_argument("--export-formats", nargs="*", default=["txt", "csv", "json"], 
                        help="Export formats: txt, csv, json, srt, vtt, lrc, elrc")
    parser.add_argument("--config", help="Path to config file (optional)")
    parser.add_argument("--batch", action="store_true", help="Process all audio files in input folder")
    return parser.parse_args()

def get_audio_files(path):
    audio_exts = [".wav", ".mp3", ".m4a", ".mp4"]
    if os.path.isfile(path):
        return [path]
    elif os.path.isdir(path):
        files = []
        for p in Path(path).glob("**/*"):
            if p.suffix.lower() in audio_exts:
                files.append(str(p))
        return files
    else:
        print(f"Input path {path} not found.")
        sys.exit(1)

def main():
    args = parse_args()
    input_files = get_audio_files(args.input) if args.batch else [args.input]
    os.makedirs(args.output_dir, exist_ok=True)
    for input_file in input_files:
        print(f"Processing {input_file}...")
        run_pipeline(
            input_file=input_file,
            output_dir=args.output_dir,
            api_keys=args.api_keys.split(","),
            # You can extend run_pipeline to accept presets, export_formats, filter_threshold, etc.
        )
    print("All files processed!")

if __name__ == "__main__":
    main()