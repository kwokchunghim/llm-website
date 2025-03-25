# 🧠 Tony Kwok — LLM-Powered Portfolio Chatbot

This project is a **personal portfolio website with a twist**: instead of a static site, you interact with an **LLM-powered chatbot** that knows everything about Tony Kwok's background, projects, experience, and skills — all powered by **RAG (Retrieval-Augmented Generation)**, **Groq**, and **Gradio**.

---

## 🚀 Features

- 💬 **Interactive chatbot UI** with Gradio
- 🧠 **RAG pipeline** using FAISS + BGE-small embeddings
- ⚡️ Inference through **Groq's blazing-fast hosted LLMs**
- 📄 Custom vector index built from structured JSON resume
- 🧪 Fully testable + clean project structure

---

## 🧰 Tech Stack

| Layer       | Tool/Lib                         |
|-------------|----------------------------------|
| UI          | [Gradio](https://www.gradio.app) |
| LLM         | [Groq](https://console.groq.com) |
| Embeddings  | `bge-small-en-v1.5`              |
| Retrieval   | FAISS                            |
| Language    | Python 3.10+                     |

---

## 📄 Repo Structure

```
llm-website/
├── app/                  → Core logic and components
│   ├── config.py         → Central config (paths, keys, constants)
│   ├── embedder.py       → Embedding model setup (BGE-small)
│   ├── retriever.py      → FAISS index + chunk retrieval
│   ├── llm.py            → Groq API interaction
│   ├── prompts.py        → Prompt templates and builders
│   └── ui.py             → Gradio interface builder
│
├── entrypoints/          → CLI + app launchers
│   ├── gradio_app.py     → Launch Gradio UI
│   ├── test_llm.py       → Manual RAG pipeline test
│   └── test_retriever.py → Manual retriever test
│
├── data/                 
│   └── cv_chunks_flattened.json  → Flattened JSON CV data
│
├── tests/                → Unit tests (optional)
│
├── .env                  → Environment variables (excluded from Git)
├── .gitignore
├── Makefile              → Developer commands (run, test, build)
├── requirements.txt      
├── requirements-dev.txt  → Dev-only dependencies
├── Dockerfile            → Build the Docker image
└── README.md             → Project overview (this file)
```
