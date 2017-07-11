while True:
    n = int(input())

    if n == 0:
        break

    names = []

    for i in range(n):
        names.append(str(input()))

    names.sort(key=lambda name: name[:2])
    (print(name) for name in names)
    print("")
