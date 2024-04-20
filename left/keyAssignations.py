from kmk.keys import KC
from snKeycodes import ESKeycodes
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.layers import Layers
from kmk.modules.mouse_keys import MouseKeys

def assignKeys ():
    
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
    layer0Asignations[41] =  KC.MO(1)
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
    layer0Asignations[52] =  ESKeycodes.OPENING_BRAQUETS
    layer0Asignations[53] =  ESKeycodes.CLOSING_BRAQUETS
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
    layer0Asignations[64] =  ESKeycodes.TILDE_DIERESIS
    layer0Asignations[65] =  KC.PLUS
    layer0Asignations[66] =  KC.ESCAPE
    layer0Asignations[67] =  KC.FD(0)
    layer0Asignations[68] =  KC.RALT
    layer0Asignations[69] =  KC.LEFT
    layer0Asignations[70] =  KC.DOWN
    layer0Asignations[71] =  KC.RIGHT




    layer1Asignations = [ KC.NO]*72
    #ROW0
    layer1Asignations[0] =  KC.F1
    layer1Asignations[1] =  KC.F2
    layer1Asignations[2] =  KC.F3
    layer1Asignations[3] =  KC.F4
    layer1Asignations[4] =  KC.F5
    layer1Asignations[5] =  KC.F11
    layer1Asignations[6] =  KC.F12
    layer1Asignations[7] =  KC.F6
    layer1Asignations[8] =  KC.F7
    layer1Asignations[9] =  KC.F8
    layer1Asignations[10] =  KC.F9
    layer1Asignations[11] =  KC.F10
    #ROW1
    layer1Asignations[12] =  KC.TRANSPARENT
    layer1Asignations[13] =  KC.TRANSPARENT
    layer1Asignations[14] =  KC.TRANSPARENT
    layer1Asignations[15] =  KC.TRANSPARENT
    layer1Asignations[16] =  KC.TRANSPARENT
    layer1Asignations[17] =  KC.TRANSPARENT
    layer1Asignations[18] =  KC.TRANSPARENT
    layer1Asignations[19] =  KC.MW_UP
    layer1Asignations[20] =  KC.MB_LMB
    layer1Asignations[21] =  KC.MS_UP
    layer1Asignations[22] =  KC.MB_RMB
    layer1Asignations[23] =  KC.MB_MMB
    
    #ROW2
    layer1Asignations[24] =  KC.TRANSPARENT
    layer1Asignations[25] =  KC.TRANSPARENT
    layer1Asignations[26] =  KC.TRANSPARENT
    layer1Asignations[27] =  KC.TRANSPARENT
    layer1Asignations[28] =  KC.TRANSPARENT
    layer1Asignations[29] =  KC.TRANSPARENT
    layer1Asignations[30] =  KC.TRANSPARENT
    layer1Asignations[31] =  KC.MW_DOWN
    layer1Asignations[32] =  KC.MS_LEFT
    layer1Asignations[33] =  KC.MS_DOWN
    layer1Asignations[34] =  KC.MS_RIGHT
    layer1Asignations[35] =  KC.TRANSPARENT
    #ROW3
    layer1Asignations[36] =  KC.TRANSPARENT
    layer1Asignations[37] =  KC.TRANSPARENT
    layer1Asignations[38] =  KC.TRANSPARENT
    layer1Asignations[39] =  KC.TRANSPARENT
    layer1Asignations[40] =  KC.TRANSPARENT
    layer1Asignations[41] =  KC.TRANSPARENT
    layer1Asignations[42] =  KC.TRANSPARENT
    layer1Asignations[43] =  KC.TRANSPARENT
    layer1Asignations[44] =  KC.TRANSPARENT
    layer1Asignations[45] =  KC.TRANSPARENT
    layer1Asignations[46] =  KC.TRANSPARENT
    layer1Asignations[47] =  KC.TRANSPARENT
    #ROW4
    layer1Asignations[48] =  KC.TRANSPARENT
    layer1Asignations[49] =  KC.TRANSPARENT
    layer1Asignations[50] =  KC.TRANSPARENT
    layer1Asignations[51] =  KC.TRANSPARENT
    layer1Asignations[52] =  KC.TRANSPARENT
    layer1Asignations[53] =  KC.TRANSPARENT
    layer1Asignations[54] =  KC.TRANSPARENT
    layer1Asignations[55] =  KC.TRANSPARENT
    layer1Asignations[56] =  KC.TRANSPARENT
    layer1Asignations[57] =  KC.TRANSPARENT
    layer1Asignations[58] =  KC.TRANSPARENT
    layer1Asignations[59] =  KC.TRANSPARENT
    #ROW5
    layer1Asignations[60] =  KC.TRANSPARENT
    layer1Asignations[61] =  KC.TRANSPARENT
    layer1Asignations[62] =  KC.TRANSPARENT
    layer1Asignations[63] =  KC.TRANSPARENT
    layer1Asignations[64] =  KC.TRANSPARENT
    layer1Asignations[65] =  KC.TRANSPARENT
    layer1Asignations[66] =  KC.TRANSPARENT
    layer1Asignations[67] =  KC.FD(0) #home
    layer1Asignations[68] =  KC.TRANSPARENT
    layer1Asignations[69] =  KC.TRANSPARENT
    layer1Asignations[70] =  KC.TRANSPARENT
    layer1Asignations[71] =  KC.TRANSPARENT


    return  [
        layer0Asignations,
        layer1Asignations
    ]



