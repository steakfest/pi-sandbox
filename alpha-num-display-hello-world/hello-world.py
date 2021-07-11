import board
import threading

from adafruit_ht16k33.segments import Seg14x4

TAIL = "    "

class DoubleSegment():
	"""A Class for managing two i2c alphanumeric Segments"""
	
	def __init__(self, leftAddr, rightAddr):
		i2c = board.I2C()
		self.leftDisplay  = Seg14x4(i2c, leftAddr)
		self.rightDisplay = Seg14x4(i2c, rightAddr)

	def brightness(self, bVal):
		self.leftDisplay.brightness(bVal)
		self.rightDisplay.brightness(bVal)

	def blink_rate(self, bRate):
		self.leftDisplay.blink_rate = bRate
		self.rightDisplay.blink_rate = bRate

	def print(self, pval):
		self.leftDisplay.print(pval)
		self.rightDisplay.print(pval)

doubleSegment = DoubleSegment(0x70, 0x71)

doubleSegment.print("JOHN")

# threads = []

# threads.append(threading.Thread(target=display.marquee, args=("HOME RUN" + TAIL,)))
# threads.append(threading.Thread(target=display2.marquee, args=("JOHN MCGOAN" + TAIL,)))

# for thread in threads:
# 	thread.start()

# for thread in threads:
# 	thread.join()


