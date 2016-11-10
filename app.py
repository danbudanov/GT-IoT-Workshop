from flask import Flask, request, render_template, redirect
import json
app = Flask(__name__)


alarm_info = {
        'time' : '12:30',
        'date': '9/29/13',
        'set': True,
        'message': "hi!"
        }
@app.route('/', methods=['GET', 'POST'])
def handle_alarm():
    if request.method == 'POST':
        # parse the json
        print "POSTed!"
        print request.form
        return redirect('/')
        # set_alarm( alarm_info )
    else:
        return render_template("index.html", alarm = alarm_info)
