import logging

import fastapi
from fastapi import Header, HTTPException

from app.services.weather import Weather
from app.web.constants import X_TOKEN

router = fastapi.APIRouter()

logger = logging.getLogger(__name__)


@router.get(
    "",
    response_model_exclude_none=True,
    description="Get weather",
)
async def get_weather(
    pm_service: Weather = fastapi.Depends(),
):
    return await pm_service.get_weather()


@router.get(
    "/{day}",
    response_model_exclude_none=True,
    description="Get weather by the day",
)
async def get_weather_by_date(
    day: str, pm_service: Weather = fastapi.Depends(), x_token: str = Header(None)
):
    if x_token != X_TOKEN:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return await pm_service.get_weather_by_day(day)
