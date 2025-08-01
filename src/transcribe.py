import whisper
import os

def transcribe_audio(audio_path):
    """Transcribe audio to Whisper JSON output."""
    model = whisper.load_model("base")
    result = model.transcribe(audio_path, word_timestamps=True)
    return result  # Dict with 'segments', 'text', etc.