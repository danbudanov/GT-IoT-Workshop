from flask import Flask, request, render_template, redirect
import json, datetime
# from apscheduler import Scheduler
app = Flask(__name__)

# def get_time(time_str):

alarm_info = {
        'set': False,
        }

# sched = Scheduler()
# s
@app.route('/', methods=['GET', 'POST'])
def handle_alarm():
    global alarm_time;
    if request.method == 'POST':
        for i in request.form:
            alarm_info[i] = request.form[i]
        print "Alarm was set to {} on {}".format(alarm_info['time'], alarm_info['date'])
        alarm_info["set"] = True
        alarm_time = datetime.datetime.strptime((alarm_info["time"] + " " \
            + alarm_info["date"]), "%H:%M %Y-%m-%d")
        # print time
        # print (alarm_info["time"] + " " + alarm_info["date"]) == "05:07 2016-11-17"
        print alarm_time.hour
        return redirect('/')
        # set_alarm( alarm_info )
    else:
        return render_template("index.html", alarm = alarm_info)
