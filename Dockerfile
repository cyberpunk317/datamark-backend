FROM python:3.8

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY flaskr /app

WORKDIR /app
EXPOSE 5000
CMD ["python", "app.py"]

