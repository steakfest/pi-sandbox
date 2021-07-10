import board
import neopixel
from time import sleep
import random
import sys

pixels = neopixel.NeoPixel(board.D18, 4)

if len(sys.argv) > 1 and sys.argv[1] == 'stop':
    for p in range(4):
        pixels[p] = (0,0,0)
    sys.exit(0)

delay = 0.1

pixels[0] = (255,255,255)
pixels[1] = (255,255,255)
pixels[2] = (255,255,255)
pixels[3] = (255,255,255)


def resetPixels():
    pixels[0] = (0,0,0)
    pixels[1] = (0,0,0)
    pixels[2] = (0,0,0)
    pixels[3] = (0,0,0)

def randColor():
    maxIntensity = 64
    return (
        random.randrange(maxIntensity),
        random.randrange(maxIntensity),
        random.randrange(maxIntensity))

def randPixel():
    return random.randrange(4)


def setPixel(activePixel, activeColor):
    for pix in range(4):
        color = (0,0,0)
        if pix == activePixel:
            color = activeColor
        pixels[pix] = color

def animate():
    activePixel = 0

    while True:
        setPixel(activePixel, (0,0,64))
        sleep(delay)
        activePixel = (activePixel + 1) % 4



def kitanimate():
    activePixel = 0
    direction   = +1

    while True:
        setPixel(activePixel, (64,0,0))
        sleep(delay)
        activePixel = (activePixel + direction)
        if activePixel >= 4:
            direction = direction * -1
            activePixel = 3
        if activePixel < 0:
            direction = direction * -1
            activePixel = 0

def sparkle():

    while True:
        pixels[randPixel()] = randColor()
        pixels[randPixel()] = randColor()
        pixels[randPixel()] = randColor()
        pixels[randPixel()] = randColor()
        sleep(delay)


resetPixels()

# sparkle()

animate()
