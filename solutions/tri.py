nums = str(input()).split()
nums = list(map(int, nums))

num1, num2, num3 = nums[0], nums[1], nums[2]

if num1 + num2 == num3:
    print("{0}+{1}={2}".format(num1, num2, num3))
elif num1 - num2 == num3:
    print("{0}-{1}={2}".format(num1, num2, num3))
elif num1 * num2 == num3:
    print("{0}*{1}={2}".format(num1, num2, num3))
elif num1 / num2 == num3:
    print("{0}/{1}={2}".format(num1, num2, num3))
elif num1 == num2 + num3:
    print("{0}={1}+{2}".format(num1, num2, num3))
elif num1 == num2 - num3:
    print("{0}={1}-{2}".format(num1, num2, num3))
elif num1 == num2 * num3:
    print("{0}={1}*{2}".format(num1, num2, num3))
elif num1 == num2 / num3:
    print("{0}={1}/{2}".format(num1, num2, num3))
