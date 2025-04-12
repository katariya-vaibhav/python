num = int(input("Enter Number"))

for i in range(1, 11):
    if i == 5:
        continue
    print(f"{num} * {i} = {num*i}")
    
