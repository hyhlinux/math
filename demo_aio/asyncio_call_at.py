import asyncio
import datetime


def get_time():
    return datetime.datetime.now()


def callback(arg, loop):
    print('callback invoked with {} at:{}'.format(arg, loop.time()))

async def do(loop):
    now = loop.time()
    print('registering callbacks: {}'.format(now))
    loop.call_at(now+1, callback, 1, loop)
    loop.call_at(now+1, callback, 2, loop)
    loop.call_soon(callback, 3, loop)
    print('registering end callbacks: {}'.format(get_time()))

    await asyncio.sleep(1)
    print('registering end2 callbacks: {}'.format(get_time()))


def main():
    event_loop = asyncio.get_event_loop()
    event_loop.set_debug(True)
    try:
        print('entering event loop')
        event_loop.run_until_complete(do(event_loop))
    finally:
        print('closing event loop')
        event_loop.close()

if __name__ == '__main__':
    main()