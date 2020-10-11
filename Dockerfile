#docker script

FROM python:latest

WORKDIR /usr/src/app

ADD requirements.txt /usr/src/app

RUN pip install -r requirements.txt

ADD . /usr/src/app

# collect static/asset files

RUN python manage.py collectstatic --noinput

CMD gunicorn _dj_.wsgi:application --bind 0.0.0.0:$PORT
