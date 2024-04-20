print("Starting on NRF")

import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
#from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.scanners.keypad import KeysScanner
from kmk.modules.split import Split, SplitSide,SplitType
#from kmk.extensions.rgb import RGB, AnimationModes
from kmk.extensions.statusled import statusLED
from adafruit_mcp230xx.mcp23017 import MCP23017
import digitalio
from digitalio import DigitalInOut, Direction, Pull
import busio
import kmk.scanners.digitalio
from snKeycodes import ESKeycodes
from kmk.extensions.media_keys import MediaKeys
from keyAssignations import assignKeys
from kmk.modules.layers import Layers
from kmk.modules.holdtap import HoldTap
from kmk.modules.mouse_keys import MouseKeys



i2c = busio.I2C(scl=board.SCL, sda=board.SDA, frequency=1_000_000)
mcp = MCP23017(i2c, address=0x20)
holdtap = HoldTap()

statusLED = statusLED(led_pins=[board.D8, board.D9, board.D10])

col_pins = (mcp.get_pin(8), mcp.get_pin(9), mcp.get_pin(10), mcp.get_pin(11), mcp.get_pin(12), mcp.get_pin(13))
row_pins = (mcp.get_pin(2), mcp.get_pin(3), mcp.get_pin(4), mcp.get_pin(5), mcp.get_pin(6), mcp.get_pin(7))

class MCPKeyboard(KMKKeyboard):
    def __init__(self, colPins, rowPins, diodeOrientation):
        # create and register the scanner
        self.matrix = kmk.scanners.digitalio.MatrixScanner(
            cols=colPins,
            rows=rowPins,
            diode_orientation=diodeOrientation,
            pull=digitalio.Pull.UP,
            rollover_cols_every_rows=None, # optional
            
        )


#keyboard = MyKeyboard()
keyboard = MCPKeyboard( row_pins, col_pins, DiodeOrientation.ROW2COL)
keyboard.coord_mapping =  [
    0,  1,  2,  3,  4,  5, 
    36, 37, 38, 39, 40, 41,
    6,  7,  8,  9, 10, 11,
    42, 43, 44, 45, 46, 47,
    12, 13, 14, 15, 16, 17,
    48, 49, 50, 51, 52, 53,
    18, 19, 20, 21, 22, 23,
    54, 55, 56, 57, 58, 59,
    24, 25, 26, 27, 28, 29,
    60, 61, 62, 63, 64, 65,
    30, 31, 32, 33, 34, 35,
    66, 67, 68, 69, 70, 71 
]

split = Split(
    split_side=SplitSide.LEFT,
    #split_side=None,
    split_type=SplitType.UART,
    split_target_left=True,
    data_pin = board.D7,#RX
    data_pin2 = board.D6,#TX
    uart_flip = False,
    debug_enabled = False
)

#keyboard.modules.append(holdtap)
keyboard.modules.append(split)
keyboard.modules.append(Layers())

keyboard.extensions.append(statusLED)
keyboard.extensions.append(MediaKeys())
keyboard.modules.append(MouseKeys())
keyboard.debug_enabled = False


keyboard.keymap = assignKeys()

#rgb = RGB(
#    pixel_pin=board.D4, 
#    num_pixels=3,
#    val_default=100,
#    animation_mode = AnimationModes.BREATHING_RAINBOW,
#    reverse_animation = True,
#    animation_speed=5
#)
#rgb.set_hsv_fill(100, 300, 100)
#keyboard.extensions.append(rgb)



if __name__ == '__main__':
    keyboard.go()


