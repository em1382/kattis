N, M = (int(x) for x in input().split())
left = M - N
message = "Dr. Chaz {0}{1}{2} piece{3} of chicken{4}!"

if left >= 0:
    if left == 1:
        print(message.format("will have ", str(1), "", "", " left over"))
    else:
        print(message.format("will have ", str(left), "", "s", " left over"))
elif left < 0:
    if left == -1:
        print(message.format("needs ", str(1), " more", "", ""))
    else:
        print(message.format("needs ", str(abs(left)), " more", "s", ""))
