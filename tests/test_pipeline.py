from src.transcribe import transcribe_audio
from src.parse_whisper import parse_whisper_json
from src.merge_segments import merge_segments
from src.tagging import tag_lyrics

def test_pipeline_mock(monkeypatch):
    # Monkeypatch transcribe_audio to return dummy Whisper output
    monkeypatch.setattr("src.transcribe.transcribe_audio", lambda x: {
        "segments": [
            {"start": 0.5, "end": 3.2, "words": [{"word": "Hello", "start": 0.5, "end": 1.0}, {"word": "world", "start": 1.1, "end": 3.2}]},
            {"start": 3.3, "end": 7.8, "words": [{"word": "Second", "start": 3.3, "end": 5.0}, {"word": "line", "start": 5.1, "end": 7.8}]}
        ]
    })
    whisper_json = transcribe_audio("dummy.wav")
    segments = parse_whisper_json(whisper_json)
    lines = merge_segments(segments)
    tagged = tag_lyrics(lines, preset="chakra")
    # There should be 2 lines with correct tags
    assert len(tagged) == 2
    assert any("root" in line["tags"] for line in tagged)