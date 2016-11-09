
# external imports
import time
from datetime import datetime

# our imports
from alarm import Alarm

g_alarm = None

def main():
	global myAlarm 
	g_alarm = Alarm()
	g_alarm.set({'time': datetime.now().strftime("%H:%M:%S")})
	g_alarm.init_cb()
	
	g_alarm.start()
	time.sleep(10)
	g_alarm.stop()
	time.sleep(10)
	print "done"
	g_alarm.destr_cb()

if __name__ == "__main__": main()
