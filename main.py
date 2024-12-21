from keypadSequence import KeypadSequence

SEQUENCES = ["780A", "846A", "965A", "386A", "638A"]

if __name__ == "__main__":
    total_complexity = 0
    for sequence in SEQUENCES:
        keypad_sequence = KeypadSequence(sequence)
        keypad_sequence.run()
        total_complexity += keypad_sequence.complexity

    print(total_complexity)
