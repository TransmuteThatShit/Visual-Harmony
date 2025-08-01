import os
import json

def export_all_formats(lines, output_dir):
    export_txt(lines, os.path.join(output_dir, "lyrics.txt"))
    export_csv(lines, os.path.join(output_dir, "regions.csv"))
    export_srt(lines, os.path.join(output_dir, "lyrics.srt"))
    export_vtt(lines, os.path.join(output_dir, "lyrics.vtt"))
    export_lrc(lines, os.path.join(output_dir, "lyrics.lrc"))
    export_json(lines, os.path.join(output_dir, "lyrics.json"))
    export_moises_json(lines, os.path.join(output_dir, "lyrics.moises.json"))

def export_txt(lines, path):
    with open(path, "w") as f:
        for l in lines:
            f.write(f"{l['start']:.2f}-{l['end']:.2f}: {l['text']}\n")

def export_csv(lines, path):
    with open(path, "w") as f:
        f.write("Start,End,Text,ID,Tags\n")
        for l in lines:
            tags = ",".join(l.get("tags", []))
            f.write(f"{l['start']},{l['end']},\"{l['text']}\",{l['id']},\"{tags}\"\n")

def export_srt(lines, path):
    def ts(s): return f"{int(s//3600):02}:{int((s%3600)//60):02}:{int(s%60):02},{int((s%1)*1000):03}"
    with open(path, "w") as f:
        for idx, l in enumerate(lines, 1):
            f.write(f"{idx}\n{ts(l['start'])} --> {ts(l['end'])}\n{l['text']}\n\n")

def export_vtt(lines, path):
    def ts(s): return f"{int(s//3600):02}:{int((s%3600)//60):02}:{int(s%60):02}.{int((s%1)*1000):03}"
    with open(path, "w") as f:
        f.write("WEBVTT\n\n")
        for l in lines:
            f.write(f"{ts(l['start'])} --> {ts(l['end'])}\n{l['text']}\n\n")

def export_lrc(lines, path):
    def ts(s): return f"[{int(s//60):02}:{int(s%60):02}.{int((s%1)*100):02}]"
    with open(path, "w") as f:
        for l in lines:
            f.write(f"{ts(l['start'])}{l['text']}\n")

def export_json(lines, path):
    with open(path, "w") as f:
        json.dump(lines, f, indent=2)

def export_moises_json(lines, path):
    segments = []
    for line in lines:
        segment = {
            "start": line["start"],
            "end": line["end"],
            "text": line["text"],
            "words": [
                # If word timing info exists, include it; otherwise, just word text
                {"word": w, "start": ws, "end": we}
                for w, ws, we in zip(
                    line.get("words", []),
                    line.get("word_starts", [line["start"]]*len(line.get("words", []))),
                    line.get("word_ends", [line["end"]]*len(line.get("words", [])))
                )
            ],
            "confidence": line.get("confidence", 1.0),
            "tags": line.get("tags", [])
        }
        segments.append(segment)
    with open(path, "w") as f:
        json.dump({"segments": segments}, f, indent=2)