import random

lowest_num = 1
highest_num = 50
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print('Python Number Guessing Game')
print(f"Select a number between {lowest_num} and {highest_num}")