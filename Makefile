PROJECT_DIR=$(shell pwd)

SERVICE_NAME = forecast-app

SERVICES_DIR=$(PROJECT_DIR)

SERVICE_SERVICE_DIR=$(SERVICES_DIR)
SERVICE_ENV_DIR?=$(SERVICE_SERVICE_DIR)/.venv
SERVICE_PYTHON?=$(SERVICE_ENV_DIR)/bin/python3
SERVICE_PYTHON_ACTIVATE=$(SERVICE_ENV_DIR)/bin/activate

SERVICE_APP_DIR=$(SERVICE_SERVICE_DIR)/app

.PHONY: service_flake8 service_mypy service_black service_run service_run_console

service_check_code: service_black service_flake8 service_mypy

service_install_poetry:
	python3 -m venv .venv && \
	cd $(SERVICE_SERVICE_DIR) && \
	source $(SERVICE_PYTHON_ACTIVATE) && \
	poetry install

service_install_req:
	python3 -m venv .venv && \
	source $(SERVICE_ENV_DIR)/bin/activate && \
	pip3 install -r requirements.txt

service_black:
	cd $(SERVICE_SERVICE_DIR) && \
	poetry run black $(SERVICE_APP_DIR)

service_flake8:
	cd $(SERVICE_SERVICE_DIR) && \
	poetry run flake8 $(SERVICE_APP_DIR)

service_mypy:
	cd $(SERVICE_SERVICE_DIR) && \
	poetry run mypy $(SERVICE_APP_DIR)

service_run:
	ls -la && \
	source $(SERVICE_ENV_DIR)/bin/activate && \
	SETTINGS_MODULE=local $(SERVICE_PYTHON) $(SERVICE_SERVICE_DIR)/__main__.py

service_docker_run:
	ls -la && \
	docker build -t service . && \
	docker run -p 9090:9090 service

service_docker_compose:
	ls -la && \
	docker-compose up --build