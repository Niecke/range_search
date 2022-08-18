import random
import csv

#MAX_STEPS_BETWEEN_RANGES = int(1e5)
#MAX_STEPS_IN_RANGE = int(1e5)
#MIN_VALUE = int(1e10)
#MAX_VALUE = int(1e11)-1
MAX_STEPS_BETWEEN_RANGES = int(1e2)
MAX_STEPS_IN_RANGE = int(1e1)
MIN_VALUE = int(1e2)
MAX_VALUE = int(1e3)-1
RANGES_PATH = "ranges.csv"

num_ranges = 0
postion = MIN_VALUE
print(f"Generating ranges from {MIN_VALUE:,} to {MAX_VALUE:,}")
with open(RANGES_PATH, 'w') as ranges_file:
    writer = csv.writer(ranges_file)
    while postion <= MAX_VALUE:
        next_postion = random.randrange(postion, postion + MAX_STEPS_IN_RANGE)

        # next_position can be greater than the MAX_VALUE
        if next_postion > MAX_VALUE:
            next_postion = MAX_VALUE

        print(f"Range: {postion:,} -> {next_postion:,}")
        writer.writerow([postion, next_postion])
        postion = random.randrange(
            next_postion, next_postion + MAX_STEPS_BETWEEN_RANGES)
        num_ranges += 1

    print((f"Ranges generated: {num_ranges}"))
