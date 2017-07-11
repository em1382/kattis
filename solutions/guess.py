import sys

number_list = list(range(1, 1001))
for i in range(10):
    guess_index = len(number_list) // 2
    print(number_list[guess_index])
    sys.stdout.flush()
    hint = str(input())
    if hint == 'lower':
        number_list = number_list[:guess_index]
    elif hint == 'higher':
        number_list = number_list[guess_index:]
    else:
        break
