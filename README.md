# Visual-Harmony Lyric Sync & Vocal Processing Pipeline

A modular pipeline for automatic lyric transcription, tagging, multi-format export, and visual generation using AI.

## Features

- Whisper-powered transcription (word-level timing, multi-format input)
- Segment merging, keyword/tagging (chakra, emotion, looping, etc)
- Moises-style JSON output for downstream applications
- Multi-format lyric export: TXT, CSV, SRT, VTT, LRC, JSON
- Batch processing via CLI
- Automated prompt generation for Stability AI image creation
- Visual harmony integration with lyric themes
- Robust logging and error handling

## Usage

```bash
python 0.py input.mp3 output_dir api_key1,api_key2,...
```

## Dev Checklist

See `_personal_instructions` for full feature roadmap.

## Module Structure

- `0.py` - Main pipeline
- `audio_utils.py` - Audio extraction and duration
- `lyrics_utils.py` - Whisper transcription, theme extraction
- `generate_visuals.py` - Prompt creation, visual generation
- `stability_api_manager.py` - API key management and fallback

## TODO

- Implement all `NotImplementedError` stubs
- Add segment merging, tagging, and multi-format export modules
- Expand README with CLI/config instructions and sample files
- Write unit tests for each module

## Troubleshooting

- Check logs for errors and progress
- Validate output files in DAW, video or karaoke apps
- Ensure API keys are valid and .env/config is loaded

---

TransmuteThatShit © 2025