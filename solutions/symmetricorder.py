case = 0
while True:
    c = int(input())
    if c == 0:
        break
    even = []
    odd = []
    for i in range(c):
        name = str(input())
        if i % 2 == 0:
            even.append(name)
        else:
            odd.append(name)

    print("SET", case + 1)
    even.sort(key=len)
    for e in even:
        print(e)
    odd.sort(key=len)
    for o in reversed(odd):
        print(o)

    case += 1
