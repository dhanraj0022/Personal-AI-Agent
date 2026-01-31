📘 Personal AI Agent — Local LLM + GitHub Automation
🚀 Overview

This project is a local-first personal AI agent system designed to:

Run fully offline using Ollama

Use task-specific LLM models

Generate structured Markdown (.md) knowledge files

Maintain clean GitHub version control

Support future RAG (Retrieval-Augmented Generation) workflows

The system is built with modular agent architecture, making it extensible for learning, DSA tracking, AI study notes, and automated documentation.

🧠 Core Objectives

✅ Local LLM execution (no API costs)

✅ Clear separation of responsibilities (router, writer, orchestrator)

✅ Git-safe automation (no venv or secrets committed)

✅ Markdown-first knowledge storage

✅ Designed for long-term learning tracking

📁 Project Structure
Personal-AI-Agent/
│
├── agent/
│   ├── orchestrator.py     # Main controller (task flow)
│   ├── llm.py              # Ollama LLM interface
│   ├── writer.py           # Markdown generation
│   ├── router.py           # Task routing (future use)
│   ├── github.py           # Git automation (optional)
│   └── __init__.py
│
├── outputs/
│   └── notes/              # Generated .md files
│
├── config.yaml             # Model + system configuration
├── main.py                 # Application entry point
│
├── commit.bat              # One-command Git automation
├── .gitignore              # Prevents venv, cache, secrets
├── requirements.txt
├── README.md
│
└── venv/                   # Local only (never pushed)

⚙️ Technologies Used

Python 3.11

Ollama (local LLM runtime)

Phi-3 Mini (lightweight low-memory model)

Nomic Embed Text (for future RAG)

Git + GitHub

Markdown-based knowledge storage

🧩 Installed Ollama Models
Purpose	Model
General reasoning	phi3:mini
Code generation	deepseek-coder:6.7b
Embeddings	nomic-embed-text

⚠️ Large models like LLaMA/Gemma require higher RAM and may not run on low-memory systems.

🛠 Setup Steps (Completed)
1️⃣ Python Environment

Installed Python 3.11.x

Created virtual environment:

python -m venv venv
venv\Scripts\activate

2️⃣ Dependency Installation
pip install -r requirements.txt


Key libraries:

ollama

pyyaml

gitpython

3️⃣ Ollama Setup

Install Ollama and pull required models:

ollama pull phi3:mini
ollama pull nomic-embed-text


Start Ollama server:

ollama serve


Ollama runs locally on:

http://localhost:11434

4️⃣ Configuration File (config.yaml)
model:
  default: phi3:mini

github:
  enabled: false


GitHub automation can be enabled later.

5️⃣ Running the Application
python main.py


This will:

Call the local LLM

Generate markdown content

Save files into structured folders

Avoid pushing venv or system files

🔁 Git Automation (Optional)

A batch script simplifies Git usage:

commit.bat
@echo off
setlocal EnableDelayedExpansion

if "%~1"=="" (
    set "msg=AI update"
) else (
    set "msg=%~1"
)

git add .
git commit -m "%msg%"
git push


Usage:

.\commit.bat "Add DSA sliding window notes"


✔ Clean
✔ Safe
✔ Repeatable

🔒 Git Safety

The following are ignored permanently:

venv/
__pycache__/
.env
*.pyc


This ensures:

No environment files pushed

No secrets leaked

Clean repository history

🧠 Design Philosophy
Separation of Concerns
Component	Responsibility
orchestrator	Workflow control
llm	Model interaction
writer	File creation
router	Task-based routing
github	Optional push automation

This mirrors production-grade backend design.

🔮 Planned Enhancements

 RAG using embeddings

 Date-based progress retrieval

 Multi-model routing (DSA vs AI vs summaries)

 Google Drive integration

 Auto-generated commit messages

 Daily learning tracker

 Semantic search over markdown files

🧑‍💻 Author

Dhanraj Singh
Built as a long-term learning companion and AI experimentation platform.

✅ Status

🟢 Working
🟢 Local LLM operational
🟢 GitHub integrated
🟢 Ready for expansion
