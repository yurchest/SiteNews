FROM python:3.10

WORKDIR /app

COPY ./requirements.txt /requirements.txt

RUN pip install --no-cache-dir --upgrade -r /requirements.txt

EXPOSE 8000

COPY . /app

#CMD ["uvicorn", "app.src.app:app", "--host", "0.0.0.0", "--port", "8000"]