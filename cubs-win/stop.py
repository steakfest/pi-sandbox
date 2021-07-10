#!/usr/bin/env python

from time import sleep
from sys import exit

import sys

import unicornhat as unicorn

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(90)
unicorn.brightness(1.0)
width,height=unicorn.get_shape()


unicorn.clear()
