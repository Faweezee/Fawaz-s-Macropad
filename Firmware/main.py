import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.macros import Macros

keyboard = KMKKeyboard()
macros = Macros()
keyboard.modules.append(macros)


keyboard.col_pins = (board.D6, board.D7, board.D8, board.D9)
keyboard.row_pins = (board.D0, board.D1, board.D2)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

# --- KEYMAPPING ---
# Row 1: Esc, Copy (Ctrl+C), Paste (Ctrl+V), Cut (Ctrl+X)
# Row 2: Screenshot (PrintScreen), Undo (Ctrl+Z), Redo (Ctrl+Y), Save All (Ctrl+Shift+S)
# Row 3: Lock Screen (Win+L), Comment (Ctrl+/), Search (Ctrl+F), Win+Tab

keyboard.keymap = [
    [
        # Row 1
        KC.ESC,    KC.LCTRL(KC.C),    KC.LCTRL(KC.V),    KC.LCTRL(KC.X),
        # Row 2
        KC.PSCR,   KC.LCTRL(KC.Z),    KC.LCTRL(KC.Y),    KC.LCTRL(KC.LSFT(KC.S)),
        # Row 3
        KC.LGUI(KC.L), KC.LCTRL(KC.SLSH), KC.LCTRL(KC.LSFT(KC.F)), KC.LGUI(KC.TAB),
    ]
]

if __name__ == '__main__':
    keyboard.go()