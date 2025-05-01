FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY auth.py .

EXPOSE 5002

CMD [ "python3","auth.py" ]