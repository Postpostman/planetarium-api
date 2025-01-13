FROM python:3.12-slim

LABEL maintainer="roman.vynnytskyi.tt@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /planetarium-api

COPY requirements.txt /planetarium-api/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /planetarium-api/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
