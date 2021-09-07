FROM python:3-alpine

ENV FLASK_APP=src
ENV FLASK_ENV=production

ADD setup.py .
RUN pip install -e .

COPY . /app
WORKDIR /app

RUN ["flask", "init-db"]

CMD ["waitress-serve", "--call", "src:create_app"]