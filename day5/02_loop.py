number = int(input("Enter Number"))
sum = 0

for i in range(1,number+1):
    if i%2 == 0:
        sum+=1

print(f"sum of even number is {sum}")