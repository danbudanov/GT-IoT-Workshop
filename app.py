from flask import Flask
app = Flask(__name__)

@app.route('/')
def started():
    return 'Hey dudez'

@app.route('/alarms')
