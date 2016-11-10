from flask import Flask, request, render_template, redirect
import json
from datetime import datetime
from threading import Timer
from alarm import Alarm
app = Flask(__name__)

alarm = Alarm()

myAlarm = {
        'set': False,
        }

@app.route('/', methods=['GET', 'POST'])
def handle_alarm():
    global alarm_time;
    global alarm;

    if request.method == 'POST':
        for i in request.form:
            myAlarm[i] = request.form[i]
        print "Alarm was set to {} on {}".format(myAlarm['time'], myAlarm['date'])
        myAlarm["set"] = True

	alarm_time = datetime.strptime(myAlarm["time"])
	now = datetime.now()
	alarm_delay = (now - alarm_time).total_seconds()
	
	alarm.set({'time': alarm_time.strftime("%H:%M:%S")})
	Timer(alarm_delay, alarm.start())
	
        # alarm_time = datetime.datetime.strptime((myAlarm["time"] + " " \
        #     + myAlarm["date"]), "%H:%M %Y-%m-%d")
        # print alarm_time.hour
        return redirect('/')
    else:
        return render_template("index.html", alarm = myAlarm)
