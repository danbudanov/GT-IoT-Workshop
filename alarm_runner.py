
# external imports
from datetime import datetime

# our imports
from alarm import Alarm

g_alarm = None

def main():
	global myAlarm 
	g_alarm = Alarm()
	g_alarm.init_cb()
	g_alarm.start()

if __name__ == "__main__": main()
