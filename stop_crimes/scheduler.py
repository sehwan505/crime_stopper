from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.base import JobLookupError
from google_crawling import google_crawling
#
sched = BackgroundScheduler()


sched.add_job(google_crawling("빅데이터"),'cron',day=2)
print("abc")
sched.start()