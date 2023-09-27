import logging
from datetime import datetime, date
import os

from cachetools.func import ttl_cache
import requests

from app.web.constants import TTL, ENV_CITY_NAME
from settings import API_URL, API_KEY

logger = logging.getLogger(__name__)


class Weather:
    def _get_weather_payload(self, data: dict):
        forecast = {
            "name": data.get("name", ""),
            "temperature": data.get("main", {}).get("temp"),
            "humidity": data.get("main", {}).get("humidity"),
            "description": data.get("weather", [])[0],
        }

        return forecast

    def _get_weather_by_day(self, data: dict, day: str):
        temperatures = list()
        day = date.fromisoformat(day)  # type: ignore
        for item in data["list"]:
            timestamp = item["dt"]
            temperature_kelvin = item["main"]["temp"]
            temperature_celsius = temperature_kelvin - 273.15
            datetime_utc = datetime.utcfromtimestamp(timestamp)

            if datetime_utc.date() == day:
                temperatures.append(
                    {
                        "datetime_utc": datetime_utc.strftime("%Y-%m-%d %H:%M:%S UTC"),
                        "temperature_celsius": temperature_celsius,
                    }
                )
        response_data = {"temperatures": temperatures}

        return response_data

    async def get_weather(self):
        city = os.environ.get(ENV_CITY_NAME)

        url = f"{API_URL}weather?q={city}&appid={API_KEY}"
        data = dict()

        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
            logger.info(f"Response payload: '{data}'")
        except Exception as e:
            print(f"An exception occurred: {e}")
            logger.warning(f"Request error to the url: '{url}'")

        forecast = self._get_weather_payload(data)
        return forecast

    @ttl_cache(maxsize=128, ttl=TTL)
    async def get_weather_by_day(self, day):
        city = os.environ.get(ENV_CITY_NAME)

        url = f"{API_URL}forecast?q={city}&appid={API_KEY}"
        data = dict()

        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
            logger.info(f"Response payload: '{data}'")
        except Exception as e:
            print(f"An exception occurred: {e}")
            logger.warning(f"Request error to the url: '{url}'")

        forecast = self._get_weather_by_day(data, day)
        return forecast
