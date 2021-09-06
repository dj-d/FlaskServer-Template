FROM python:3-alpine

ADD setup.py .
RUN pip install -e .

COPY . /app
WORKDIR /app

CMD ["waitress-serve", "--call", "src:create_app"]