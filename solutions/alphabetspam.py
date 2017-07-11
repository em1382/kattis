line = str(input())

low = up = sym = ws = 0

for c in line:
    if c.isupper():
        up += 1
    elif c.islower():
        low += 1
    elif not c.isalpha() and c != '_':
        sym += 1
    elif c == '_':
        ws += 1

print(1.0 * ws / len(line))
print(1.0 * low / len(line))
print(1.0 * up / len(line))
print(1.0 * sym / len(line))
