c = int(input())
for i in range(c):
    animal = ""
    animal_sounds = []
    fox_sounds = []

    sounds = list(str(input()).split(" "))

    while True:
        animal = str(input())
        if "what" in animal:
            break
        s = animal.split(" goes ")[1]
        animal_sounds.append(s)

    for s in sounds:
        if s not in animal_sounds:
            fox_sounds.append(s)

    print(" ".join(fox_sounds))
