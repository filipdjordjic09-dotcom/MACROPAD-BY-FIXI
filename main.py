import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DirectPins
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

# Podrška za Rotary Encoder
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

# 4 Tastera spojeni direktno na GPIO pinove (P26, P27, P28, P29)
keyboard.matrix = DirectPins(
    pins=[board.P26, board.P27, board.P28, board.P29],
)

# Pinovi za enkoder: Pin A (P6), Pin B (P7), Klik taster (P0)
encoder_handler.pins = (
    (board.P6, board.P7, board.P0),
)

# Enkoder kontrole:
# Okretanje ulevo -> Stišavanje (Volume Down)
# Okretanje udesno -> Pojačavanje (Volume Up)
# Pritisak na enkoder -> Mute (Isključivanje zvuka)
encoder_handler.map = [
    ((KC.VOLD, KC.VOLU, KC.MUTE),),
]

# Mapiranje 4 tastera:
keyboard.keymap = [
    [
        KC.LCTL(KC.C),  # Taster 1: Copy (Ctrl + C)
        KC.LCTL(KC.V),  # Taster 2: Paste (Ctrl + V)
        KC.LCTL(KC.Z),  # Taster 3: Undo (Ctrl + Z)
        KC.LCTL(KC.Y),  # Taster 4: Redo (Ctrl + Y)
    ]
]

if __name__ == '__main__':
    keyboard.go()