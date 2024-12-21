from numericKeypad import NumericKeypad
from directionalKeypad import DirectionalKeypad

if __name__ == "__main__":
    sequence = "029A"
    numeric_keypad = NumericKeypad()

    directional_keypad_sequence1 = ""
    for char in sequence:
        while not numeric_keypad.move_position(char):
            directional_keypad_sequence1 += numeric_keypad.last_action
        directional_keypad_sequence1 += numeric_keypad.last_action

    print(directional_keypad_sequence1)

    directional_keypad = DirectionalKeypad()

    directional_keypad_sequence2 = ""
    for char in directional_keypad_sequence1:
        while not directional_keypad.move_position(char):
            directional_keypad_sequence2 += directional_keypad.last_action
        directional_keypad_sequence2 += directional_keypad.last_action

    print(directional_keypad_sequence2)

