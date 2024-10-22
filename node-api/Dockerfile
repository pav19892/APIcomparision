# Node.js Dockerfile
FROM node:22-slim

WORKDIR /app

COPY ./package*.json /app
COPY ./task.js /app/task.js

RUN npm install express

EXPOSE 8012

CMD ["node","task.js"]
