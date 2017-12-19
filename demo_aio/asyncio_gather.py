import asyncio


def now():
    import datetime
    return datetime.datetime.now()

async def phase(n):
    print('in phase:{} at:{}'.format(n, now()))
    await asyncio.sleep(n)
    print('done with phase:{} at:{}'.format(n, now()))
    return 'phase result:{} now:{}'.format(n, now())

async def do():
    print('starting do')
    print('waiting for phases to complete')
    results = await asyncio.gather(
        phase(1),
        phase(2),
    )
    print('results:{}'.format(results))


def main():
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(do())
    finally:
        event_loop.close()


if __name__ == '__main__':
    main()