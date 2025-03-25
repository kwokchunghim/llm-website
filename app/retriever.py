import json

import faiss
import numpy as np

from app.config import TOP_K_RETRIEVAL
from app.embedder import embed_texts


class RAGRetriever:
    def __init__(self, json_path):
        self.data = self.load_data(json_path)
        self.texts = [item["content"] for item in self.data]
        self.embeddings = embed_texts(self.texts)
        self.index = faiss.IndexFlatL2(self.embeddings.shape[1])
        self.index.add(np.array(self.embeddings))

    def load_data(self, path):
        with open(path) as f:
            return json.load(f)

    def retrieve(self, query, k=TOP_K_RETRIEVAL):
        query_vector = embed_texts([query])[0].reshape(1, -1)
        distances, indices = self.index.search(np.array(query_vector), k)
        return [self.data[i] for i in indices[0]]
