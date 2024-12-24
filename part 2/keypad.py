import numpy as np

NUMERIC_KEYPAD_ARRAY = np.array([[7, 8, 9], [4, 5, 6], [1, 2, 3], ["", 0, "A"]])
NUMERIC_KEYPAD_STARTING_POS = (3, 2)
NULL_COORDINATES = (3, 0)


def move_position(target_value, last_target_value):
    return compute_most_efficient_path(last_target_value, target_value)


def compute_most_efficient_path(last_target_value, target_value):
    position = np.where(NUMERIC_KEYPAD_ARRAY == last_target_value)
    position = (position[0][0], position[1][0])
    null_value = ""
    destination_path = ""
    next_action = ""
    while True:
        keypad_row_id, keypad_col_id = position

        current_keypad_row = NUMERIC_KEYPAD_ARRAY[keypad_row_id, :]
        current_keypad_col = NUMERIC_KEYPAD_ARRAY[:, keypad_col_id]

        target_coordinates = np.where(NUMERIC_KEYPAD_ARRAY == target_value)

        target_col_index = target_coordinates[1][0]
        target_row_index = target_coordinates[0][0]

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
            return destination_path + "A"
