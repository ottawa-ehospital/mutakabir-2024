FROM python:3.9.18-slim-bullseye

WORKDIR /code

COPY models /code/models
COPY api /code/api
COPY main.py /code/main.py
COPY Procfile /code/Procfile
COPY model.toml /code/model.toml
COPY heroku.yml /code/heroku.yml
COPY requirements.txt /code/requirements.txt

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
