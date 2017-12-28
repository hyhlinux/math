FROM amancevice/pandas:0.21.0-python3-alpine

WORKDIR /app
ADD require.txt /app/require.txt
RUN pip3 install -r require.txt
RUN apk update && apk add curl bash tree tzdata \
	&& cp -r -f /usr/share/zoneinfo/Hongkong /etc/localtime

ADD . /app
# CMD python3 /app/server.py
CMD sh /app/start.sh
