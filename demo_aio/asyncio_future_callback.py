import asyncio
import functools
import datetime


def get_time():
	return datetime.datetime.now()


def callback(future, n):
	print('{}: future done: {} {}'.format(n, future.result(), get_time()))


async def register_callbacks(all_done):
	print('registering callbacks on future')
	all_done.add_done_callback(functools.partial(callback, n=1))
	all_done.add_done_callback(functools.partial(callback, n=2))
	print('registering callbacks on future end')

async def do(all_done):
	await register_callbacks(all_done)
	print('setting result of future')
	all_done.set_result('the result')


def main():
	event_loop = asyncio.get_event_loop()
	try:
		all_done = asyncio.Future()
		event_loop.run_until_complete(do(all_done))
	finally:
		event_loop.close()


if __name__ == '__main__':
	main()