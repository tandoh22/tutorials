name = input('what is your name? ')
print(f"hello {name}!")
birth_year = int(input('enter your birth year: '))
age = 2025 - birth_year 
status = "you are an adult, please sign up!" if age >= 18 else "you are not qualified to sign up, you are still minor"
print(status)