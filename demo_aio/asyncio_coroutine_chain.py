import asyncio

async def outer():
    print('in outer')
    result1 = await phase1()
    result2 = await phase2(result1)
    return result1, result2

async def phase1():
    print('in phase1')
    return 'result1'

async def phase2(arg):
    print('in phase2', arg)
    return 'result2 derived from {}'.format(arg)


def main():
    event_loop = asyncio.get_event_loop()
    try:
        ret = event_loop.run_until_complete(outer())
        print(ret)
    finally:
        event_loop.close()
if __name__ == '__main__':
    main()