# mine-lamp
I need a glowing minecraft lamp, with the following requirements

- [ ] Controlled by a board that supports micro-python
- [ ] USB powered
- [ ] Super Bright
- [ ] RGBW color range


Things that I considered but left out:

- wifi - while neat, this addds a lot of complexity to the code, and since it is USB powered you can easily control it from your laptop if you want it to change colors when some event happens
- battery - That seems useful, but it would need to charge and since the purpose is to be bright, it would drain fast

# 3D Print Designs
- Starting from this: https://www.thingiverse.com/thing:524925

The idea is to print that, with a solid base and maybe a hole for the USB cable to be routed through. The base will need to be altered so that it has small pegs to hold the GEMMA and Jewl in place. Then we print a very thin insert to go inside that cube to act as a light difuser. Although the thin printed cube is ideal, I might end up printing very thing squares that are glued/placed inside the outer cube. A bit of paint to get the outer cube to look like a minecraft cube and all will be great!

# Parts List
- Adafruit GEMMA M0 - https://www.adafruit.com/product/3501
- Neopixel Jewl (7 x 5050 RGBW LEDS) - https://www.adafruit.com/product/2858


