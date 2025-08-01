import os
from src.exporters import export_srt, export_vtt, export_lrc, export_csv, export_txt, export_json

def sample_lines():
    return [
        {"id": "line_1", "start": 0.5, "end": 3.2, "words": ["Hello", "world"], "text": "Hello world", "tags": ["root"]},
        {"id": "line_2", "start": 3.3, "end": 7.8, "words": ["Second", "line"], "text": "Second line", "tags": []}
    ]

def test_export_srt(tmp_path):
    path = tmp_path / "out.srt"
    export_srt(sample_lines(), path)
    assert path.read_text().startswith("1")

def test_export_vtt(tmp_path):
    path = tmp_path / "out.vtt"
    export_vtt(sample_lines(), path)
    assert "WEBVTT" in path.read_text()

def test_export_lrc(tmp_path):
    path = tmp_path / "out.lrc"
    export_lrc(sample_lines(), path)
    assert "[" in path.read_text()

def test_export_csv(tmp_path):
    path = tmp_path / "out.csv"
    export_csv(sample_lines(), path)
    assert "Start,End" in path.read_text()

def test_export_txt(tmp_path):
    path = tmp_path / "out.txt"
    export_txt(sample_lines(), path)
    assert "Hello world" in path.read_text()

def test_export_json(tmp_path):
    path = tmp_path / "out.json"
    export_json(sample_lines(), path)
    assert "line_1" in path.read_text()