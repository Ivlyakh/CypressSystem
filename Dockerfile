FROM cypress/browsers:node10.16.3-chrome80-ff73

WORKDIR /home/node

COPY package.json .
COPY package-lock.json .

RUN npm install 

COPY cypress.json ./
COPY cypress/ ./cypress/

#CMD ["./node_modules/.bin/cypress", "run", "--headless"]
CMD ["curl", "-s", "https://ipapi.co/json"]