FROM python:3.9-slim

WORKDIR /app

COPY todos.py ./
COPY requirements.txt ./

RUN pip install -r requirements.txt

EXPOSE 5003

ENV TODOS_API_URL=http://localhost:5003
ENV AUTH_API_URL=http://localhost:5002
ENV USERS_API_URL=http://localhost:5001
ENV PORT=5003

CMD ["python3", "todos.py"]