# Don't Remove Credit @LokahBotUniverse
# Subscribe YouTube Channel For Amazing Bot @LokahBotUniverse
# Ask Doubt on telegram @LokahBotUniverse

FROM python:3.10.8-slim-bullseye

RUN apt update && apt upgrade -y
RUN apt install git -y
COPY requirements.txt /requirements.txt

RUN cd /
RUN pip3 install -U pip && pip3 install -U -r requirements.txt
RUN mkdir /LokahBotUniverse
WORKDIR /LokahBotUniverse
COPY . /LokahBotUniverse
CMD ["python", "bot.py"]
