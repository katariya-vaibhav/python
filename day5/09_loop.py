items = ["apple" , "banana" , "cherry" , "mango" , "orange" , "apple"]
unique_item = set()

for item in items:
    if item in unique_item:
        continue
    unique_item.add(item)
print(unique_item)