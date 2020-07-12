FROM python:3.6.9-slim

WORKDIR /usr/src/app

COPY . .

RUN pip install pytest

ENTRYPOINT ["python3",  "jsoncounter.py"]
