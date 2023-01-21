FROM docker.io/python:3.10-slim

WORKDIR /opt/bot

COPY requirements.txt /opt/bot/requirements.txt
RUN pip3 install -r /opt/bot/requirements.txt

COPY . .

ENTRYPOINT ["python3", "main.py"]
