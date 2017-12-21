import asyncio
import json
from aiohttp import web
from log import get_log
from esapi import ES

logger = get_log('aio')
es = ES()

async def index(request):
    logger.info('req:{}'.format(request))
    return web.Response(body=b'<h1>Aiohttp index</h1>', content_type='text/html')

async def get_rate_ip(ip):
    logger.info("ip:{}".format(ip))
    data = await es.async_get_ip_rate(ip)
    return data

async def do():
    logger.info('starting do')
    logger.info('waiting for phases to complete')
    top_ip = es.get_top_ip(100)
    phases = [get_rate_ip(ip.get('key', '')) for ip in top_ip]
    completed, pending = await asyncio.wait(phases)
    data = {}
    for index, t in enumerate(completed):
        logger.info("index:{} data:{}".format(index, t.result()))
        data["{}".format(index)] = t.result()
    if pending:
        logger.info('pending:{}'.format(pending))
        for t in pending:
            t.cancel()
    return data


async def auto(request):
    logger.info('req:{} bf'.format(request))
    data = await do()
    logger.info('done')
    return web.Response(body=json.dumps(data))


async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route(method='GET', path='/api/index', handler=index)
    app.router.add_route(method='GET', path='/api/auto', handler=auto)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logger.info('server start at http://127.0.0.1:9000')
    return srv


def main():
    logger.info('start web')
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(init(event_loop))
        event_loop.run_forever()
    finally:
        event_loop.close()

if __name__ == '__main__':
    main()