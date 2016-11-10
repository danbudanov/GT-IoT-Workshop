# global imports
from threading import Timer
from datetime import datetime

import pyupm_i2clcd as lcd

# local imports
from devices import controls

class Alarm(object):
	cb_cont = True
	cb_en = True
	cb_int = 1

	properties = None
	
	in_alarm = False
	disp_show_time = False

	def __init__(self):
		global cb_int
		cb_int = 1

		self.init_cb()

	def __exit__(self, exc_type, exc_value, traceback):
		self.destr_cb()
	
	def init_cb(self):
		self.cb_scheduler()

	def destr_cb(self):
		self.cb_cont = False

	def cb_int(self, interval):
		global cb_int
		cb_int = interval	
	
	def cb_scheduler(self):
		global cb_int

		if (self.cb_en == True):
			self.cb_handler()

		if (self.cb_cont == True):
			Timer(cb_int, self.cb_scheduler).start()

	###############################
	# functionality
	###############################
	def cb_handler(self):
		if (self.in_alarm == True):
			if (self.disp_show_time == True):
				controls.print_lcd(0, 
self.properties['time'], 
"green")
			else:
				controls.print_lcd(0, "Wake Up!", "red")
				controls.play_sound(1)
			
			tmp = controls.read_temp()
			print tmp
			if (tmp > 75):
				controls.print_lcd(1, "Weather: WARM", 
"none")
			elif (tmp < 60):
				controls.print_lcd(1, "Weather: COLD", 
"none")
			else:
				controls.print_lcd(1, "Weather: MILD", 
"none")
			self.disp_show_time = (not self.disp_show_time)
		else:
			controls.print_lcd(0, datetime.now 
().strftime("%H:%M:%S"), "white")
			controls.print_lcd(1, "                    ", 
"none")

		if (controls.read_btn() == True):
			self.in_alarm = False

	def set(self, props):
		self.properties = props

	def start(self):
		self.in_alarm = True

	def stop(self):
		self.in_alarm = False
		
