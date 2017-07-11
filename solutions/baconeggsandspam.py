food = {}

days = int(input())

while days != 0:
    for i in range(days):
        item = str(input())
        food[item.split(" ")[0]] = item.split(" ")[1:]

    orders = {}
    output = []

    for key in food:
        for item in food[key]:
            if item not in orders:
                orders[item] = []

    for key in orders:
        for item in food:
            if key in food[item]:
                orders[key].append(item)

        orders[key].sort()
        output.append(key + " " + " ".join(orders[key]))

    output.sort()

    for item in output:
        print(item)

    print("")

    food = {}

    days = int(input())
