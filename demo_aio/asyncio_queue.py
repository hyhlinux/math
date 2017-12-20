import asyncio
import functools
from log import get_log

logger = get_log('async_event')

async def consumer(n, q):
    logger.info('consumer {}: starting'.format(n))
    while True:
        logger.info('consumer {}: waiting for item'.format(n))
        item = await q.get()
        logger.info('consumer {}:has item {}'.format(n, item))
        if item is None:
            q.task_done()
            break
        else:
            await asyncio.sleep(0.01*item)
            q.task_done()
    logger.info('consumer {}: ending'.format(n))

async def producer(q, num_workers):
    logger.info('starting producer')
    for i in range(num_workers):
        await q.put(i)
        logger.info('producer: added task {} to the queue'.format(i))
    logger.info('producer: adding stop signals to the queue')
    for i in range(num_workers):
        await q.put(None)
    logger.info('produer: waiting for queue to empty')
    await q.join()
    logger.info('producer: ending')

async def do(loop, num_consumers):
    # Create a shared event
    q = asyncio.Queue(maxsize=num_consumers)
    consumers = [loop.create_task(consumer(i, q)) for i in range(num_consumers)]
    prod = loop.create_task(producer(q, num_consumers))
    await asyncio.wait(consumers+[prod])
    logger.info('done')


def main():
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(do(event_loop, 2))
    finally:
        event_loop.close()


if __name__ == '__main__':
    main()