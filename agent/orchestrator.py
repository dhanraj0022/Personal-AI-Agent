from agent.router import route
from agent.writer import write_markdown
from agent.github import push
import yaml
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

def run(task_type, prompt, filename):
    config_path = BASE_DIR / "config.yaml"

    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    mode = route(task_type)

    if mode == "writer":
        write_markdown(prompt, filename)

    if config.get("github", {}).get("enabled", False):
        try:
            push(f"AI update: {filename}")
        except Exception as e:
            print("Git push skipped:", e)