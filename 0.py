import os
import sys
import time
import logging
import traceback
from audio_utils import extract_audio, get_audio_duration
from lyrics_utils import transcribe_audio, extract_themes_from_lyrics
from generate_visuals import build_prompt_sequence, generate_visuals_from_prompts
from stability_api_manager import StabilityAPIManager

def main(input_file, output_dir, api_keys):
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")
    summary = {}
    start_time = time.time()

    try:
        ext = os.path.splitext(input_file)[1].lower()
        audio_path = None
        if ext in [".wav", ".mp3", ".m4a"]:
            audio_path = input_file
        elif ext == ".mp4":
            audio_path = extract_audio(input_file, output_dir)
        else:
            logging.error(f"Unsupported file type: {ext}")
            sys.exit(1)
        logging.info(f"Audio file for processing: {audio_path}")

        duration = get_audio_duration(audio_path)
        summary["duration"] = duration

        t0 = time.time()
        transcript, confidence = transcribe_audio(audio_path)
        t1 = time.time()
        summary["transcription_time"] = t1 - t0
        summary["confidence"] = confidence
        logging.info(f"Transcription complete. Confidence: {confidence:.2f}")

        themes = extract_themes_from_lyrics(transcript)
        prompt_sequence = build_prompt_sequence(themes)
        logging.info(f"Lyric themes: {themes}")
        logging.info(f"Prompt sequence: {prompt_sequence}")

        api_manager = StabilityAPIManager(api_keys)
        image_paths = []
        for i, prompt in enumerate(prompt_sequence):
            try:
                img_path = generate_visuals_from_prompts(
                    prompt,
                    output_dir,
                    api_manager=api_manager,
                    suffix=f"{i+1}_{confidence:.2f}_{duration:.1f}s"
                )
                image_paths.append(img_path)
                logging.info(f"Generated image: {img_path} (API key: {api_manager.last_used_key})")
            except Exception as e:
                logging.error(f"Image generation failed for prompt: {prompt}")
                traceback.print_exc()
                continue
        summary["visuals"] = image_paths

        transcript_path = os.path.join(
            output_dir,
            f"transcript_{duration:.1f}s_conf{confidence:.2f}.txt"
        )
        with open(transcript_path, "w") as f:
            f.write(transcript)
        summary["transcript_path"] = transcript_path

        end_time = time.time()
        summary["total_time"] = end_time - start_time
        summary["input_file"] = input_file
        summary["output_dir"] = output_dir
        print("=== PIPELINE SUMMARY ===")
        print(summary)

    except Exception as e:
        logging.error("Pipeline failed.")
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_dir = sys.argv[2]
    api_keys = sys.argv[3].split(",")
    main(input_file, output_dir, api_keys)