import asyncio
import functools

from log import get_log

logger = get_log('async_lock')


def unlock(lock):
	logger.info('callback releasing lock')
	lock.release()

async def coro1(lock):
	logger.info('coro1 waiting for the lock')
	with await lock:
		logger.info('coro1 acquired lock')
	logger.info('coro1 released lock')

async def coro2(lock):
	logger.info('coro2 waiting for the lock')
	with await lock:
		logger.info('coro2 acquired lock')
	logger.info('coro2 released lock')

async def do(loop):
	# Create and acquire a shared lock
	lock = asyncio.Lock()
	logger.info('acquiring the lock before starting coroutines')
	await lock.acquire()
	logger.info('lock acquired: {}'.format(lock.locked()))

	# 2s 后，释放锁
	loop.call_later(2, functools.partial(unlock, lock))
	# Run the coroutines that want to use the lock
	logger.info('waiting for coroutines')
	await asyncio.wait([coro1(lock), coro2(lock)]),


def main():
	event_loop = asyncio.get_event_loop()
	try:
		event_loop.run_until_complete(do(event_loop))
	finally:
		event_loop.close()

if __name__ == '__main__':
	main()