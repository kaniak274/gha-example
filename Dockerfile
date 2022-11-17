FROM node:12 AS frontend

COPY . /app

RUN npm install && npm run build

FROM python:3.10-slim

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . /app

COPY --from=frontend /build/ /app/build

WORKDIR /app

EXPOSE 9000

ARG abc

ENV ABC=$abc

RUN useradd -ms /bin/sh newuser
USER newuser

ENTRYPOINT ["flask", "run", "--host=0.0.0.0", "--port=9000"]

