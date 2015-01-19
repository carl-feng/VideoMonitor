__author__ = 'carlfeng'

import serial, sys, time
import struct

class PTZ(object):
	array_up = [0xff,0x01,0x00,0x08,0x00,0x17,0x20]
	array_down = [0xff,0x01,0x00,0x10,0x00,0x17,0x28]
	array_left = [0xff,0x01,0x00,0x04,0x17,0x00,0x1c]
	array_right = [0xff,0x01,0x00,0x02,0x17,0x00,0x1a]
	array_stop = [0xff,0x01,0x00,0x00,0x00,0x00,0x01]
	
	def __init__(self):
		self.port = serial.Serial("/dev/ttyUSB0", baudrate=9600, 
			bytesize=8, parity='N', stopbits=1, xonxoff=0, timeout=1)
	
	def up(self):
		for key in self.array_up:
			self.port.write(struct.pack("B", key))
	def down(self):
		for key in self.array_down:
			self.port.write(struct.pack("B", key))
	def right(self):
		for key in self.array_right:
			self.port.write(struct.pack("B", key))
	def left(self):
		for key in self.array_left:
			self.port.write(struct.pack("B", key))
	def stop(self):
		for key in self.array_stop:
			self.port.write(struct.pack("B", key))
	
	def DoAction(self, action):
		if action == "up":
			self.up()
		if action == "down":
			self.down()
		if action == "right":
			self.right()
		if action == "left":
			self.left()
		
		time.sleep(1)
		self.stop()


if __name__ == '__main__':
	if len(sys.argv) != 2:
		print "Usage: %s [up|down|right|left|stop]"% sys.argv[0]
	ptz = PTZ()
	if sys.argv[1] == "up":
		ptz.up()
	if sys.argv[1] == "down":
		ptz.down()
	if sys.argv[1] == "right":
		ptz.right()
	if sys.argv[1] == "left":
		ptz.left()
	if sys.argv[1] == "stop":
		ptz.stop()
