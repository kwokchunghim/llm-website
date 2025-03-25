.PHONY: run test build-index test_llm

run:
	@echo "Running Gradio app..."
	PYTHONPATH=$(PWD) python entrypoints/gradio_app.py

test:
	@echo "Running manual retrieval test..."
	PYTHONPATH=$(PWD) python entrypoints/test_retriever.py

build-index:
	@echo "Building FAISS index from JSON chunks..."
	PYTHONPATH=$(PWD) python entrypoints/build_index.py

test-llm:
	PYTHONPATH=$(PWD) python entrypoints/test_llm.py
