import asyncio


async def coroutine():
    print("in coroutine")
    return 'result'


def main():
    event_loop = asyncio.get_event_loop()
    try:
        print('starting coroutine')
        coro = coroutine()
        print('entering event loop')
        ret = event_loop.run_until_complete(coro)
        print(ret)
    finally:
        print('closing event loop')
        event_loop.close()


if __name__ == '__main__':
    main()
