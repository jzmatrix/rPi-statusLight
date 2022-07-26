#!/usr/bin/env python3
# rpi_ws281x library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

import time
from time import sleep
from rpi_ws281x import *
import argparse

# LED strip configuration:
LED_COUNT      = 576      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

maxBright = 175

def innerX(strip):
    maxSet = 255
    minSet = 50
    for y in range (maxSet,minSet,-5):
        colorSet = Color(y,0,0)
        for x in range(0, 64):
            strip.setPixelColor(x, colorSet)
        for x in range(128, 192):
            strip.setPixelColor(x, colorSet)
        for x in range(256, 256+64):
            strip.setPixelColor(x, colorSet)
        for x in range(384, 384+64):
            strip.setPixelColor(x, colorSet)
        for x in range(512, 512+64):
            strip.setPixelColor(x, colorSet)
        strip.show()
    for y in range (minSet,maxSet,5):
        colorSet = Color(y,0,0)
        for x in range(0, 64):
            strip.setPixelColor(x, colorSet)
        for x in range(128, 192):
            strip.setPixelColor(x, colorSet)
        for x in range(256, 256+64):
            strip.setPixelColor(x, colorSet)
        for x in range(384, 384+64):
            strip.setPixelColor(x, colorSet)
        for x in range(512, 512+64):
            strip.setPixelColor(x, colorSet)
        strip.show()


# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()
    ##########
    strip.setBrightness(175)
    colorSet = Color(255,0,0)
    for x in range(0, 64):
        strip.setPixelColor(x, colorSet)
    for x in range(128, 192):
        strip.setPixelColor(x, colorSet)
    for x in range(256, 256+64):
        strip.setPixelColor(x, colorSet)
    for x in range(384, 384+64):
        strip.setPixelColor(x, colorSet)
    for x in range(512, 512+64):
        strip.setPixelColor(x, colorSet)
    strip.show()
    ##########
    while True:
        innerX(strip)

