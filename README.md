# Gimmicks Travels - Flask Azure Open AI api

A Simple Python Flask API to Interact with Azure Open AI

## Executing the API

```bash
python app.py           # On Windows
```

```Powershell
$env:FLASK_APP = "app"
$env:FLASK_ENV = "development"
flask run
```

## Few Commands to get started

```bash
pip install virtualenv
python.exe -m pip install --upgrade pip
python -m venv .venv
.venv/Scripts/activate
pip freeze
deactivate

pip install Flask python-dotenv openai
pip freeze > ./requirements
```

## Steps to create the API

> 1. Create a new folder
> 1. Create an .env file and Environment Variables
> 1. Create a virtual environment
> 1. Install `pip install Flask python-dotenv openai` and other dependencies
> 1. pip freeze > requirements.txt
> 1. Create a `app.py` file
