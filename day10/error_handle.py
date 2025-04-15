try:
    file = open("day10/invalid_file.txt", "w")
    file.write("Hello, World!")
finally:
    file.close()
    print("File closed successfully.")
    
    
with open ("day10/invalid_file.txt", "w") as file:
    file.write("Hello, World!")
    print("File closed successfully.")
    
    
    