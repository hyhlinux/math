FROM python:alpine3.6
WORKDIR /app
RUN apk add --update --no-cache g++ gcc libxslt-dev
ADD . /app
RUN pip install -r requirement.txt
CMD python /app/main.py