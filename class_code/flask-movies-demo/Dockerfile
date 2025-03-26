
# os - alpine # python env
FROM python:3.14.0a6-alpine3.21
#pwd /

# mkdir app && cd app 
WORKDIR /app 
#pwd /app

COPY . .

RUN pip install -r requirments.txt

EXPOSE 3030

CMD python3 movies.py