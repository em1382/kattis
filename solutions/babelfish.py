import sys

dic = {}

for line in sys.stdin:
    line = line.rstrip("\n")

    if line != "" and " " in line:
        dic[line.split(" ")[1]] = line.split(" ")[0]
    elif line in dic:
        print(dic[line])
    else:
        if line != "":
            print("eh")
