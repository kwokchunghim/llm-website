from app.ui import build_gradio_app


def main():
    app = build_gradio_app()
    app.launch()


if __name__ == "__main__":
    main()
