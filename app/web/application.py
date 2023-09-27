from app.web.api.router import (
    register_api_routers,
)
from fastapi import FastAPI
from fastapi.responses import UJSONResponse


def get_app() -> FastAPI:
    """
    Get FastAPI application.

    This is the main constructor of an application.

    :return: application.
    """

    app = FastAPI(
        title="Finance service",
        openapi_url="/openapi.json",
        swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"},
        default_response_class=UJSONResponse,
    )

    register_api_routers(app)

    return app
