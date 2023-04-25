import random


def check_numbers(number, attempts):
    for i in range(1, attempts + 1):
        print(f'You have {attempts + 1 - i} attempts.')
        player_guess = int(input('Make a guess. '))
        if player_guess == number:
            return print("You won.")
        elif attempts > 0:
            if number > player_guess:
                print(f'Too low.')
            elif number < player_guess:
                print('Too high.')
    return print("You Loose")

print('Welcome to the Number Guessing Game!.')
print("I'm thinking of a number between 1 and 100.")
computer_number = random.randint(1, 100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == 'easy':
    attempts = 10
    check_numbers(computer_number, attempts)
elif difficulty == 'hard':
    attempts = 5
    check_numbers(computer_number, attempts)
