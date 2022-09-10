FROM python:3.9-slim-buster

WORKDIR /barah

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "gunicorn", "-b", "0.0.0.0:8000", "flask_app:app"]