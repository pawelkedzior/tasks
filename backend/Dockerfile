FROM python:3.12-slim

WORKDIR /backend

COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY ./src ./src

CMD ["python3", "src/main.py"]
