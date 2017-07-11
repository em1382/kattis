cups = [1, 0, 0]


def A():
    cups[1], cups[0] = cups[0], cups[1]


def B():
    cups[2], cups[1] = cups[1], cups[2]


def C():
    cups[2], cups[0] = cups[0], cups[2]

for c in str(input()):
    if c == "A":
        A()
    elif c == "B":
        B()
    elif c == "C":
        C()

print(cups.index(1) + 1)
