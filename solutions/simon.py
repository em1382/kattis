c = int(input())
for i in range(c):
    cmd = str(input())
    if cmd.startswith("simon says "):
        print(cmd.split("simon says ")[1])
    else:
        print()
