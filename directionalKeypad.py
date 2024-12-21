import numpy as np


class DirectionalKeypad:
    KEYPAD = np.array([["", "^", "A"], ["<", "v", ">"]])
    DEFAULT_STARTING_POS = (0, 2)

    def __init__(self):
        self._position = self.DEFAULT_STARTING_POS
        self._last_action = ""

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value

    @property
    def last_action(self):
        return self._last_action

    @last_action.setter
    def last_action(self, value):
        self._last_action = value

    def move_position(self, target_value):
        keypad_row_id, keypad_col_id = self.position
        current_keypad_row = self.KEYPAD[keypad_row_id]

        if target_value in current_keypad_row:
            target_col_index = np.where(current_keypad_row == target_value)[0][0]
            if target_col_index < keypad_col_id:
                self.last_action = "<"
                self.position = (keypad_row_id, keypad_col_id - 1)
                return False
            elif target_col_index > keypad_col_id:
                self.last_action = ">"
                self._position = (keypad_row_id, keypad_col_id + 1)
                return False
            else:
                self.last_action = "A"
                return True
        else:
            target_row_index = np.where(self.KEYPAD == target_value)[0][0]
            if target_row_index < keypad_row_id:
                self.last_action = "^"
                self.position = (keypad_row_id - 1, keypad_col_id)
                return False
            else:
                self.last_action = "v"
                self.position = (keypad_row_id + 1, keypad_col_id)
                return False
