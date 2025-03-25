import os

from dotenv import load_dotenv

load_dotenv()  # This loads variables from .env

# API keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# LLM Model settings
GROQ_MODEL = "llama-3.3-70b-versatile"
TEMPERATURE = 0.3
TOP_K_RETRIEVAL = 20

# Embedding model
EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"

# Data paths
DATA_PATH = "data/cv_chunks_flattened.json"


# Gradio
GRADIO_DESCRIPTION = (
    "<div style='font-size: 1.1rem; line-height: 1.6;'>"
    "Hi there! I'm an interactive RAG-powered chatbot built on Tony Kwok's personal portfolio. "
    "Ask me anything about Tony — his experience, skills, projects, or education — and I'll do my best to answer. "
    "<br><br>"
    "<strong>Disclaimer:</strong> This chatbot is powered by an LLM and may occasionally produce incorrect or outdated information. "
    "If you need one-hundred percent accurate details, please refer to Tony’s official CV or get in touch at chkwok730@gmail.com directly."
    "</div>"
)

GRADIO_EXAMPLES = [
    "What is Tony's current role?",
    "Tell me about his recent ML projects",
    "What are his strongest skills?",
    "Where did Tony go to university?",
]