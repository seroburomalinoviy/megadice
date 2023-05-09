FROM python:3.9-slim-buster

RUN mkdir -p /root/MegaDice

WORKDIR /root/MegaDice

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "bot.py"]