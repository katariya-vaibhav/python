number = 5
fact = 1

while number > 0:
    print(f"Current number: {number}, Current factorial: {fact}")
    fact = fact * number
    number = number - 1

print(f"Final factorial: {fact}")