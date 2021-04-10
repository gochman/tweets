FROM python:3-onbuild

COPY . /src
WORKDIR /src
# RUN pip install -r requirements.txt

ENV FLASK_ENV=docker
# EXPOSE 5000
CMD bash -c 'while !</dev/tcp/postgres/5432; do sleep 1; done' && python api.py