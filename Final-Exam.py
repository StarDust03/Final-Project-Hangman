# Lauren Meade
# 3.7.19
# Final Project:


"""
project explanation

"""

string = "hello"
print("Let's play hangman! The word you have to guess is", len(string), "letters.")


num_of_guesses = 7
for i in range(num_of_guesses):
    guess = input("Guess a letter: ")
    if guess not in string:
        print("You got it wrong! You lose a limb.")
    else:
        print("You got it right!")