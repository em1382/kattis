sweeps = int(input())
before = list(input())
after = list(input())

for i in range(sweeps):
    for j in range(len(before)):
        if before[j] == '1':
            before[j] = '0'
        else:
            before[j] = '1'

if (before == after):
    print('Deletion succeeded')
else:
    print('Deletion failed')
