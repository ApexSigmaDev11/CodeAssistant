# main.py

import os
from dotenv import load_dotenv
from datetime import datetime
from utils.ollama_interface import ask_ollama

def load_system_prompt():
    try:
        with open("prompts/tutor_prompt.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return "You are a helpful programming tutor."

def log_interaction(prompt, response):
    os.makedirs("logs", exist_ok=True)
    filename = f"logs/session_{datetime.now().strftime('%Y%m%d')}.log"
    with open(filename, "a") as f:
        f.write(f"\n\n---\nUser:\n{prompt}\n\nAssistant:\n{response}\n")

def main():
    load_dotenv()
    model = os.getenv("OLLAMA_MODEL", "deepseek-coder:6.7b")
    system_prompt = load_system_prompt()

    print("🤖 Code Assistant: AI Tutor Mode Activated")
    print("Type 'exit' to end the session.\n")

    while True:
        user_input = input("💬 What do you want to learn today?\n> ")
        if user_input.strip().lower() in ["exit", "quit"]:
            print("📚 Session ended. See you next time!")
            break

        response = ask_ollama(model, user_input, system_prompt)
        print(f"\n🧠 Assistant:\n{response}")
        log_interaction(user_input, response)

if __name__ == "__main__":
    main()
