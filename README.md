![](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)

[![SonarCloud](https://github.com/dj-d/FlaskServer-Template/actions/workflows/sonarcloud.yml/badge.svg)](https://github.com/dj-d/FlaskServer-Template/actions/workflows/sonarcloud.yml)

# FlaskServer-Template

Simple template to initialize a backend in Python using the Flask microframework

## Docker Compose

Create an .env file

#### Example
```dotenv
    CONTAINER_NAME=YOUR_CONTAINER_NAME
    PORT=YOUR_PORT
```

### Run

#### Build & Start
```shell
  docker-compose up --build -d
```

#### Stop
```shell
  docker-compose down
```


## Docker

#### Build
```shell
  docker build -t flask-template .
```

#### Start
```shell
  docker run -d --name flask-template -it flask-template
```

#### Stop
```shell
  docker stop flask-template
```


## Manual

### Setup
Set .env file

#### Linux
```shell
    export FLASK_ENV=production
    export FLASK_ENV=src
```

#### Windows
```shell
    set FLASK_ENV=production
    set FLASK_ENV=src
```

### Run
```shell
  flask run
```