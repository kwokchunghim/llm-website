from app.retriever import RAGRetriever


def main():
    retriever = RAGRetriever("data/cv_chunks.json")
    results = retriever.retrieve("What projects has Tony worked on?")
    print("\n✅ Retrieved Results:")
    for i, result in enumerate(results):
        print(f"{i+1}. {result['content']}\n")


if __name__ == "__main__":
    main()
