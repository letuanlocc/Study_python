def sum(i,n):
    if n == 1:
        return i
    else:
        return sum(i + n , n - 1)
n = 100
i = 1
print(sum(1,n))