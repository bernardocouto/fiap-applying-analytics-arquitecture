FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP src/application.py

RUN mkdir /application
WORKDIR /application
ADD . /application

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python3", "src/application.py"]
