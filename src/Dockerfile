FROM python:3.9

COPY . /usr/src

WORKDIR /usr

RUN pip install --no-cache-dir --upgrade -r /usr/src/requirements.txt

CMD ["uvicorn", "src.main:app", "--host=0.0.0.0", "--port=80", "--reload"]