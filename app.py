from flask import Flask, request, render_template
app = Flask(__name__)


alarm_info = {
        'time' : '12:30',
        'day': '9/29/13',
        }
@app.route('/', methods=['GET', 'POST'])
def set_alarm():
    if request.method == 'POST':
        # parse the json
        set_alarm( alarm_data )
    else:
        return render_template("alarm.html", alarm_info = alarm_info)


