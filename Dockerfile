FROM python:3.9.18-slim-bullseye

COPY Pipfile .
COPY Pipfile.lock .
RUN python -m pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

RUN mkdir -p /opt/genepatt/
COPY src/ /opt/genepatt/

WORKDIR /opt/genepatt/
