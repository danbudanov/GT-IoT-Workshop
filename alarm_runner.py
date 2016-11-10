
# external imports
import time
from datetime import datetime

# our imports
from alarm import Alarm

g_alarm = None


########################
# IO
#
# I2C(2) <- lcd
# D4     <- button
# D3     <- buzzer
# A0     <- temp
#########################
def main():
	global myAlarm 
	# create an alarm
	g_alarm = Alarm()

	# set alarm data
	# should be updated before the alarm is triggered
	g_alarm.set({'time': datetime.now().strftime("%H:%M:%S")})
	
	# starts the alarm
	g_alarm.start()

	time.sleep(10)

	# stops the alarm
	# sensors may also stop the alarm
	g_alarm.stop()

	time.sleep(10)
	print "done"

	# call this at program exit to kill child threads
	g_alarm.destr_cb()

if __name__ == "__main__": main()
