userAge = int(input("Enter your age: "))
if userAge < 18:
    print("You are a minor.")
elif userAge < 65:
    print("You are an adult.")
else:  
    print("You are a senior citizen.")