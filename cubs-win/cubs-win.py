#!/usr/bin/env python

from time import sleep
from sys import exit

import sys

import unicornhat as unicorn

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(270)
unicorn.brightness(0.75)
width,height=unicorn.get_shape()

wp = [255, 255, 255]
bp = [0,   0,   255]
lb = [200, 200, 255]

win_flag  = [
    [wp,wp,wp,wp,wp,wp,wp,wp,],
    [wp,bp,wp,wp,wp,wp,bp,wp,],
    [wp,bp,wp,wp,wp,wp,bp,wp,],
    [wp,bp,wp,wp,wp,wp,bp,wp,],
    [wp,bp,wp,bp,bp,wp,bp,wp,],
    [wp,bp,bp,wp,wp,bp,bp,wp,],
    [wp,bp,wp,wp,wp,wp,bp,wp,],
    [wp,wp,wp,wp,wp,wp,wp,wp,],
]
lose_flag = [
    [bp,bp,bp,bp,bp,bp,bp,bp,],
    [bp,bp,wp,bp,bp,bp,bp,bp,],
    [bp,bp,wp,bp,bp,bp,bp,bp,],
    [bp,bp,wp,bp,bp,bp,bp,bp,],
    [bp,bp,wp,bp,bp,bp,bp,bp,],
    [bp,bp,wp,bp,bp,bp,bp,bp,],
    [bp,bp,wp,wp,wp,wp,bp,bp,],
    [bp,bp,bp,bp,bp,bp,bp,bp,],
]



def red(pixel):
    return pixel[0]

def green(pixel):
    return pixel[1]

def blue(pixel):
    return pixel[2]

def show_bitmap(bitmap):
    print("Showing Bitmap")
    for x in range(8):
        for y in range(8):
            unicorn.set_pixel(x, 7-y, red(bitmap[x][y]), green(bitmap[x][y]), blue(bitmap[x][y]))
            
            unicorn.show()


while True:
    show_bitmap(win_flag)
    sleep(5.0)
    show_bitmap(lose_flag)
    sleep(5.0)


