import keypadSequence
import time
import cProfile

ITERATIONS = 2

SEQUENCES = ["780A", "846A", "965A", "386A", "638A"]

def run():
    t0 = time.time()
    total_complexity = 0
    for sequence in SEQUENCES:
        total_complexity += keypadSequence.run(sequence, ITERATIONS)
    t1 = time.time()

    print(total_complexity)
    total = t1 - t0
    print(total)


if __name__ == "__main__":
    run()
    # cProfile.run('run()')
