# while loop

name = input("enter your name: ")
while name == "":
    print("you did not enter your name!")
    name = input('enter your name: ')
print(f"hello {name}!")