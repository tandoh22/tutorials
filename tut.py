# while loop

num = int(input("enter a number between 1 and 10: "))
while num < 1 or num > 10:
    print(f"{num} is invalid")
    num = int(input("enter a number between 1 and 10: "))
print(f"{num} is valid, you are good to go!")