import schedule
import time
import os

from Process import process

every_day = os.environ.get('every_day')
run_start = os.environ.get('run_start')


def job():
    process()


default_every_day = "06:00"
if every_day is not None:
    default_every_day = every_day

sdd = default_every_day.split(':')
hour = int(sdd[0])
d8h = (hour + 24 - 8) % 24
sd8 = str(d8h)
if len(sd8) == 1:
    sd8 = '0' + sd8

default_every_day = sd8 + ':' + sdd[1]

if run_start is None:
    process()

schedule.every().day.at(default_every_day).do(job)

#
while True:
    schedule.run_pending()
    time.sleep(1)
