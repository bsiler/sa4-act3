number = 10

print("I'm thinking of a number...")
guess = input("What number am I thinking of? ")


while guess != str(number):
    if guess == 'q':
        print(f"Sorry! The number was {number}.")
        exit()
    guess = input("Try again: ")
print("Congratulations! You guessed the right number.")