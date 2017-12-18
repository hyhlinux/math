import asyncio
import datetime


def get_time():
    return datetime.datetime.now()


def callback(arg):
    print('callback invoked with {} and {}'.format(arg, get_time()))

async def do(loop):
    print('registering callbacks: {}'.format(get_time()))
    loop.call_later(1, callback, 1)
    loop.call_later(1, callback, 2)
    loop.call_soon(callback, 3)
    print('registering end callbacks: {}'.format(get_time()))

    await asyncio.sleep(1)
    print('registering end2 callbacks: {}'.format(get_time()))


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