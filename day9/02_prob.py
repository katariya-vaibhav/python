
def debug(func):
    def wrapper(*args , **kwargs):
        args_value = ", ".join([f"{arg} = {arg}" for arg in args])
        kwargs_value = ", ".join([f"{key} = {value}" for key , value in kwargs.items()])
        print(f"Function: {func.__name__}({args_value}, {kwargs_value})")
        return func(*args , **kwargs)
    return wrapper    


@debug
def hello():
    print("Say hello")

@debug
def greetingUser(name , greeting = "Hello"):
    return f"{greeting} {name}!"


hello()
print(greetingUser("John" , greeting="Hi"))