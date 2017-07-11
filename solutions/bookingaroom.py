from random import choice
r, n = [int(x) for x in input().split()]
if r == n:
    print('too late')
else:
    rooms = list(range(1, r + 1))
    for i in range(n):
        rooms.remove(int(input()))
    if len(rooms) > 0:
        print(choice(rooms))
    else:
        print('too late')
