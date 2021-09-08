![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

[![SonarCloud](https://sonarcloud.io/images/project_badges/sonarcloud-orange.svg)](https://sonarcloud.io/dashboard?id=dj-d_FlaskServer-Template)

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=dj-d_FlaskServer-Template&metric=alert_status)](https://sonarcloud.io/dashboard?id=dj-d_FlaskServer-Template)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=dj-d_FlaskServer-Template&metric=security_rating)](https://sonarcloud.io/dashboard?id=dj-d_FlaskServer-Template)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=dj-d_FlaskServer-Template&metric=bugs)](https://sonarcloud.io/dashboard?id=dj-d_FlaskServer-Template)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=dj-d_FlaskServer-Template&metric=code_smells)](https://sonarcloud.io/dashboard?id=dj-d_FlaskServer-Template)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=dj-d_FlaskServer-Template&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=dj-d_FlaskServer-Template)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=dj-d_FlaskServer-Template&metric=coverage)](https://sonarcloud.io/dashboard?id=dj-d_FlaskServer-Template)

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