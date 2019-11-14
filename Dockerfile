FROM python:alpine
EXPOSE 5000
RUN pip install pymorphy2 flask waitress
WORKDIR /app
COPY ./app.py /app/
ENTRYPOINT ["python", "app.py"]
