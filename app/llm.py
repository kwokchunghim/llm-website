import os

from dotenv import load_dotenv
from groq import Groq

from app.config import GROQ_MODEL, TEMPERATURE
from app.prompts import SYSTEM_PROMPT, build_user_prompt

# Load environment variables from .env
load_dotenv()

# Create Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def query_llm(question, context_chunks):
    user_prompt = build_user_prompt(question, context_chunks)

    chat_completion = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
        temperature=TEMPERATURE,
        max_completion_tokens=1024,
        top_p=1,
        stop=None,
        stream=False,
    )

    return chat_completion.choices[0].message.content
