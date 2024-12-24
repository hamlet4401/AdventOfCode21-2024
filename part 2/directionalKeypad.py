import numpy as np

REVERSE_ARROW_ACTIONS = {"<": ">", ">": "<", "^": "v", "v": "^"}
MOVEMENT_COORDINATES = {"<": (0, -1), "^": (-1, 0), "v": (1, 0), ">": (0, 1), "A": (0, 0)}
COORDINATES = {"A": (0, 2), "^": (0, 1), "<": (1, 0), ">": (1, 2), "v": (1, 1)}
DIRECTIONAL_KEYPAD_ARRAY = np.array([["", "^", "A"], ["<", "v", ">"]])
DIRECTIONAL_KEYPAD_STARTING_POS = (0, 2)
NULL_COORDINATES = (0, 0)
LUT = {}


def move_position(target_value, last_target_value):
    lut_key = "".join([last_target_value, target_value])
    return LUT.get(lut_key, compute_most_efficient_path(last_target_value, target_value, LUT, lut_key))


def compute_most_efficient_path(last_target_value, target_value, lut, lut_key):
    position = COORDINATES[last_target_value]
    null_value = ""

    destination_path = ""
    next_action = ""
    target_coordinates = np.where(DIRECTIONAL_KEYPAD_ARRAY == target_value)

    target_col_index = target_coordinates[1][0]
    target_row_index = target_coordinates[0][0]
    while True:
        keypad_row_id, keypad_col_id = position

        current_keypad_row = DIRECTIONAL_KEYPAD_ARRAY[keypad_row_id, :]
        current_keypad_col = DIRECTIONAL_KEYPAD_ARRAY[:, keypad_col_id]

        # Most efficient route conditions
        no_repetition = next_action == ""
        non_null_row = null_value not in current_keypad_row
        non_null_col = null_value not in current_keypad_col
        left_condition = target_col_index < keypad_col_id and (
                keypad_col_id < NULL_COORDINATES[1] or target_col_index > NULL_COORDINATES[1] or non_null_row)
        right_condition = target_col_index > keypad_col_id and (
                keypad_col_id > NULL_COORDINATES[1] or target_col_index < NULL_COORDINATES[1] or non_null_row)
        down_condition = target_row_index > keypad_row_id and (
                keypad_row_id > NULL_COORDINATES[0] or target_row_index < NULL_COORDINATES[0] or non_null_col)
        up_condition = target_row_index < keypad_row_id and (
                keypad_row_id < NULL_COORDINATES[0] or target_row_index > NULL_COORDINATES[0] or non_null_col)

        if last_target_value == target_value:
            lut[lut_key] = "A"
            return "A"
        elif next_action == "<" or (no_repetition and left_condition):
            destination_path += "<"
            next_action = "<" if abs(keypad_col_id - target_col_index) > 1 else ""
            position = (keypad_row_id, keypad_col_id - 1)
        elif next_action == "v" or (no_repetition and down_condition):
            destination_path += "v"
            next_action = "v" if abs(keypad_row_id - target_row_index) > 1 else ""
            position = (keypad_row_id + 1, keypad_col_id)
        elif next_action == "^" or (no_repetition and up_condition):
            destination_path += "^"
            next_action = "^" if abs(keypad_row_id - target_row_index) > 1 else ""
            position = (keypad_row_id - 1, keypad_col_id)
        elif next_action == ">" or (no_repetition and right_condition):
            destination_path += ">"
            next_action = ">" if abs(keypad_col_id - target_col_index) > 1 else ""
            position = (keypad_row_id, keypad_col_id + 1)
        else:
            lut[lut_key] = destination_path + "A"
            lut[target_value + last_target_value] = reverse_destination_path(destination_path) + "A"
            return lut[lut_key]


def reverse_destination_path(destination_path):
    return "".join(REVERSE_ARROW_ACTIONS[action] for action in reversed(destination_path))
