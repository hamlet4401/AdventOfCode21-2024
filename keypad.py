import numpy as np


class Keypad:

    def __init__(self, keypad_array, starting_position):
        self._keypad = keypad_array
        self._position = starting_position
        self._last_action = ""

    @property
    def keypad(self):
        return self._keypad

    @property
    def position(self):
        return self._position

    @property
    def last_action(self):
        return self._last_action

    def move_position(self, target_value):
        keypad_row_id, keypad_col_id = self.position
        current_keypad_row = self.keypad[keypad_row_id]

        if target_value in current_keypad_row:
            target_col_index = np.where(current_keypad_row == target_value)[0][0]
            if target_col_index < keypad_col_id:
                self._last_action = "<"
                self._position = (keypad_row_id, keypad_col_id-1)
                return False
            elif target_col_index > keypad_col_id:
                self._last_action = ">"
                self._position = (keypad_row_id, keypad_col_id + 1)
                return False
            else:
                self._last_action = "A"
                return True
        else:
            target_row_index = np.where(self.keypad == target_value)[0][0]
            if target_row_index < keypad_row_id:
                self._last_action = "^"
                self._position = (keypad_row_id - 1, keypad_col_id)
                return False
            else:
                self._last_action = "v"
                self._position = (keypad_row_id + 1, keypad_col_id)
                return False
