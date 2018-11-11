import gglex
import app
import datetime
import time
from apscheduler.schedulers.blocking import BlockingScheduler

evList=gglex.main()

for i in range(len(evList)):
    print('Event '+str(i)+':',evList[i])

def get_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_url():
    return evList[0][2]

def get_event_time():
    time=evList[0][0]
    time_p=time[:10]+' '+time[11:19]
    return time_p

def format_h(time):
    return int(time[11:13])

def format_m(time):
    return int(time[14:16])



def check_schedule():
    app.speak(get_url())
    scheduler.pause()
    global evList
    evList=evList[1:]
    if len(evList)==0:
        print("No More Events")
    else:
        scheduler.add_job(check_schedule, 'date', run_date=get_event_time())
        scheduler.resume()
    

scheduler = BlockingScheduler()
scheduler.add_job(check_schedule, 'date', run_date=get_event_time())
scheduler.start()
