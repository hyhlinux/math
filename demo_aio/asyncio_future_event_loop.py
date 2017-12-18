import asyncio


def mark_done(future, result):
	print('setting future result to {!r}'.format(result))
	future.set_result(result)


def main():
	event_loop = asyncio.get_event_loop()
	try:
		all_done = asyncio.Future()
		print('scheduling mark_done')
		event_loop.call_soon(mark_done, all_done, 'the result')
		result = event_loop.run_until_complete(all_done)
		print('returned result:{}'.format(result))
	finally:
		event_loop.close()
	pass

if __name__ == '__main__':
	main()