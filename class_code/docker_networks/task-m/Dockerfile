FROM node:16-alpine

WORKDIR /app

COPY pack*.json ./

RUN npm i 

COPY . .

EXPOSE 3000

CMD ["npm", "start"]
