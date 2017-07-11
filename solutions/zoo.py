animals = {}
list_count = 0

count = int(input())
while count != 0:
    for i in range(count):
        animal = input().split()[-1].lower()
        if animal in animals:
            animals[animal] += 1
        else:
            animals[animal] = 1
    list_count += 1
    print('List {0}:'.format(list_count))
    for key, value in sorted(animals.items()):
        print('{0} | {1}'.format(key, value))
    animals = {}
    count = int(input())
