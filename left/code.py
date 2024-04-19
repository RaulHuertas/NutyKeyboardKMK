print("Starting on NRF")

import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
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


_KEY_CFG = [
    board.D0,
    board.D1,    
    board.D2,
    board.D3,
]

i2c = busio.I2C(scl=board.SCL, sda=board.SDA, frequency=400_000)
mcp = MCP23017(i2c, address=0x20)

statusLED = statusLED(led_pins=[board.D8, board.D9, board.D10])

col_pins = (mcp.get_pin(8), mcp.get_pin(9), mcp.get_pin(10), mcp.get_pin(11), mcp.get_pin(12), mcp.get_pin(13))
row_pins = (mcp.get_pin(2), mcp.get_pin(3), mcp.get_pin(4), mcp.get_pin(5), mcp.get_pin(6), mcp.get_pin(7))


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
    debug_enabled = True
)
keyboard.modules.append(split)
keyboard.extensions.append(statusLED)

layer0Asignations = [ KC.NO]*72
#ROW0
layer0Asignations[0] =  KC.N1
layer0Asignations[1] =  KC.N2
layer0Asignations[2] =  KC.N3
layer0Asignations[3] =  KC.N4
layer0Asignations[4] =  KC.N5
layer0Asignations[5] =  ESKeycodes.OPENING_QUESTION_MARK
layer0Asignations[6] =  ESKeycodes.QUOTE
layer0Asignations[7] =  KC.N6
layer0Asignations[8] =  KC.N7
layer0Asignations[9] =  KC.N8
layer0Asignations[10] =  KC.N9
layer0Asignations[11] =  KC.N0
#ROW1
layer0Asignations[12] =  KC.Q
layer0Asignations[13] =  KC.W
layer0Asignations[14] =  KC.E
layer0Asignations[15] =  KC.R
layer0Asignations[16] =  KC.T
layer0Asignations[17] =  KC.NO
layer0Asignations[18] =  ESKeycodes.PIPE
layer0Asignations[19] =  KC.Y
layer0Asignations[20] =  KC.U
layer0Asignations[21] =  KC.I
layer0Asignations[22] =  KC.O
layer0Asignations[23] =  KC.P
#ROW2

layer0Asignations[24] =  KC.A
layer0Asignations[25] =  KC.S
layer0Asignations[26] =  KC.D
layer0Asignations[27] =  KC.F
layer0Asignations[28] =  KC.G
layer0Asignations[29] =  KC.NO
layer0Asignations[30] =  KC.LGUI
layer0Asignations[31] =  KC.H
layer0Asignations[32] =  KC.J
layer0Asignations[33] =  KC.K
layer0Asignations[34] =  KC.L
layer0Asignations[35] =  ESKeycodes.NTIL
#ROW3
layer0Asignations[36] =  KC.Z
layer0Asignations[37] =  KC.X
layer0Asignations[38] =  KC.C
layer0Asignations[39] =  KC.V
layer0Asignations[40] =  KC.B
layer0Asignations[41] =  KC.NO
layer0Asignations[42] =  ESKeycodes.LESSER_GREATER
layer0Asignations[43] =  KC.N
layer0Asignations[44] =  KC.M
layer0Asignations[45] =  KC.COMMA
layer0Asignations[46] =  KC.DOT
layer0Asignations[47] =  KC.SLASH
#ROW4
layer0Asignations[48] =  KC.LCTRL
layer0Asignations[49] =  KC.LSHIFT
layer0Asignations[50] =  KC.LALT
layer0Asignations[51] =  KC.SPACE
layer0Asignations[52] =  KC.OPENING_BRAQUETS
layer0Asignations[53] =  KC.CLOSING_BRAQUETS
layer0Asignations[54] =  KC.DELETE
layer0Asignations[55] =  KC.BSPACE
layer0Asignations[56] =  KC.ENTER
layer0Asignations[57] =  KC.PSCREEN
layer0Asignations[58] =  KC.UP
layer0Asignations[59] =  KC.PAUSE
#ROW5
layer0Asignations[60] =  KC.AUDIO_VOL_DOWN
layer0Asignations[61] =  KC.AUDIO_MUTE
layer0Asignations[62] =  KC.AUDIO_VOL_UP
layer0Asignations[63] =  KC.TAB
layer0Asignations[64] =  KC.TILDE_DIERESIS
layer0Asignations[65] =  KC.PLUS
layer0Asignations[66] =  KC.ESCAPE
layer0Asignations[67] =  KC.NO
layer0Asignations[68] =  KC.RALT
layer0Asignations[69] =  KC.LEFT
layer0Asignations[70] =  KC.DOWN
layer0Asignations[71] =  KC.RIGHT





keyboard.keymap = [
    layer0Asignations
]

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

keyboard.extensions.append(MediaKeys())


if __name__ == '__main__':
    keyboard.go()


