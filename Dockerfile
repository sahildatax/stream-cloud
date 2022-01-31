FROM python

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

ENV PORT = 8080
EXPOSE 8080

RUN python -m bot

RUN gunicorn main:main --workers 4 --threads 4 --bind 0.0.0.0:8080 --timeout 86400 --worker-class aiohttp.GunicornWebWorker

RUN python -m bot
