#!/bin/sh

nohup /app/http-watchmen cron --config /app/conf/app.yml &
python3 /app/ser.py
