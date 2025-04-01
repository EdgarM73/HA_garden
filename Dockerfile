FROM python:3.10

WORKDIR /app
COPY run.py /app/run.py
COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

CMD ["python", "/app/run.py"]
