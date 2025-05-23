# utils/ollama_interface.py

import requests

def ask_ollama(model: str, user_input: str, system_prompt: str = "") -> str:
    """
    Send a user prompt to Ollama and return the full response.
    """
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": model,
        "prompt": user_input,
        "system": system_prompt,
        "stream": False
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()["response"]
    except Exception as e:
        return f"[ERROR] Failed to connect to Ollama: {e}"
