encoded = str(input())
decoded = ''
i = 0
while i < len(encoded):
    if encoded[i] in 'aeiou':
        decoded += encoded[i]
        i += 2
    else:
        decoded += encoded[i]
    i += 1
print(decoded)
