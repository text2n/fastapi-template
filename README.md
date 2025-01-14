## Clone git repo
git clone https://github.com/text2n/fastapi-template.git

## Create virtual environment
python3 -m venv .venv

## Activate virtual environment
source .venv/bin/activate

## Install dependencies
pip install -r requirements.txt

## Update requirements (after installing new packages)
pip freeze > requirements.txt

## Deactivate virtualenv
deactivate

## Copy .env.example to .env and change configurations
cp .env.example .env

## Run server
fastapi dev app/main.py