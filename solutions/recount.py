candidates = {}
name = ''
while name != '***':
    name = input()
    if name not in candidates:
        candidates[name] = 1
    else:
        candidates[name] += 1
maximum = max(candidates, key=candidates.get)
if list(candidates.values()).count(candidates[maximum]) > 1:
    print('Runoff!')
else:
    print(maximum)
