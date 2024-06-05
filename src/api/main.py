from fastapi import FastAPI


def create_app():
    app = FastAPI(title="A simple chat application", docs_url="/api/docs", debug=True)
    return app
