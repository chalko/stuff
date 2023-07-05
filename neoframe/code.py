import time
import board
from rainbowio import colorwheel
import neopixel
import digitalio
from analogio import AnalogIn


print('start')
NUMPIXELS = 48# Update this to match the number of LEDs.
SPEED = 0.05  # Increase to slow down the rainbow. Decrease to speed it up.
BRIGHTNESS = 0.99  # A number between 0.0 and 1.0, where 0.0 is off, and 1.0 is max.
TOP_LIGHT_PIN = board.NEOPIXEL7
LEFT_LED_PIN = board.NEOPIXEL0

BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)


PIR_PIN = board.D24   # Pin number connected to PIR sensor output wire.

# Setup digital input for PIR sensor:
pir = digitalio.DigitalInOut(PIR_PIN)
pir.direction = digitalio.Direction.INPUT

pixels = neopixel.NeoPixel(LEFT_LED_PIN, NUMPIXELS, brightness=BRIGHTNESS, auto_write=False)

top_led  = digitalio.DigitalInOut(TOP_LIGHT_PIN)
top_led.direction = digitalio.Direction.OUTPUT

board_led = digitalio.DigitalInOut(board.LED)
board_led.direction = digitalio.Direction.OUTPUT


dist_in = AnalogIn(board.A0)

# Main loop that will run forever:
old_value = pir.value
while True:
    pir_value = pir.value
    distRaw  = dist_in.value
    #print("A0: %f" % distRaw)

    if pir_value:
        # PIR is detecting movement! Turn on LED.
        # Check if this is the first time movement was
        # detected and print a message!
        if not old_value:
            print('Motion detected!')
            distRaw  = dist_in.value
            print("A0: %f" % distRaw)  # write raw value to REPL
            board_led.value = True
            pixels.fill(RED)
            pixels.show()

    else:
        # PIR is not detecting movement. Turn off LED.
        # Again check if this is the first time movement
        # stopped and print a message.
        if old_value:
            print('Motion ended!')
            board_led.value = False
            pixels.fill(BLUE)
            pixels.show()
            time.sleep(.5)
            pixels.fill(BLACK)
            pixels.show()
    old_value = pir_value
