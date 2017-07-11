def sumDigits(num):
    total = 0
    digits = list(num)
    for d in digits:
        total += int(d)
    return total


while True:
    n = str(input())
    if n == "0":
        break
    i = 0
    while True:
        if sumDigits(str(i * int(n))) == sumDigits(n):
            if i > 10:
                print(i)
                break
        i += 1
