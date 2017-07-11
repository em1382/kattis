dominant_values = {"A": 11, "K": 4, "Q": 3,
                   "J": 20, "T": 10, "9": 14, "8": 0, "7": 0}
nondom_values = {"A": 11, "K": 4, "Q": 3,
                 "J": 2, "T": 10, "9": 0, "8": 0, "7": 0}
score = 0

n, b = input().split()
for i in range(int(n) * 4):
    card = input()
    if card[1] == b:
        score += dominant_values[card[0]]
    else:
        score += nondom_values[card[0]]

print(score)
