from agent.orchestrator import run

prompt = """
Explain sliding window technique.
Include:
- definition
- example
- time complexity
"""

run(
    task_type="writer",
    prompt=prompt,
    filename="sliding_window.md"
)
