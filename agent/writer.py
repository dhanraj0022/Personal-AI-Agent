from agent.llm import call_llm
import os

def write_markdown(prompt, filename):
    system_prompt = "Write clean structured markdown."

    content = call_llm(system_prompt, prompt)

    os.makedirs("outputs", exist_ok=True)

    with open(f"outputs/{filename}", "w", encoding="utf-8") as f:
        f.write(content)

    return filename
