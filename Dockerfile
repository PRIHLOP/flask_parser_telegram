FROM python:alpine
WORKDIR /app
COPY . /app/
RUN pip install Flask telethon flake8 --no-cache-dir
CMD ["python", "app.py"]
