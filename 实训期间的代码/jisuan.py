def sum1(n):
    if 0 <n <= 100:
        return n + sum1(n-1)
    else:
        return 0
print (sum1(100))
