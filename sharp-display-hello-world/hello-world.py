import sys
import board
import busio
import digitalio
# import displayio
from PIL import Image, ImageDraw, ImageFont
import adafruit_sharpmemorydisplay
from time import sleep


# Colors
BLACK = 0
WHITE = 255

BORDER = 5
FONTSIZE = 90

spi = busio.SPI(board.SCK, MOSI=board.MOSI)
scs = digitalio.DigitalInOut(board.D6) # inverted chip select

display = adafruit_sharpmemorydisplay.SharpMemoryDisplay(spi, scs, 400, 240)



with Image.open("imagery/zoom-logo.png") as image:

	print(image.format, image.size, image.mode)

	display.image(image)
	display.show()

	while True:
		pass


sys.exit()


# Clear display.
display.fill(0)
display.show()

# on_off = 1
# while True:
#     on_off = (on_off + 1) % 2
#     print("Filling with:" + str(on_off))
#     display.fill(on_off)
#     display.show()
#     sleep(1)

# sys.exit()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new('1', (display.width, display.height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black background
draw.rectangle((0, 0, display.width, display.height), outline=BLACK, fill=BLACK)

# Draw a smaller inner rectangle
draw.rectangle((BORDER, BORDER, display.width - BORDER - 1, display.height - BORDER - 1),outline=WHITE, fill=WHITE)

# Load a TTF font.
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', FONTSIZE)

# Draw Some Text
text = ["Cubs", "Win!!"]
textIndex = 0
while True:
	draw.rectangle((BORDER, BORDER, display.width - BORDER - 1, display.height - BORDER - 1),outline=WHITE, fill=WHITE)
	(font_width, font_height) = font.getsize(text[textIndex])
	draw.text((display.width//2 - font_width//2, display.height//2 - font_height//2), text[textIndex], font=font, fill=BLACK)
	# Display image
	display.image(image)
	display.show()
	textIndex = (textIndex + 1) % 2
	sleep(1)
	

