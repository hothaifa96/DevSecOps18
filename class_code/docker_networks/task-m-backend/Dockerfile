FROM python:3.14-rc-alpine3.21

WORKDIR /task-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY main.py .

EXPOSE 5050

CMD [ "python3", "main.py" ]