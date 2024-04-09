print("Starting on NRF")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.scanners.keypad import KeysScanner
from kmk.modules.split import Split, SplitSide,SplitType
from kmk.extensions.rgb import RGB, AnimationModes

_KEY_CFG = [
    board.D0,
    board.D1,    
    board.D2,
    board.D3,
]


class MyKeyboard(KMKKeyboard):
    def __init__(self):
        # create and register the scanner
        self.matrix = KeysScanner(
            # require argument:
            pins=_KEY_CFG,
            # optional arguments with defaults:
            value_when_pressed=False,
            pull=True,
            interval=0.02,  # Debounce time in floating point seconds
            max_events=64
        )

keyboard = MyKeyboard()
keyboard.coord_mapping =  [
    0,  1,  2,  3,  4,  5,         
    30, 31, 32, 33, 34, 35,
    6,  7,  8,  9, 10, 11,
    36, 37, 38, 39, 40, 41,
    12, 13, 14, 15, 16, 17,        
    42, 43, 44, 45, 46, 47,
    18, 19, 20, 21, 22, 23,
    48, 49, 50, 51, 52, 53,
    24, 25, 26, 27, 28, 29,
    54, 55, 56, 57, 58, 59,
    60, 61, 62, 63, 64, 65,
    66, 67, 68, 69, 70, 71 
]

split = Split(
    split_side=SplitSide.LEFT,
    split_type=SplitType.UART,
    split_target_left=True,
    data_pin = board.D7,#RX
    data_pin2 = board.D6,#TX
    uart_flip = False
)
keyboard.modules.append(split)
layer0Asignations = [ KC.I]*72
layer0Asignations[0] =  KC.A
layer0Asignations[1] =  KC.B
layer0Asignations[2] =  KC.C
layer0Asignations[3] =  KC.D
layer0Asignations[4] =  KC.E
layer0Asignations[5] =  KC.F
layer0Asignations[6] =  KC.G
layer0Asignations[7] =  KC.H
keyboard.keymap = [
    layer0Asignations
]

rgb = RGB(
    pixel_pin=board.D4, 
    num_pixels=3,
    val_default=100,
    animation_mode = AnimationModes.BREATHING_RAINBOW,
    reverse_animation = True,
    animation_speed=5
)
#rgb.set_hsv_fill(100, 300, 100)
keyboard.extensions.append(rgb)

if __name__ == '__main__':
    keyboard.go()


