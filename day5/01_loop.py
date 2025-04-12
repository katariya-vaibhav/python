numbers = [1, -2, 3, -11, 18, 4, 23, 45, -9]

count = 0

for num in numbers:
    if num > 0:
        count = count + 1
else:
    print("No negative numbers found in the list.")

print(f"positive number count is {count}")