import lib.ezgpio as ezgpio
import time

positions = [7, 11, 12, 13, 15, 16, 18, 22, 29, 31, 32, 33, 35, 36, 37, 38, 40]

pins = {}


for position in positions:
    pin = {}
    print(f'Setting up pin no{position}')
    pin['input'] = ezgpio.input(position)
    pin['position'] = position
    pin['old_state'] = pin['input'].state
    pins[position] = pin

while True:
    for pin in pins.values():
        state = pin['input'].state
        old_state = pin['old_state']
        position = pin['position']
        if state != old_state:
            print(f'Pin {position} changed from {old_state} to {state}')
            pin['old_state'] = state
