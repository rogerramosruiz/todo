# Todo App

## Table of Contents
- [Stack](#stack)
- [Setup](#set-up)
    - [Requirements](#requirements)
    - [Environmet files](#environmet-files)
    - [Run with docker](#run-with-docker-compose)
- [Testing (optional)](#testing-optional)
    - [Warning](#warning)
    - [Requirements](#test-requirements)
    - [Create a virutal environment](#create-a-virutal-environment)
    - [Run tests](#run-tests)

## Stack

<img src="https://raw.githubusercontent.com/docker-library/docs/01c12653951b2fe592c1f93a13b4e289ada0e3a1/postgres/logo.png" width="60"> <img src="https://redis.com/wp-content/themes/wpx/assets/images/logo-redis.svg" height="50"> <img src="https://upload.wikimedia.org/wikipedia/commons/3/3c/Flask_logo.svg" height="60"> <img src="https://www.docker.com/wp-content/uploads/2022/03/vertical-logo-monochromatic.png" height="60"> <img src="https://upload.wikimedia.org/wikipedia/commons/1/1b/Svelte_Logo.svg" height="60"> <img src="https://upload.wikimedia.org/wikipedia/commons/d/d5/Tailwind_CSS_Logo.svg" height="60">


## Set up

### Requirements
- Docker
- Docker-compose

### Clone repo
```bash
git clone  https://github.com/rogerramosruiz/todo.git
cd todo
```
### Environmet files
Rename the the environment files

Linux
```bash
mv ./envfiles/.auth.env.template ./envfiles/.auth.env
mv ./envfiles/.auth.postgres.env.template ./envfiles/.auth.postgres.env
mv ./envfiles/.redis.env.template ./envfiles/.redis.env
mv ./envfiles/.task.env.template ./envfiles/.task.env
mv ./envfiles/.task.postgres.env.template ./envfiles/.task.postgres.env
```

Windows
```powershell
move envfiles\.auth.env.template envfiles\.auth.env
move envfiles\.auth.postgres.env.template envfiles\.auth.postgres.env
move envfiles\.redis.env.template envfiles\.redis.env
move envfiles\.task.env.template envfiles\.task.env
move envfiles\.task.postgres.env.template envfiles\.task.postgres.env
```

Fill the empty variables in the environnment files

### Run with docker-compose

First set **PUBLIC_API_URL** with your domain name or IP address for the front-end

Linux
```bash
export PUBLIC_API_URL=http://192.168.0.2
```

Windows

```bash
SET PUBLIC_API_URL=http://192.168.0.2
```

Build images and run containers
```bash
docker-compose up -d
```

if **PUBLIC_API_URL** value is changed later on then run the last command with flag --build

```bash
docker-compose up --build -d
```

## Testing optional
First make sure containers are running

### Warning
Running tests will polute your databases, delete the directory volumes once tests are done

### Test requirements
- python


### Create a virutal environment
Creating a virutal envirnment is not required, but recomended

Linux
```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r auth/requirements_test.txt
```
Windows
```bash
python -m venv venv
venv\Scripts\activate
pip install -r auth/requirements_test.txt
```

### Run tests 
```
pytest -v auth/test/
pytest -v task/test/
```