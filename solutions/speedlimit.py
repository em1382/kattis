while True:
    c = int(input())
    if c == -1:
        break

    dist = []
    elap = []

    for i in range(c):
        d, e = str(input()).split()
        dist.append(int(d))
        elap.append(int(e))

    total, last = 0, 0
    for d, e in zip(dist, elap):
        total += d * abs(e - last)
        last = e

    print(total, "miles")
