# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Internal RGB LED rainbow example"""
import time
import board
from rainbowio import colorwheel

if hasattr(board, "APA102_SCK"):
    import adafruit_dotstar

    led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
else:
    import neopixel

    led = neopixel.NeoPixel(board.NEOPIXEL, 1)

# Initial values
led.brightness = 0.1  # Start with lower brightness
i = 0

total_time = 30
steps = 100  # Number of steps in the sequence
step_duration = total_time / steps  # Time for each step

# brightness and frequency variables
min_brightness = 0.1
max_brightness = 1.0
brightness_step = (max_brightness - min_brightness) / steps

# Sequence 2 and 3 parameters
pulse_steps = 50
pulse_duration = 15  # Run the pulse sequence for 15 seconds
pulse_step_duration = pulse_duration / pulse_steps

# Colors for pulse effect seq1
color1 = (255, 0, 0)  # Red
color2 = (0, 0, 255)  # Blue

# Colors for seq2
color3 = (255, 255, 255)  # White
color4 = (255, 255, 0)    # Yellow

# Midpoint to switch colors
color_switch_point = pulse_steps // 2

while True:
    # First sequence: Color wheel with increasing brightness
    for step in range(steps):  # Loop for running the colorwheel
        led.brightness = min_brightness + step * brightness_step

        # Cycle through colors with frequency change (faster near the end)
        i = (i + 10 + step) % 256  # Increase the speed as step increases
        led.fill(colorwheel(i))

        # Delay which speeds up as time increases
        time.sleep(step_duration * (1 - step / steps))
    # Second sequence: Pulse effect between red and blue
    for pulse_step in range(pulse_steps):
        # Calculate intermediate brightness level for pulsing
        pulse_brightness = min_brightness + abs(
            (pulse_step % (pulse_steps // 2)) - pulse_steps // 4
        ) * (max_brightness / (pulse_steps // 4))

        # Alternate between two colors
        if pulse_step % 2 == 0:
            led.fill(color1)
        else:
            led.fill(color2)

        # Set the brightness level
        led.brightness = pulse_brightness

        # Sleep to control the pulse speed
        time.sleep(pulse_step_duration)
    #Third sequence: Pulse effect between white and yellow (same code as above sequence)
    for pulse_step in range(pulse_steps):
        pulse_brightness = min_brightness + abs(
            (pulse_step % (pulse_steps // 2)) - pulse_steps // 4
        ) * (max_brightness / (pulse_steps // 4))

        if pulse_step % 2 == 0:
            led.fill(color3)
        else:
            led.fill(color4)

        led.brightness = pulse_brightness
        time.sleep(pulse_step_duration)