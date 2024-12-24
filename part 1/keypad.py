import numpy as np


class Keypad:
    def __init__(self, keypad_array, starting_position):
        self._keypad = keypad_array
        self._position = starting_position
        self._last_action = ""
        self._repeated_movement = 0
        self._next_action = ""

    @property
    def keypad(self):
        return self._keypad

    @property
    def position(self):
        return self._position

    @property
    def last_action(self):
        return self._last_action

    @property
    def repeated_movement(self):
        return self._repeated_movement

    def move_position(self, target_value):
        null_value = ""
        keypad_row_id, keypad_col_id = self._position

        current_keypad_row = self._keypad[keypad_row_id, :]
        current_keypad_col = self._keypad[:, keypad_col_id]

        target_coordinates = np.where(self._keypad == target_value)
        null_coordinates = np.where(self._keypad == null_value)

        target_col_index = target_coordinates[1][0]
        target_row_index = target_coordinates[0][0]

        null_col_index = null_coordinates[1][0]
        null_row_index = null_coordinates[0][0]

        left = target_col_index < keypad_col_id and (
                    keypad_col_id < null_col_index or target_col_index > null_col_index or null_value not in current_keypad_row)
        right = target_col_index > keypad_col_id and (
                    keypad_col_id > null_col_index or target_col_index < null_col_index or null_value not in current_keypad_row)
        down = target_row_index > keypad_row_id and (
                    keypad_row_id > null_row_index or target_row_index < null_row_index or null_value not in current_keypad_col)
        up = target_row_index < keypad_row_id and (
                    keypad_row_id < null_row_index or target_row_index > null_row_index or null_value not in current_keypad_col)
        if ((self._next_action == "" and target_col_index < keypad_col_id) or self._next_action == "<") and left:
            self._last_action = "<"
            if abs(keypad_col_id - target_col_index) > 1:
                self._next_action = "<"
            else:
                self._next_action = ""
            self._position = (keypad_row_id, keypad_col_id - 1)
            if self._repeated_movement != 0:
                self._repeated_movement -= 1
            return False
        if ((self._next_action == "" and target_row_index > keypad_row_id) or self._next_action == "v") and down:
            self._last_action = "v"
            if abs(keypad_row_id - target_row_index) > 1:
                self._next_action = "v"
            else:
                self._next_action = ""
            self._position = (keypad_row_id + 1, keypad_col_id)
            return False
        if ((self._next_action == "" and target_row_index < keypad_row_id) or self._next_action == "^") and up:
            self._last_action = "^"
            if abs(keypad_row_id - target_row_index) > 1:
                self._next_action = "^"
            else:
                self._next_action = ""
            self._position = (keypad_row_id - 1, keypad_col_id)
            return False
        if ((self._next_action == "" and target_col_index > keypad_col_id) or self._next_action == ">") and right:
            self._last_action = ">"
            if abs(keypad_col_id - target_col_index) > 1:
                self._next_action = ">"
            else:
                self._next_action = ""
            self._position = (keypad_row_id, keypad_col_id + 1)
            return False
        else:
            self._last_action = "A"
            return True
