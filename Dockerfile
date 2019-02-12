FROM python:3.6-slim

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code
RUN pip install -r requirements.txt
COPY src/ /code

ENTRYPOINT ["python3", "app/manage.py", "runserver", "0.0.0.0:8000"]
