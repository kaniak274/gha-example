FROM python:3.10-slim

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . /app

WORKDIR /app

EXPOSE 9000

CMD ["flask", "run", "--host=0.0.0.0", "--port=9000"]

