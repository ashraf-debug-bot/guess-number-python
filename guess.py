import random
# importing random module to generate random numbers


def pas(x):
    random_number = random.randint(1, x)
    guess = 0

    while guess != random_number:
        guess = int(input(f"Guess the number between 1 to {x}: "))
        if guess < random_number:
            print(f"Sorry,guess again {guess} is too low")
        elif guess > random_number:
            print(f"Sorry,guess again {guess} is too high")
    print(f'yay, congrats!! you have guessed correctly this number is {random_number}')


pas(10)
