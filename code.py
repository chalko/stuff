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


PIR_PIN = board.D9   # Pin number connected to PIR sensor output wire.

# Setup digital input for PIR sensor:
pir = digitalio.DigitalInOut(PIR_PIN)
pir.direction = digitalio.Direction.INPUT

pixels = neopixel.NeoPixel(LEFT_LED_PIN, NUMPIXELS, brightness=BRIGHTNESS, auto_write=False)

top_led  = digitalio.DigitalInOut(TOP_LIGHT_PIN)
top_led.direction = digitalio.Direction.OUTPUT

# Main loop that will run forever:
old_value = pir.value
while True:
    pir_value = pir.value
    if pir_value:
        # PIR is detecting movement! Turn on LED.
        # Check if this is the first time movement was
        # detected and print a message!
        if not old_value:
            print('Motion detected!')
            pixels.fill(RED)
            pixels.show()

    else:
        # PIR is not detecting movement. Turn off LED.
        # Again check if this is the first time movement
        # stopped and print a message.
        if old_value:
            print('Motion ended!')
            pixels.fill(BLUE)
            pixels.show()
            time.sleep(.5)
            pixels.fill(BLACK)
            pixels.show()
    old_value = pir_value
