FROM node

WORKDIR /app

COPY p*.json ./

RUN npm i

COPY . .

EXPOSE 3000

CMD [ "npm","start" ]