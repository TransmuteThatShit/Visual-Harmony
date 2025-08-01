def detect_loopable_segments(lines, min_repeats=2, bar_length=None, timing_tolerance=0.1):
    """
    Tag lines as 'loopable' if they repeat at least `min_repeats` times.
    Optionally check if their length matches bar_length (in seconds) within timing_tolerance.
    Marks each detected line with a 'loopable' tag.
    Returns the modified lines list.
    """
    text_map = {}
    for line in lines:
        key = line["text"].strip().lower()
        text_map.setdefault(key, []).append(line)

    for key, occurrences in text_map.items():
        if len(occurrences) >= min_repeats:
            for occ in occurrences:
                if bar_length is None or abs((occ["end"] - occ["start"]) - bar_length) <= timing_tolerance:
                    tags = occ.get("tags", [])
                    if "loopable" not in tags:
                        tags.append("loopable")
                        occ["tags"] = tags
    return lines