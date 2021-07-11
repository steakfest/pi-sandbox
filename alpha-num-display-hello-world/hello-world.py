import board
import threading

from adafruit_ht16k33.segments import Seg14x4

TAIL = "    "

i2c      = board.I2C()
display  = Seg14x4(i2c)
display2 = Seg14x4(i2c)

display  = Seg14x4(i2c, address=0x70)
display2 = Seg14x4(i2c, address=0x71)

display.brightness = 0.75
display2.brightness = 0.75

# display.blink_rate = 3

# display.print("H1V2")

threads = []

threads.append(threading.Thread(target=display.marquee, args=("HOME RUN" + TAIL,)))
threads.append(threading.Thread(target=display2.marquee, args=("JOHN MCGOAN" + TAIL,)))

for thread in threads:
	thread.start()

for thread in threads:
	thread.join()


