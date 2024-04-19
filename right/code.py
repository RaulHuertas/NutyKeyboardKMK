print("Starting on S3")

import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.scanners.keypad import KeysScanner
from kmk.modules.split import Split, SplitSide,SplitType
from adafruit_mcp230xx.mcp23017 import MCP23017
from kmk.modules.layers import Layers
import digitalio
from digitalio import DigitalInOut, Direction, Pull

import kmk.scanners.digitalio

_KEY_CFG = [
    board.IO1, board.IO2,board.IO3, board.IO4
]

i2c = busio.I2C(scl=board.IO6, sda=board.IO5, frequency=400_000)
mcp = MCP23017(i2c, address=0x20)

class MyKeyboard(KMKKeyboard):
    def __init__(self):
        # create and register the scanner
        self.matrix = KeysScanner(
            # require argument:
            pins=_KEY_CFG,
            # optional arguments with defaults:
            value_when_pressed=False,
            pull=True,
            interval=0.015,  # Debounce time in floating point seconds
            max_events=64
        )

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


keyboard = MCPKeyboard(row_pins, col_pins, DiodeOrientation.ROW2COL)
keyboard.coord_mapping =  [
    #0,  1,  2,  3,  4,  5, 
    #6,  7,  8,  9, 10, 11,
    #12, 13, 14, 15, 16, 17,
    #18, 19, 20, 21, 22, 23,
    #24, 25, 26, 27, 28, 29,
    #30, 31, 32, 33, 34, 35,

    36, 37, 38, 39, 40, 41,
    42, 43, 44, 45, 46, 47,
    48, 49, 50, 51, 52, 53,
    54, 55, 56, 57, 58, 59,
    60, 61, 62, 63, 64, 65,
    66, 67, 68, 69, 70, 71 
]


split = Split(
    split_side=SplitSide.RIGHT,
    #split_side=None,
    split_type=SplitType.UART,
    split_target_left=True,
    data_pin = board.IO44,#RX
    data_pin2 = board.IO43,#TX
    uart_flip = False,
    debug_enabled = True
)
#layer = Layers
#keyboard.modules.append(layer)
keyboard.modules.append(split)

#keyboard.col_pins = col_pins
#keyboard.row_pins = row_pins

#keyboard.diode_orientation = DiodeOrientation.ROW2COL
keyboard.debug_enabled = True


layer0Asignations = [ KC.NO]*72
# layer0Asignations[0] =  KC.I
# layer0Asignations[1] =  KC.J
# layer0Asignations[2] =  KC.K
# layer0Asignations[3] =  KC.L
# layer0Asignations[4] =  KC.M
# layer0Asignations[5] =  KC.N
# layer0Asignations[6] =  KC.O
# layer0Asignations[7] =  KC.P
keyboard.keymap = [
    layer0Asignations
]

if __name__ == '__main__':
    keyboard.go()


