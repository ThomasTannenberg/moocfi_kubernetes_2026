import os
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

#standard port 3000
PORT = int(os.getenv("PORT", "3000"))


@asynccontextmanager
async def lifespan(app: FastAPI):
    print(f"Server started in port {PORT}", flush=True)
    yield


def register_routes(app: FastAPI) -> None:
    @app.get("/", response_class=PlainTextResponse)
    def root() -> str:
        return "Todo app"


def create_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)
    register_routes(app)
    return app


def main() -> None:
    uvicorn.run(app, host="0.0.0.0", port=PORT)


app = create_app()


if __name__ == "__main__":
    main()