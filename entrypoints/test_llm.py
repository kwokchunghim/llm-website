from app.llm import query_llm
from app.retriever import RAGRetriever


def main():
    query = "Where did Tony study?"

    retriever = RAGRetriever("data/cv_chunks.json")
    chunks = retriever.retrieve(query)

    print("\nRetrieved Context:")
    for i, chunk in enumerate(chunks):
        print(f"{i+1}. {chunk['content']}")

    print("\nLLM Response:")
    response = query_llm(query, chunks)
    print(response)


if __name__ == "__main__":
    main()
