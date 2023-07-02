## SPDX-FileCopyrightText: 2022 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
from rainbowio import colorwheel
import neopixel
import digitalio

NUMPIXELS = 48# Update this to match the number of LEDs.
SPEED = 0.05  # Increase to slow down the rainbow. Decrease to speed it up.
BRIGHTNESS = 0.99  # A number between 0.0 and 1.0, where 0.0 is off, and 1.0 is max.
TOP_LIGHT_PIN = board.D5
LEFT_LED_PIN = board.D6

BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)

pixels = neopixel.NeoPixel(LEFT_LED_PIN, NUMPIXELS, brightness=BRIGHTNESS, auto_write=False)

top_led  = digitalio.DigitalInOut(TOP_LIGHT_PIN)
top_led.direction = digitalio.Direction.OUTPUT

while True:
    time.sleep(0.5)
    top_led.value = True
    top_led.value = False
    time.sleep(0.5)
    pixels.fill(GREEN)
    pixels.show()
    time.sleep(0.5)
    pixels.fill(RED)
    pixels.show()
    time.sleep(0.5)
    pixels.fill(BLACK)
    pixels.show()
    time.sleep(0.5)
