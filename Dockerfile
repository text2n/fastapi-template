
FROM python:3.10

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app
COPY ./storage /code/storage
COPY ./.env  /code/

CMD ["fastapi", "run", "app/main.py", "--port", "80"]