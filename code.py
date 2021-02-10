import board
import neopixel
import time
from digitalio import DigitalInOut, Direction, Pull
from adafruit_debouncer import Debouncer

pixpin = board.D1
numpix = 7
buttonpin = board.D0

btnio = DigitalInOut(buttonpin)
btnio.direction = Direction.INPUT
btnio.pull = Pull.UP
btn = Debouncer(btnio)

pixels = neopixel.NeoPixel(pixpin, numpix, brightness=.9, pixel_order=neopixel.RGBW)

pixels.fill((255, 0, 0, 0))
pixels.write()

toggle = 1
modes = [
    (255,0,0,0),
    (0,255,0,0),
    (0,0,255,0),
    (0,0,0,255)
    ]
    
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)
    
def cont(btn):
    while btn.value == False:
        for i in range(255):
            pixels.fill(wheel(i))
            pixels.write()
            time.sleep(.01)
            btn.update()
            if btn.value:
                break
        

def button_push():
    global toggle
    global modes
    pixels.fill(modes[toggle])
    pixels.write()
    toggle+=1
    if toggle >= len(modes):
        toggle = 0

while True:
    btn.update()
    if btn.fell:
        button_push()
        time.sleep(0.2)
        btn.update()
        if btn.value == False:
            time.sleep(1)
            btn.update()
            if btn.value == False:
                cont(btn)