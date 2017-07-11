inside = []
outside = []

events = int(input())
for i in range(events):
    event, person = input().split()
    if event == 'entry':
        if person not in inside:
            inside.append(person)
            print(person, 'entered')
        else:
            print(person, 'entered (ANOMALY)')
    elif event == 'exit':
        if person in inside:
            inside.remove(person)
            print(person, 'exited')
        else:
            print(person, 'exited (ANOMALY)')
