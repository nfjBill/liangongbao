import schedule
import time
import os

from Process import process

every_day = os.environ.get('every_day')
run_start = os.environ.get('run_start')


def job():
    process()


default_every_min = "06:00"
if every_day is not None:
    default_every_min = every_day

if run_start is None:
    process()

schedule.every().day.at(default_every_min).do(job)

#
while True:
    schedule.run_pending()
    time.sleep(1)
