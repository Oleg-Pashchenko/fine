
FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8082"]
