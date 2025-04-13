def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    

print(factorial(5)) # 120
print(factorial(6)) # 720
print(factorial(7)) # 5040
print(factorial(8)) # 40320