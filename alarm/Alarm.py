# global imports
from threading import Timer

import pyupm_i2clcd as lcd

class Alarm(object):
	cb_en = False
	cb_int = 1

	properties = None

	def __init__(self):
		global cb_int
		cb_int = 1
	
	def init_cb(self):
		self.cb_scheduler()

	def cb_int(self, interval):
		global cb_int
		cb_int = interval	
	
	def cb_scheduler(self):
		global cb_int

		if (self.cb_en == True):
			self.cb_handler()

		Timer(cb_int, self.cb_scheduler).start()

	def cb_handler(self):
		print "update"

	def set(self, props):
		self.properties = props

	def start(self):
		self.cb_en = True

	def stop(self):
		self.cb_en = False
		cb_en = False
		
