import sys
import statistics

name = ""
nums = []

for line in sys.stdin:
    for v in line.split(" "):
        try:
            nums.append(float(v))
        except ValueError:
            name += v + " "

    print(round(statistics.mean(nums), 6), name.strip())

    name = ""
    nums = []
