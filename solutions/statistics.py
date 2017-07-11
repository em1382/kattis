import sys
i = 1
for line in sys.stdin:
    x = [int(x) for x in line.split()]
    del x[0]
    print("Case {0}:".format(i), min(x), max(x), (max(x) - min(x)))
    i += 1
