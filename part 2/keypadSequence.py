import numpy as np
import re
import time

import keypad
import directionalKeypad


def calculate_complexity(final_directional_sequence, sequence):
    sequence_length = len(final_directional_sequence)
    numeric_value_of_sequence = get_numeric_part_of_sequence(sequence)
    return sequence_length * numeric_value_of_sequence


def run(sequence, iterations):
    t0 = time.time()
    directional_sequence = get_keypad_sequence(sequence)
    print(directional_sequence)

    final_sequence = get_dir_keypad_sequence(directional_sequence, iterations)
    print(final_sequence)

    complexity = calculate_complexity(final_sequence, sequence)
    t3 = time.time()
    print("Iteration time: " + str(t3 - t0))
    return complexity


def get_dir_keypad_sequence(sequence, iterations):
    current_sequence = sequence
    last_targets = np.full(iterations, "A", dtype=object)  # Local array
    for iter_idx in range(iterations):
        # Use a list buffer to construct new sequence
        new_sequence = []
        for char in current_sequence:
            result = directionalKeypad.move_position(char, last_targets[iter_idx])
            if result:
                new_sequence.append(result)
                last_targets[iter_idx] = char  # Update last target locally
        current_sequence = ''.join(new_sequence)  # Join once per iteration
    return current_sequence


def get_keypad_sequence(sequence):
    directional_keypad_sequence = ""
    last_char = "A"
    for char in sequence:
        directional_keypad_sequence += keypad.move_position(char, last_char)
        last_char = char
    return directional_keypad_sequence


def get_numeric_part_of_sequence(sequence):
    match = re.search(r'\d+', sequence)
    return int(match.group()) if match else 0
