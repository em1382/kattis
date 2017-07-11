a = ["A", "B", "C"]
b = ["B", "A", "B", "C"]
g = ["C", "C", "A", "A", "B", "B"]
names = ["Adrian", "Bruno", "Goran"]
correct = [0, 0, 0]

M, seq = input(), input()
for i, c in enumerate(seq):
    if a[i % len(a)] == c:
        correct[0] += 1
    if b[i % len(b)] == c:
        correct[1] += 1
    if g[i % len(g)] == c:
        correct[2] += 1

print(max(correct))

for i in range(len(correct)):
    if correct[i] == max(correct):
        print(names[i])
