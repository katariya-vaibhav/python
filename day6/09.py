# def even_gen(limit):
#     for i in range(2 , limit + 1 , 2):
#         # if i % 2 == 0:
#             # print(i)
#         return i # its return only first number and exit the loop and function

# print(even_gen(15))
# even_gen(25)
# even_gen(50)


def even_gen(limit):
    for i in range(2 , limit+1, 2):
        yield i

for num in even_gen(10):
    print(num)