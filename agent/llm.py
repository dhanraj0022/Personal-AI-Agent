import ollama
import yaml
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

def call_llm(system_prompt, user_prompt):
    config_path = BASE_DIR / "config.yaml"

    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    model = config["model"]["default"]

    response = ollama.chat(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )

    return response["message"]["content"]
