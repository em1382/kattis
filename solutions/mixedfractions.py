while True:
    num, den = str(input()).split(" ")
    if (num == "0" and den == "0"):
        break

    num = int(num)
    den = int(den)
    wn = num // den
    remain = num % den

    print(wn, remain, "/", den)
