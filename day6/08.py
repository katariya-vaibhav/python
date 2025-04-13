def print_kwargs(**kwargs):
    # print(kwargs) # This will print the entire dictionary of keyword arguments
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(name="Alice", age=30, city="New York")
print_kwargs(name="Bob", age=25, country="USA")
print_kwargs(name="Charlie", age=35, occupation="Engineer")
print_kwargs(name="David", age=28, hobby="Reading")
print_kwargs(name="Eve", age=22, favorite_color="Blue")
print_kwargs(name="Frank", age=40, favorite_food="Pizza")