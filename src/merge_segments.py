def merge_segments(segments):
    """Merge word segments into lyric lines with start/end times and unique IDs."""
    lines = []
    current_line = []
    line_start = None
    for i, seg in enumerate(segments):
        if line_start is None:
            line_start = seg["start"]
        current_line.append(seg["text"])
        # Simple rule: new line on punctuation or every N words
        if seg["text"].endswith(('.', '!', '?')) or len(current_line) >= 10:
            lines.append({
                "id": f"line_{len(lines)+1}",
                "start": line_start,
                "end": seg["end"],
                "words": current_line.copy(),
                "text": " ".join(current_line)
            })
            current_line = []
            line_start = None
    if current_line:
        lines.append({
            "id": f"line_{len(lines)+1}",
            "start": line_start,
            "end": segments[-1]["end"],
            "words": current_line.copy(),
            "text": " ".join(current_line)
        })
    return lines