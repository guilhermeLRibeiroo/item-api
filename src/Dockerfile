FROM python:3.9

COPY . /usr/src/app

WORKDIR /usr/src/app

RUN pip install pipreqs

RUN pipreqs .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=80", "--reload"]
