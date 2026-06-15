import os
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Standard port 3000
PORT = int(os.getenv("PORT", "3000"))


@asynccontextmanager
async def lifespan(app: FastAPI):
    print(f"Server started in port {PORT}", flush=True)
    yield


def register_routes(app: FastAPI) -> None:
    @app.get("/", response_class=HTMLResponse)
    def root() -> str:
        return """
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <title>Todo App</title>
            <style>
              body {
                font-family: Arial, sans-serif;
                background: #f4f4f5;
                margin: 0;
                padding: 40px;
              }

              .container {
                max-width: 700px;
                margin: 0 auto;
                background: white;
                padding: 32px;
                border-radius: 12px;
                box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
              }

              h1 {
                margin-top: 0;
              }

              .subtitle {
                color: #555;
              }

              .footer {
                margin-top: 32px;
                font-size: 14px;
                color: #777;
              }
            </style>
          </head>
          <body>
            <main class="container">
              <h1>Todo App</h1>
              <p class="subtitle">Welcome to the Todo App.</p>
              <p>This is the project application for the mooc.fi DevOps with Kubernetes 2026 course.</p>
              <p class="footer">Running inside Kubernetes.</p>
            </main>
          </body>
        </html>
        """


def create_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)
    register_routes(app)
    return app


def main() -> None:
    uvicorn.run(app, host="0.0.0.0", port=PORT)


app = create_app()


if __name__ == "__main__":
    main()