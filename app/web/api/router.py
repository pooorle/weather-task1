import fastapi
from app.web.api import weather


def register_api_routers(app: fastapi.FastAPI) -> None:
    """Register routers."""
    app.include_router(weather.router, prefix="/api/v1/weather")
