userName  = "vaibhav"

def greetUser():
    # userName = "vaibhav1"
    print("Hello", userName)

greetUser()
print("Hello", userName)



def closreFun(num):
    def innerFun(num2):
        return num ** num2
    return innerFun

closure = closreFun(2) # closure is a function that takes one argument and returns another function
# closure function return innerFun function with num (its takes all necessary variables from the outer function used in inner function)
print(closure(3)) # 2^3 = 8