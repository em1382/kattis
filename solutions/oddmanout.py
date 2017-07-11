cases = int(input())
casestr = "Case #{0}:"

for i in range(cases):
    p = int(input())
    line = str(input())
    nums = line.split()
    for x in nums:
        if nums.count(x) < 2:
            print(casestr.format(i + 1), x)
