def sum_digits(n):
    count = 0
    n = str(n)
    for d in n:
        count += int(d)
    return count


L = int(input())
D = int(input())
X = int(input())
digits_sum_to_x = []
for i in range(L, D + 1):
    if sum_digits(i) == X:
        digits_sum_to_x.append(i)
print(min(digits_sum_to_x))
print(max(digits_sum_to_x))
