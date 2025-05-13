from prompts import get_prompts
from ollama_client import query_ollama
from jinja2 import Template
import os

def main():
    model = "openhermes"
    user_input = input("Enter a phrase to translate: ").strip()

    prompts = get_prompts(user_input)
    responses = {}

    for key, prompt in prompts.items():
        print(f"→ Generating: {key}")
        responses[key] = query_ollama(model, prompt)

    with open("templates/demo_translation.html", "r") as f:
        template = Template(f.read())

    rendered = template.render(**responses)

    os.makedirs("output", exist_ok=True)
    with open("output/translation_output.html", "w") as out:
        out.write(rendered)

    print("\n✅ Translations saved to output/translation_output.html")

if __name__ == "__main__":
    main()

