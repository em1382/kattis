import sys
words = {}
total = 0
num_words, num_desc = str(input()).split(" ")
for i in range(int(num_words)):
    word, value = str(input()).split(" ")
    words[word] = value

for line in sys.stdin:
    if line == ".\n":
        print(total)
        total = 0
    for w in line.rstrip().split():
        if w in words:
            total += int(words[w])
