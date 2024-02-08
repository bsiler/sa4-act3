number = 10
guesses_left = 5
print("I'm thinking of a number...")
guess = input("What number am I thinking of? ")
guesses_left -= 1

while guess != str(number):
    if guess == 'q' or guesses_left == 0:
        print(f"Sorry! The number was {number}.")
        exit()
    print(f"You have " + str(guesses_left) + " guess(es) remaining.")
    guess = input("Try again: ")
    guesses_left -= 1
print("Congratulations! You guessed the right number.")