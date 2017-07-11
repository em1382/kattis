import math

t = int(input())
for i in range(t):
    daily = int(input())
    print(math.ceil(daily / 400))
