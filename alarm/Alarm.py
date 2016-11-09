# global imports
from threading import Timer

import pyupm_i2clcd as lcd

from devices import controls

class Alarm(object):
	cb_cont = True
	cb_en = False
	cb_int = 1

	properties = None
	disp_show_time = False;

	def __init__(self):
		global cb_int
		cb_int = 1
	
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
		if (self.disp_show_time == True):
			controls.print_lcd(0, self.properties['time'])
		else:
			controls.print_lcd(0, "Wake Up!")

		self.disp_show_time = (not self.disp_show_time)

	def set(self, props):
		self.properties = props

	def start(self):
		self.cb_en = True

	def stop(self):
		self.cb_en = False
		cb_en = False
		
