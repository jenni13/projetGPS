#! /usr/bin/python

# License: GPL 2.0

import os
from gps import *
from time import *
import time
import threading
import webbrowser

url = 'http://www.google.fr/maps/'
chrome_path = '/usr/bin/google-chrome %s'
os.system('clear')

class GpsPoller(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		global gpsd #bring it in scope
		gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
		self.current_value = None
		self.running = True #setting the thread running to true

	def run(self):
		global gpsd
		while gpsp.running:
			gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer

if __name__ == '__main__':

	gpsp = GpsPoller() # create the thread
	gpsp.start()
	t_end = time.time()+10
	while True:
		
		os.system('clear')

		print
		print ' GPS reading'
		print '----------------------------------------'
		print 'latitude    ' , gpsd.fix.latitude
		print 'longitude   ' , gpsd.fix.longitude
		time.sleep(5)
		if time.time() >= t_end:
			break

	gpsp.running = False
	print 'redirection page web'
	webbrowser.get(chrome_path).open(url)
	print 'allo'
	sys.exit(0)
