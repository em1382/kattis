c = int(input())
for i in range(c):
    com = str(input())

    if com.startswith("Simon says"):
        print(com[11:])
