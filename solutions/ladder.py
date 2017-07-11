import math
h, v = [float(x) for x in input().split()]
print(math.ceil(h / math.sin(math.radians(v))))
