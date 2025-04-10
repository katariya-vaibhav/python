class Car:
    def __repr__(self):
        return "Car('Tesla', 'Model 3')"
    
    def __str__(self):
        return "Tesla Model 3"


# Testing with a custom class / object
c = Car()
print(repr(c))  # Output: Car('Tesla', 'Model 3')
print(str(c))   # Output: Tesla Model 3
print(c)        # Output: Tesla Model 3
# ------------------------------------------------------ 
print(c.__repr__())  # Output: Car('Tesla', 'Model 3')
print(c.__str__())   # Output: Tesla Model 3



# Testing with a string
x = 'hello'
print("repr(x):", repr(x))
print("str(x):", str(x))
print("print(x):", end=" ")
print(x)



