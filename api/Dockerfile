FROM python:3.4

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE production_settings

RUN git clone https://github.com/lepus-ctf/lepus-api.git /app
RUN pip install -r /app/package.pip
RUN pip install psycopg2
RUN pip install gunicorn

ADD production_settings.py /app/src/production_settings.py

WORKDIR /app/src

RUN python manage.py collectstatic --noinput

VOLUME /app/static
