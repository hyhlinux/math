import asyncio
import datetime


def now():
    return datetime.datetime.now()


async def phase(i):
    print('in phase {} at:{} '.format(i, now()))
    await asyncio.sleep(1*i)
    print('done with phase {} now:{}'.format(i, now()))
    return 'phase {} result at:{}'.format(i, now())

async def do(n):
    print('staring do:')
    phases = [
        phase(i)
        for i in range(n)
    ]
    print('waiting for phases to complete')
    completed, pending = await asyncio.wait(phases)
    # print('complete: {} pending:{}'.format(completed, pending))
    results = [t.result() for t in completed]
    print('results: {}'.format(results))


def main():
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(do(3))
    finally:
        event_loop.close()

if __name__ == '__main__':
    main()