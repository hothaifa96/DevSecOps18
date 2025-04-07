FROM python:3.14.0a6-alpine3.21

WORKDIR /applicaiton

COPY code.py .

# no need to declare 
ENV NAME=chen  

# we must declare it -> exception in the code
ENV YEAR=1996

CMD [ "python3", "code.py" ]