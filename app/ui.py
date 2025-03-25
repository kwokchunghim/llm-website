import gradio as gr

from app.config import DATA_PATH, GRADIO_DESCRIPTION, GRADIO_EXAMPLES
from app.llm import query_llm
from app.retriever import RAGRetriever

# Initialize retriever once
retriever = RAGRetriever(DATA_PATH)


def chat(query, history):
    chunks = retriever.retrieve(query)
    response = query_llm(query, chunks)
    if "I'm not sure" in response or "no context" in response:
        return "I'm not sure about that — my training data doesn't include this information."
    return response


def build_gradio_app():
    with gr.Blocks() as demo:
        gr.HTML("""
            <div style="
                text-align: center;
                margin-bottom: 20px;
                padding: 10px 0;
                font-size: 1.25rem;
                line-height: 1.6;
            ">
                <h1 style="font-size: 2rem; margin-bottom: 0.5rem;">Tony Kwok's Personal AI Chatbot</h1>
                <p>Ask me anything about Tony’s work, experience, and projects.</p>
                <p style="font-size: 1.1rem;">
                    <a href="https://github.com/kwokchunghim" target="_blank">GitHub</a> |
                    <a href="https://linkedin.com/in/tonykwokch/" target="_blank">LinkedIn</a>
                </p>
            </div>
        """)


        gr.ChatInterface(
            fn=chat,
            title=None,  # Set to None since we’re using a custom header
            description=GRADIO_DESCRIPTION,
            examples=GRADIO_EXAMPLES,
        )

    return demo
