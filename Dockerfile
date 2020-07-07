FROM alpine:latest

# Install python and pip
RUN apk add --no-cache --update python3 py3-pip bash curl

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .


