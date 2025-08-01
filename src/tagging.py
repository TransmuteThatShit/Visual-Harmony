PRESETS = {
    "chakra": ["root", "heart", "third eye", "crown"],
    "emotion": ["love", "sad", "joy", "anger"],
    "loop": ["repeat", "again", "forever"],
    "twin_flame": ["mirror", "union", "destiny", "soulmate"]
}

def tag_lyrics(lines, preset="default"):
    """Tag lines with keywords from preset."""
    tags = PRESETS.get(preset, [])
    for line in lines:
        line["tags"] = [tag for tag in tags if tag in line["text"].lower()]
    return lines