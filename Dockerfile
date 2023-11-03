FROM python:3.11

WORKDIR /app

COPY . /app
COPY requirements.txt .

RUN pip install --trusted-host pypi.python.org -r requirements.txt
ENV PYTHONPATH /app


CMD ["python", "web/main.py"]