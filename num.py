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
        if guess < lowest_num or guess > highest_num:
            print("Your guess is out of range")
            print(f"Please select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too low, try again!")
        elif guess > answer:
            print("Too high, try again!")
        else:
            print(f"CORRECT!, you guessed right")
            print(f"the right answer is {answer}")
            print(f"Number of guesses: {guesses}")
            is_runnung = False
    else:
        print('INVALID GUESS')
        print(f"Please select a number between {lowest_num} and {highest_num}")