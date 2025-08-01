def build_prompt_sequence(themes):
    """
    Builds a list of prompts for visuals based on lyric themes.
    """
    # TODO: implement prompt generation logic
    return [f"visualizing {theme}" for theme in themes]

def generate_visuals_from_prompts(prompt, output_dir, api_manager, suffix=""):
    """
    Calls Stability API manager for image generation.
    Returns path to saved image.
    """
    # TODO: implement image generation and saving
    raise NotImplementedError