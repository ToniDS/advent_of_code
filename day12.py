from aocd.models import Puzzle
import itertools
from collections import defaultdict
import numpy as np


puzzle = Puzzle(year=2019, day = 16)
data = puzzle.input_data
new_data = data

pattern_original = [ 0, 1, 0, -1]


input_signal= [int(x) for x in list(data)]
input_origin = [int(x) for x in list(data)]

for i in range(1000):
    input_signal.extend(input_origin)


final_after_phases = []
phases = 100

for phase in range(phases):
    print(f"Phase: {phase}")
    final = ""
    for i, element in enumerate(input_signal):
        pattern = []
        for element in pattern_original:
            for j in range(i+1):
                pattern.append(element)
        pattern_first = pattern[1:]
        while len(pattern_first) < len(input_signal):
            pattern_first.extend(pattern)
        zwischensum = 0
        for i, element in enumerate(input_signal):
            zwischensum += element * pattern_first[i]
        final += str(zwischensum)[-1]
    final_after_phases.append(final)
    input_signal = [int(x) for x in list(final_after_phases[phase])]

print(
    final_after_phases[99]
    [int(''.join(final_after_phases[:8])):
    int(''.join(final_after_phases[:8])) +8])
