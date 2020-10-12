from apscheduler.jobstores.base import JobLookupError
from apscheduler.schedulers.background import BackgroundScheduler
import time
from google_crawling import google_crawling
from twitter_stopper2 import *



class Scheduler:
    def __init__(self):
        self.sched = BackgroundScheduler()
        self.sched.start()
        self.job_id = ''

    def kill_scheduler(self, job_id):
        try:
            self.sched.remove_job(job_id)
        except JobLookupError as err:
            print("fail to stop Scheduler: {err}".format(err=err))
            return
    def scheduler(self, type, job_id):
        print("{type} Scheduler Start".format(type=type))
        if type == 'interval':
            self.sched.add_job(crawling_twitter_live, type, minutes=40, id=job_id, args=["섹트",["고딩","중딩","17","16","15","14","13","04","03","05","06","07","판매","노예","교복","자영","자영판매","합성","거래","자위영상","팔아요"]])
        elif type == 'cron':
            self.sched.add_job(self.hello, type, day_of_week='mon-fri',
                                                 hour='0-23', second='*/2',
                                                 id=job_id, args=(type, job_id))


if __name__ == '__main__':
    scheduler = Scheduler()
    scheduler.scheduler('interval', "2")
    crawling_twitter_live("섹트",["고딩","중딩","17","16","15","14","13","04","03","05","06","07","판매","노예","교복","자영","자영판매","합성","거래","자위영상","팔아요","팜","조건만남"])
    count = 0
    while True:
        time.sleep(1)
        count += 1

        if count % 10 == 0:
            print("running")
        if count == 32000:
            scheduler.kill_scheduler("2")
            print("Kill interval Scheduler")
            break