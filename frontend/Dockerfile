FROM node:18.10.0
WORKDIR /app
COPY . .
RUN npm install --silent
RUN npm install react-scripts --silent
RUN npm run build
CMD ["npm", "start"]
