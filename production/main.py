import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

# These are the pins on the XIAO RP2040. 
# You will update these later to match exactly how you routed them in KiCad!
keyboard.col_pins = (board.D0, board.D1, board.D2) 
keyboard.row_pins = (board.D3,) 
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Here is where you assign what each of the 3 buttons does
keyboard.keymap = [
    [KC.A, KC.B, KC.C]
]

if __name__ == '__main__':
    keyboard.go()