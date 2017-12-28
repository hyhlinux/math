#!/bin/sh

nohup /app/http-watchmen cron --config /app/conf/app.yml > log.log &
python3 /app/ser.py
