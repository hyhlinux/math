import asyncio
import datetime


@asyncio.coroutine
def outer():
    print('in outer')
    print('waiting for result1', datetime.datetime.now())
    result1 = yield from phase1()
    result2 = yield from phase2(result1)
    return result1, result2


@asyncio.coroutine
def phase1():
    print('in phase1', datetime.datetime.now())
    return 'phase1:{}'.format(datetime.datetime.now())


@asyncio.coroutine
def phase2(arg):
    print('in phase2', datetime.datetime.now())
    return 'phase2 :{} {}'.format(arg, datetime.datetime.now())


def main():
    event_loop = asyncio.get_event_loop()
    try:
        return_value = event_loop.run_until_complete(outer())
        print('return_value:', return_value)
    finally:
        event_loop.close()

if __name__ == '__main__':
    main()