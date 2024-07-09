ARG PYTHON_VERSION=3.11.4
FROM python:${PYTHON_VERSION}-slim

WORKDIR /app

COPY . .

RUN python -m pip install -r requirements.txt
EXPOSE 8000

CMD ["python3", "app.py"]