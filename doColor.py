#!/usr/bin/env python3
# rpi_ws281x library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

import time
import sys
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



# Define functions which animate LEDs in various ways.
def colorWipe(strip, color):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()

def fadeIn(strip):
    for x in range(1,brightVal,5):
        strip.setBrightness(x)
        strip.show()
        time.sleep(.07)

def fadeOut(strip):
    for x in range(1,brightVal,5):
        brightLevel = brightVal-x
        strip.setBrightness(brightLevel)
        strip.show()
        time.sleep(.07)
    strip.setBrightness(0)
    strip.show()


# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    # parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    # args = parser.parse_args()
    
    red = int(sys.argv[1])
    green = int(sys.argv[2])
    blue = int(sys.argv[3])
    bright = sys.argv[4]
    pulse = int(sys.argv[5])
    brightVal = int(float(bright) * 255)
    
    print ("ARGS :: ", red, " :: " , green, " :: " , blue, " :: ", bright,  "(",brightVal,") :: " , pulse)

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT,LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()

    while True:
        strip.setBrightness(brightVal)
        strip.show()
        colorWipe(strip, Color(red,green, blue))
        if pulse == 1:
            fadeOut(strip)
            fadeIn(strip)
    
