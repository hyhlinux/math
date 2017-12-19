import asyncio
from esapi import ES

es = ES()


def now():
    import datetime
    return datetime.datetime.now()

async def get_rate_ip(ip):
    print('in get_rate_ip:{} at:{}'.format(ip, now()))
    data = await es.async_get_ip_rate(ip)
    return data

async def do():
    print('starting do')
    print('waiting for phases to complete')
    cur_time = now()
    top_ip = es.get_top_ip(100)
    phases= [get_rate_ip(ip.get('key', '')) for ip in top_ip]
    completed, pending = await asyncio.wait(phases)
    for index, t in enumerate(completed):
        print(index, t.result())
    if pending:
        print('pending:{}'.format(pending))
        for t in pending:
            t.cancel()
    print('all_time:{}'.format(now() - cur_time))


def main():
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(do())
        import time
        time.sleep(20)
    finally:
        print('close ')
        event_loop.close()


if __name__ == '__main__':
    main()