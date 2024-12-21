import numpy as np
import re

from keypad import Keypad


class KeypadSequence:
    NUMERIC_KEYPAD_ARRAY = np.array([[7, 8, 9], [4, 5, 6], [1, 2, 3], ["", 0, "A"]])
    NUMERIC_KEYPAD_STARTING_POS = (3, 2)
    DIRECTIONAL_KEYPAD_ARRAY = np.array([["", "^", "A"], ["<", "v", ">"]])
    DIRECTIONAL_KEYPAD_STARTING_POS = (0, 2)

    def __init__(self, sequence):
        self._sequence = sequence
        self._complexity = 0

    @property
    def sequence(self):
        return self._sequence

    @property
    def complexity(self):
        return self._complexity

    def calculate_complexity(self, final_directional_sequence):
        sequence_length = get_sequence_length(final_directional_sequence)
        numeric_value_of_sequence = get_numeric_part_of_sequence(self.sequence)
        print(sequence_length, numeric_value_of_sequence)
        self._complexity = sequence_length * numeric_value_of_sequence

    def run(self):
        numeric_keypad = Keypad(self.NUMERIC_KEYPAD_ARRAY, self.NUMERIC_KEYPAD_STARTING_POS)
        directional_keypad1 = Keypad(self.DIRECTIONAL_KEYPAD_ARRAY, self.DIRECTIONAL_KEYPAD_STARTING_POS)
        directional_keypad2 = Keypad(self.DIRECTIONAL_KEYPAD_ARRAY, self.DIRECTIONAL_KEYPAD_STARTING_POS)

        directional_sequence1 = get_keypad_sequence(keypad=numeric_keypad, sequence=self.sequence)
        directional_sequence2 = get_keypad_sequence(keypad=directional_keypad1, sequence=directional_sequence1)
        directional_sequence3 = get_keypad_sequence(keypad=directional_keypad2, sequence=directional_sequence2)

        self.calculate_complexity(directional_sequence3)


def get_keypad_sequence(keypad, sequence):
    directional_keypad_sequence = ""
    for char in sequence:
        while not keypad.move_position(char):
            directional_keypad_sequence += keypad.last_action
        directional_keypad_sequence += keypad.last_action

    print(f"{directional_keypad_sequence}")
    return directional_keypad_sequence


def get_sequence_length(sequence):
    return len(sequence)


def get_numeric_part_of_sequence(sequence):
    match = re.search(r'\d+', sequence)
    if match:
        number = int(match.group())  # Convert the extracted digits to an integer
        return number
    return 0
