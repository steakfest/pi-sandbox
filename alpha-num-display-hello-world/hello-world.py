import board
import threading

from adafruit_ht16k33.segments import Seg14x4

TAIL = "    "

class DoubleSegment():
	"""A Class for managing two i2c alphanumeric Segments"""
	def __init__(self, i2c, leftAddr, rightAddr):
		i2c = board.I2C()
		leftDisplay  = Seg14x4(i2c, leftAddr)
		rightDisplay = Seg14x4(i2c, rightAddr)

	def brightness(bVal):
		leftDisplay.brightness(bVal)
		rightDisplay.brightness(bVal)

	def blink_rate(bRate):
		leftDisplay.blink_rate = bRate
		rightDisplay.blink_rate = bRate

	def print(value):
		leftDisplay.print(value)
		rightDisplay.print(value)

doubleSegment = DoubleSegment()

doubleSegment.print("JOHN")

# threads = []

# threads.append(threading.Thread(target=display.marquee, args=("HOME RUN" + TAIL,)))
# threads.append(threading.Thread(target=display2.marquee, args=("JOHN MCGOAN" + TAIL,)))

# for thread in threads:
# 	thread.start()

# for thread in threads:
# 	thread.join()


