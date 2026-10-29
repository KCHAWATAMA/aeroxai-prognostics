"""FastAPI entry point. Routes live in api/routes/; keep this file small."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from api import __doc__ as api_doc
from api.settings import get_settings

VERSION = "0.1.0"


class Health(BaseModel):
    status: str
    version: str
    env: str
    model_loaded: bool


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(title="AeroXAI Prognostics API", version=VERSION, description=api_doc or "")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origin_list,
        allow_methods=["GET", "POST"],
        allow_headers=["*"],
    )

    @app.get("/health")
    def health() -> Health:
        return Health(status="ok", version=VERSION, env=settings.env, model_loaded=False)

    return app


app = create_app()
