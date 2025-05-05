import random

lowest_num = 1
highest_num = 50
guesses = 0
answer = random.randint(lowest_num, highest_num)
is_runnung = True

print('Number guessing game')
print(f"Select a number between {lowest_num} and {highest_num}")

while is_runnung:
    guess = input('Enter your guess: ')
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
    else:
        print('INVALID GUESS')
        print(f"Please select a number between {lowest_num}")