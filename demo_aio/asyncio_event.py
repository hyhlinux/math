import asyncio
import functools
from log import get_log

logger = get_log('async_event')


def set_event(event):
    logger.info('setting event in callback')
    event.set()

async def coro1(event):
    logger.info('coro1 waiting for event')
    await event.wait()
    logger.info('coro1 triggered')

async def coro2(event):
    logger.info('coro2 waiting for event')
    await event.wait()
    logger.info('coro2 triggered')

async def do(loop):
    # Create a shared event
    event = asyncio.Event()
    logger.info('event start stats:{}'.format(event.is_set()))
    loop.call_later(2, functools.partial(set_event, event))
    await asyncio.wait([coro1(event), coro2(event)])
    logger.info('event end state:{}'.format(event.is_set()))


def main():
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(do(event_loop))
    finally:
        event_loop.close()


if __name__ == '__main__':
    main()