import sys
names = []
for line in sys.stdin:
    names.append(line.rstrip().split(" "))

names = sorted(names, key=lambda name: (name[1], name[0]))
first_names = [i[0] for i in names]

for name in names:
    if first_names.count(name[0]) > 1:
        print(name[0], name[1])
    else:
        print(name[0])
