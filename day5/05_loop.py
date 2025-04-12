str = input("Enter string : ")

for chr in str:
    if str.count(chr) == 1:
        print(f"repeated char is : {chr}")
        break