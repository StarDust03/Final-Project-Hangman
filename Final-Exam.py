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
guessesLeft = 7
testString = "-----"
displayWord = " "
'''
for i in range(guessesLeft):
    
    for l in range(len(word)):
        letter = word[l]
        if guess == letter:
            testString = testString.replace(testString[l], guess, 1)
        else:
            testString.replace(testString[l], ".")
    print(testString)
'''
'''
guess = input("Guess a letter: ")
def dashes(testString):
    testString = ""
    for j in range(len(word)):
        testString = testString + "-"
    return testString
'''
def userGuess():
    global guess
    guess = input("Guess a letter: ")
    while(len(guess) != 1):
        guess = input("Guess one letter: ")
        if len(guess) == 1 and guess.islower():
            return guess

def updateWord(guess):
    for i in range(len(word) - 1):
        if guess == word[i]:
            global displayWord
            displayWord = displayWord + guess
        else:
            displayWord = displayWord + testString
    print(displayWord)



userGuess()
updateWord(guess)
print(testString)