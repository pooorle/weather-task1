from abc import ABCMeta

ENVIRONMENT: str = "Test"

SERVER_HOST: str = "0.0.0.0"
SERVER_PORT: int = 9090

WORKERS_COUNTS: int = 1

DEBUG: bool = True
RELOAD: bool = True

class BaseSettings(metaclass=ABCMeta):
    pass


APP_NAME: str = "service"

VERSION: str = ".version.json"

API_URL = "https://api.openweathermap.org/data/2.5/"
API_KEY = 'fb39dea90e5db51f15664d321d6f1e28'
