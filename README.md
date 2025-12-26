# 🧠 Local Chat Agent (Ollama + Python)

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-black)](https://ollama.com)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success.svg)]

A **local AI chat agent** built using **Python**, **uv**, and **Ollama**, leveraging an **OpenAI-compatible API** to run large language models entirely on your local machine.

This project serves as a **foundation for Agentic AI systems**, designed for **hackathons, learning, and portfolio demonstration** — with zero cloud dependency.

---

## 🚀 Why This Project Matters

- 💻 Runs **100% offline** (privacy-friendly, cost-free)
- 🤖 Demonstrates **Agentic AI fundamentals**
- 🔌 Uses **OpenAI-compatible interfaces**
- 🧪 Ideal for **hackathons, experiments, and learning**
- 📂 Clean, production-ready project structure

---

## ✨ Features

- ✅ Interactive command-line chat agent
- ✅ Local LLM inference using Ollama
- ✅ LLaMA 3 (8B) model support
- ✅ Python 3.10 with isolated environment (`uv`)
- ✅ Extensible design for memory, tools, and RAG
- ✅ No API keys or cloud costs

---

## 🛠 Tech Stack

| Layer         | Technology            |
| ------------- | --------------------- |
| Language      | Python 3.10           |
| Environment   | uv                    |
| LLM Runtime   | Ollama                |
| Model         | LLaMA 3 (8B)          |
| API Interface | OpenAI-compatible SDK |
| Platform      | macOS / Linux         |

---

## 📁 Project Structure

1_miniprojects/
│
├── 1_LocalChatAgent.py # Main chat agent
├── .venv/ # uv virtual environment
├── .gitignore
└── README.md

yaml
Copy code

---

## ⚙️ Prerequisites

- Python **3.10**
- `uv`
- `ollama`

### Install Ollama

```bash
brew install ollama
or download from
👉 https://ollama.com

🧠 Setup & Installation
1️⃣ Clone the repository
bash
Copy code
git clone (https://github.com/rajeshm20/agentic_ai_learning.git)
cd 1_miniprojects
2️⃣ Create virtual environment
bash
Copy code
uv venv
source .venv/bin/activate
3️⃣ Install dependencies
bash
Copy code
uv add openai
4️⃣ Pull LLM model
bash
Copy code
ollama pull llama3:8b
Verify:

bash
Copy code
ollama list
5️⃣ Start Ollama server
bash
Copy code
ollama serve
(Keep this running in a separate terminal)

▶️ Run the Chat Agent
bash
Copy code
uv run python 1_LocalChatAgent.py
Example:

vbnet
Copy code
Ask a question (type 'exit' to quit): Who is Elon Musk?
Assistant: Elon Musk is a technology entrepreneur known for...
Type exit to quit.

🧪 Sample Code
python
Copy code
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)
This uses Ollama’s OpenAI-compatible API, making it easy to swap between local and cloud models.

🖼 Screenshots / Demo
📌 Add screenshots or a GIF demo here

Example ideas:

Terminal chat interaction

Ollama model running locally

Project folder structure

text
Copy code
screenshots/
├── chat-demo.png
├── ollama-running.png
🏆 Hackathon Submission Notes
✔ Fully offline AI agent

✔ Zero cloud cost

✔ Privacy-first design

✔ Easily extensible to multi-agent workflows

✔ Suitable for real-world edge AI use cases

👨‍💼 Portfolio / Recruiter Highlights
Demonstrates local LLM orchestration

Shows understanding of OpenAI-compatible APIs

Clean Python environment management (uv)

Strong foundation for:

Agentic AI

RAG systems

Tool-augmented agents

Edge AI applications

🚀 Future Enhancements
🧠 Conversation memory

⚡ Streaming responses

🔧 Tool / function calling

📂 Local document RAG

🧩 Multi-agent orchestration

🌐 Web UI (FastAPI / Streamlit)


📜 License

MIT License — free to use, modify, and build upon.


🙌 Acknowledgements

Ollama Team

Meta LLaMA

OpenAI SDK (compatibility laye

```
