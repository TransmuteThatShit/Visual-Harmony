def parse_whisper_json(whisper_result):
    """Convert Whisper output to segment array with word-level timing."""
    segments = []
    for seg in whisper_result['segments']:
        for word in seg.get('words', []):
            segments.append({
                "start": word.get("start", seg["start"]),
                "end": word.get("end", seg["end"]),
                "text": word["word"],
                "confidence": word.get("probability", 1.0)
            })
    return segments