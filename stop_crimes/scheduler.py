from apscheduler.jobstores.base import JobLookupError
from apscheduler.schedulers.background import BackgroundScheduler
import time
from google_crawling import google_crawling



class Scheduler:
    def __init__(self):
        self.sched = BackgroundScheduler()
        self.sched.start()
        self.job_id = ''

    def __del__(self):
        self.shutdown()

    def shutdown(self):
        self.sched.shutdown()

    def kill_scheduler(self, job_id):
        try:
            self.sched.remove_job(job_id)
        except JobLookupError as err:
            print("fail to stop Scheduler: {err}".format(err=err))
            return
    def scheduler(self, type, job_id):
        print("{type} Scheduler Start".format(type=type))
        if type == 'interval':
            self.sched.add_job(google_crawling, type, days=2, id=job_id, args=["자영업자"])
        elif type == 'cron':
            self.sched.add_job(self.hello, type, day_of_week='mon-fri',
                                                 hour='0-23', second='*/2',
                                                 id=job_id, args=(type, job_id))


if __name__ == '__main__':
    scheduler = Scheduler()
    scheduler.scheduler('interval', "2")
    count = 0
    while True:
        print("Running main process")
        time.sleep(86400)
        count += 1
        if count == 7:
            scheduler.kill_scheduler("2")
            print("Kill interval Scheduler")
            break