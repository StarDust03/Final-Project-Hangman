# Lauren Meade
# 3.7.19
# Final Project:


"""
This program here allows a user to play Hangman. It first greats the user saying "Let's play hangman!". Then it tells
the user how many letters long the word is. Then there is a for loop asking the user for some input and an if statement
that compares to see if the letter user entered is in the word. The goal is to get to after the user inputs a letter to
show the blank lines and the letter in those blank lines if the letter is correct. If not it says the user is wrong and
does not input the letter into one of the blank lines but still shows the user what is left in the blank lines.

"""

word = "hello"
print("Let's play hangman! The word you have to guess is", len(word), "letters.")

'''
num_of_guesses = 7
for i in range(num_of_guesses):
    guess = input("Guess a letter: ")
    if guess not in word:
        print("You got it wrong! You lose a limb.")
    else:
        print("You got it right!")
'''
testString = ""
displayString = ""

"""
testString = ""
displayWord = ""

for i in range(guessesLeft):
    
    for l in range(len(word)):
        letter = word[l]
        if guess == letter:
            testString = testString.replace(testString[l], guess, 1)
    displayString = testString
    print(displayString)
        else:
            testString.replace(testString[l], ".")
    print(testString)
"""

guesses_left = 10

def userGuess():
    global guess
    guess = input("Guess a letter: ")
    while(len(guess) != 1):
        guess = input("Guess one letter: ")
        if len(guess) == 1 and guess.islower():
            return guess

def updateWord(guess):
    global testString
    displayWord = ""
    for i in range(len(word)):
        if guess == word[i]:
            displayWord = displayWord + guess
        else:
            displayWord = displayWord + testString[i]
    print(displayWord)

def dashes():
    global testString
    for j in range(len(word)):
        testString = testString + "-"



dashes()
while word != testString and guesses_left > 0:
    userGuess()
    updateWord(guess)
    if guess not in word:
        guesses_left = guesses_left - 1
        print("You got it wrong you have", guesses_left, "!")
    else:
        print("You got it right!You have", guesses_left, "Guesses Left!")
if testString == word:
    print("Yay you win the word was", word, ".")
else:
    print("You lost. The word was", word, ".")


