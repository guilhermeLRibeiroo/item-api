# item-api

Just an API

## Technologies

- [fastapi](https://fastapi.tiangolo.com/)
- [uvicorn](https://www.uvicorn.org/)

## Requirements & How to run

- You will need [Docker](https://docs.docker.com/get-docker/).
- While Docker is running (I'm using Linux containers) run `docker-compose up` on terminal\
where `docker-compose.yml` is and the API will be running at [localhost:8000](http://localhost:8000)

- To fill the database with tables you need to run `python revision.py` && `python upgrade.py`\
(usr/src/database/migrations) inside the API container using the CLI
