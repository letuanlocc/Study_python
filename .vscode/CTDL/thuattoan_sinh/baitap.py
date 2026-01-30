digits = [9]
n = len(digits)
if digits[n-1] != 9:
    digits[n-1] += 1
else:
     for k in range(n):
        print(k)
        digits.insert(k,0)
        digits[0] = 1

    