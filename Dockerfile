FROM python:3.9

WORKDIR /code

COPY . /code

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]