import numpy as np

from keypad import Keypad

NUMERIC_KEYPAD_ARRAY = np.array([[7, 8, 9], [4, 5, 6], [1, 2, 3], ["", 0, "A"]])
NUMERIC_KEYPAD_STARTING_POS = (3, 2)
DIRECTIONAL_KEYPAD_ARRAY = np.array([["", "^", "A"], ["<", "v", ">"]])
DIRECTIONAL_KEYPAD_STARTING_POS = (0, 2)


def get_keypad_sequence(keypad, sequence):
    directional_keypad_sequence = ""
    for char in sequence:
        while not keypad.move_position(char):
            directional_keypad_sequence += keypad.last_action
        directional_keypad_sequence += keypad.last_action

    print(f"{directional_keypad_sequence}")
    return directional_keypad_sequence


if __name__ == "__main__":
    sequence = "029A"
    numeric_keypad = Keypad(NUMERIC_KEYPAD_ARRAY, NUMERIC_KEYPAD_STARTING_POS)
    directional_keypad = Keypad(DIRECTIONAL_KEYPAD_ARRAY, DIRECTIONAL_KEYPAD_STARTING_POS)

    directional_sequence1 = get_keypad_sequence(keypad=numeric_keypad, sequence=sequence)
    directional_sequence2 = get_keypad_sequence(keypad=directional_keypad, sequence=directional_sequence1)
