def get_prompts(text):
    return {
        "TRANSLATE_SPANISH": f"Translate the following phrase into Spanish: {text}",
        "TRANSLATE_LATIN": f"Translate the following phrase into Latin: {text}",
        "TRANSLATE_FRENCH": f"Translate the following phrase into French: {text}"
    }

