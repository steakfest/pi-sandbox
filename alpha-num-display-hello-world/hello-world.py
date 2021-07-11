import board
from adafruit_ht16k33.segments import Seg14x4

i2c = board.I2C()
display = Seg14x4(i2c)

display = Seg14x4(i2c, address=0x70)

display.brightness = 0.5

display.blink_rate = 3

display.print("H1V2")

