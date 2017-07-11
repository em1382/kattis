import sys

nums = []

for line in sys.stdin:
    nums.append(int(line.rstrip()) % 42)

print(len(set(nums)))
