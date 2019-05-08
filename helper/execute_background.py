from state import state_datafb
import asyncio
from concurrent.futures import ThreadPoolExecutor
import time


def execute_background(max_worker, job):
    if (not state_datafb.state_is_running_schedule):
        executor = ThreadPoolExecutor(max_workers=max_worker)
        loop = asyncio.get_event_loop()
        boo = asyncio.ensure_future(loop.run_in_executor(executor, job))
        # loop.run_forever()
        # loop.close()
        state_datafb.state_is_running_schedule = True
    else:
        print('skip run schedule because run before')


def test():
    time.sleep(2)
    print('hihi')


def example():
    execute_background(max_worker=5, job=test)
    print('done')

# example()
