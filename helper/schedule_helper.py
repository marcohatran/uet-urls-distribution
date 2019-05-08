import schedule
import time


def schedule_every(seconds, job):
    print('subscribe ', job, ' per ', seconds)
    schedule.every(seconds).seconds.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)


# example only purpose
def job():
    print("I'm working...")


def example():
    schedule_every(seconds=5, job=job)
