import requests
from markupsafe import escape

def query_ollama(model: str, prompt: str) -> str:
    try:
        response = requests.post("http://localhost:11434/api/generate", json={
            "model": model,
            "prompt": prompt,
            "stream": False
        })
        response.raise_for_status()
        return escape(response.json().get("response", "[No response]"))
    except Exception as e:
        return escape(f"[Error: {e}]")

