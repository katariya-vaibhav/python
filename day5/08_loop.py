number = 6
is_prime = False

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            is_prime = False
            break
        else:
            is_prime = True
print(f"{number} - is_prime: {is_prime}")
# Compare this snippet from day5/05_loop.py: