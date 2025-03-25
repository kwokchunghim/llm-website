from sentence_transformers import SentenceTransformer

from app.config import EMBEDDING_MODEL

model = SentenceTransformer(EMBEDDING_MODEL)


def embed_texts(texts):
    # Add instruction for better retrieval performance
    formatted = [f"Represent this document for retrieval: {t}" for t in texts]
    return model.encode(formatted, convert_to_tensor=True).cpu().numpy()
