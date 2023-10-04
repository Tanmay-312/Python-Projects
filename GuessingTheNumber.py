import random

record_number_of_guesses = 0
print("Hello, Whats your name?? ")
name = (input("Enter your name here: "))

number = random.randint(10, 30)
print("Hello,", name, "I was thinking of a number from 10 to 30, could you give it a guess???")

while record_number_of_guesses < 6:
    guess = int(input("Enter your guess Here: "))

    record_number_of_guesses = record_number_of_guesses + 1

    if guess < number:
        print("Guess a higher number")
    elif guess > number:
        print("Guess a smaller number")
    elif guess == number:
        print("Lovely, you guessed it right! You took", record_number_of_guesses, "guesses")
        break
    else:
        print("Inside else!")
