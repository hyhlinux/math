import asyncio
import functools
import datetime


def get_time():
    return datetime.datetime.now()


def callback(arg, *, kwarg='default'):
    print('callback invoked with {} and {} : {}'.format(arg, kwarg, get_time()))

async def do(loop):
    print('registering callbacks')
    loop.call_soon(callback, 1)
    wrapped = functools.partial(callback, kwarg='not default')
    loop.call_soon(wrapped, 2)

    await asyncio.sleep(0.1)


def main():
    event_loop = asyncio.get_event_loop()
    try:
        print('entering event loop')
        event_loop.run_until_complete(do(event_loop))
    finally:
        print('closing event loop')
        event_loop.close()

if __name__ == '__main__':
    main()