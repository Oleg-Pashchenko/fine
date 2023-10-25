
FROM python:3.11

WORKDIR /app

COPY . /app
ENV PYTHONPATH /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

CMD ["python", "web/main.py"]
