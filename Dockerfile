FROM python:3.11-slim-bullseye

RUN pip install --upgrade pip

RUN pip install poetry==1.5.1

RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock /code/service/
WORKDIR /code/service

RUN poetry install

COPY . /code/service/

COPY settings /code/service/settings

RUN poetry install

ENV CITY=Kyiv

EXPOSE 9090

CMD ["/usr/local/bin/python", "__main__.py"]
