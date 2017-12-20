import asyncio
import functools
from log import get_log

logger = get_log('async_event')

async def consumer(condition, n):
    with await condition:
        logger.info('consumer {} is waiting'.format(n))
        await condition.wait()
        logger.info('consumer {} triggered'.format(n))
        logger.info('ending consumer {}'.format(n))

async def mainipulate_condition(condition):
    logger.info('starting manipulate_codition')
    await asyncio.sleep(0.1)
    for i in range(1, 3):
        with await condition:
            logger.info('notifying {} cosumers'.format(i))
            condition.notify(n=i)
        await asyncio.sleep(0.1)

    with await condition:
        logger.info('notifying remaining consumers')
        condition.notify_all()

async def do(loop):
    # Create a shared event
    condition = asyncio.Condition()
    consumers = [
        consumer(condition, i)
        for i in range(5)
    ]
    loop.create_task(mainipulate_condition(condition))
    await asyncio.wait(consumers)


def main():
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(do(event_loop))
    finally:
        event_loop.close()


if __name__ == '__main__':
    main()