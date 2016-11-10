from flask import Flask, request, render_template, redirect
import json, datetime
app = Flask(__name__)

myAlarm = {
        'set': False,
        }

@app.route('/', methods=['GET', 'POST'])
def handle_alarm():
    global alarm_time;
    if request.method == 'POST':
        for i in request.form:
            myAlarm[i] = request.form[i]
        print "Alarm was set to {} on {}".format(myAlarm['time'], myAlarm['date'])
        myAlarm["set"] = True
        # alarm_time = datetime.datetime.strptime((myAlarm["time"] + " " \
        #     + myAlarm["date"]), "%H:%M %Y-%m-%d")
        # print alarm_time.hour
        return redirect('/')
    else:
        return render_template("index.html", alarm = myAlarm)
