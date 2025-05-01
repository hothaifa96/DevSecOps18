FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY users_api.py .

EXPOSE 5001

CMD [ "python3","users_api.py" ]