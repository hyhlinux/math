#### run
```bash
docker run -it -v `pwd`/conf:/app/conf --network=host aioweb sh
```

```bash
app # ./http-watchmen run --logLevel 7 --config conf/app.yml --jobName job-api
```

```bash
/app # ./http-watchmen run --logLevel 7 --config conf/app.yml --jobName job-api
2017/12/27 22:45:35.686 [I] [run.go:63] config-json:{"timezone":"Asia/Shanghai","jobs":[{"name":"job-api","url":"http://47.91.255.0/api/index2","retry_cnt":3,"retry_time":5,"cron":"@every 20s","command":["python3 /app/ser.py"],"env":["MONGOPORT=27017"],"mail":null,"redis_addr":"","redis_passwd":"","redis_db":0}],"mail":{"smtp_user":"user","smtp_passwd":"pass","smtp_host":"smtp.zoho.com:465","smtp_tls":true,"mail_to":["huoyinghui@apkpure.net"],"mail_subject":""}}
2017/12/27 22:45:35.687 [D] [run.go:72] job:&{job-api http://47.91.255.0/api/index2 3 5  @every 20s [python3 /app/ser.py] [MONGOPORT=27017] <nil>   0} job.name:job-api   jobname:job-api  bcJob.Mail:{user pass smtp.zoho.com:465 true [huoyinghui@apkpure.net] }
2017/12/27 22:45:35.687 [D] [cron.go:137] err:redisPasswd can not be empty..redis ser passwd, will be empty
2017/12/27 22:45:35.687 [D] [jobs.go:54] job.name:job-api start ..

2017/12/27 22:45:51.194 [W] [utils.go:30] Expected [3] retry but was [3] 
2017/12/27 22:45:51.194 [D] [jobs.go:68] CMD##:python3 /app/ser.py            # 服务成功被启动
2017/12/27 22:45:51.195 [D] [jobs.go:82] ENV##:[HOSTNAME=c994f586cfc4 SHLVL=1 HOME=/root TERM=xterm PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin PWD=/app MONGOPORT=27017 OUTPUTPATH=/tmp/smart_backup/job-api]...
2017-12-27 22:45:51,416:   34:     esapi:    INFO:create ok!!
2017-12-27 22:45:51,416:   34:       aio:    INFO:create ok!!
2017-12-27 22:45:51,419:   53:       aio:    INFO:start web
2017-12-27 22:45:51,421:   48:       aio:    INFO:server start at http://127.0.0.1:9000
```

#### 后台托管
```bash
/app # nohup ./http-watchmen cron  --logLevel 7 --config conf/app.yml&
/app # nohup: appending output to nohup.out
/app # ps -ef
PID   USER     TIME   COMMAND
    1 root       0:00 sh
   56 root       0:00 ./http-watchmen cron --logLevel 7 --config conf/app.yml
   62 root       0:00 ps -ef
/app # tail -f nohup.out
017/12/27 23:00:23.034 [I] [cron.go:83] config-json:{"timezone":"Asia/Shanghai","jobs":[{"name":"job-api","url":"http://47.91.255.0/api/index2","retry_cnt":3,"retry_time":5,"cron":"@every 20s","command":["ls","python3 ser.py\u0026"],"env":["MONGOPORT=27017"],"mail":null,"redis_addr":"","redis_passwd":"","redis_db":0}],"mail":{"smtp_user":"user","smtp_passwd":"pass","smtp_host":"smtp.zoho.com:465","smtp_tls":true,"mail_to":["huoyinghui@apkpure.net"],"mail_subject":""}}
2017/12/27 23:00:23.034 [D] [cron.go:91] index:0 job:&{job-api http://47.91.255.0/api/index2 3 5  @every 20s [ls python3 ser.py&] [MONGOPORT=27017] <nil>   0} bcjob.mail:{user pass smtp.zoho.com:465 true [huoyinghui@apkpure.net] }
2017/12/27 23:00:23.034 [D] [cron.go:137] err:redisPasswd can not be empty..redis ser passwd, will be empty
2017/12/27 23:00:23.034 [D] [cron.go:128] cur_id:0 job-next-time:2017-12-27 23:00:43 +0800 CST
2017/12/27 23:00:43.000 [D] [jobs.go:54] job.name:job-api start ..
2017/12/27 23:00:58.496 [W] [utils.go:30] Expected [3] retry but was [3]
2017/12/27 23:00:58.497 [D] [jobs.go:68] CMD##:ls
2017/12/27 23:00:58.497 [D] [jobs.go:82] ENV##:[HOSTNAME=moby SHLVL=1 HOME=/root TERM=xterm PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin PWD=/app MONGOPORT=27017 OUTPUTPATH=/tmp/smart_backup/job-api]...
Dockerfile
__pycache__
conf
esapi.py
http-watchmen
log.py
nohup.out
require.txt
ser.py
start.sh
2017/12/27 23:00:58.500 [D] [jobs.go:68] CMD##:python3 ser.py&
2017/12/27 23:00:58.500 [D] [jobs.go:82] ENV##:[HOSTNAME=moby SHLVL=1 HOME=/root TERM=xterm PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin PWD=/app MONGOPORT=27017 OUTPUTPATH=/tmp/smart_backup/job-api]...
2017/12/27 23:00:58.509 [D] [db.go:26] pong:PONG
2017/12/27 23:00:58.512 [D] [jobs.go:151] job-api: nextRun:2017-12-27 23:01:18 +0800 CST

ç2017/12/27 23:01:03.000 [D] [jobs.go:54] job.name:job-api start ..
^C
/app # ps -ef
PID   USER     TIME   COMMAND
    1 root       0:00 sh
   56 root       0:00 ./http-watchmen cron --logLevel 7 --config conf/app.yml
   68 root       0:00 python3 ser.py           #被托管的服务，想要用后台模式启动，否则命令无法返回0.
   69 root       0:00 ps -ef
/app #
```