#### Setup Section ###
import random

# We'll learn about how this line of code works later in the course - for now just know it loads the colored text
from colorama import Fore, Back, Style

# Introduction to the program
def intro():
  print("==============================================================")
  print("Welcome to Word PLay!")
  print("==============================================================")
  print("")
  print("You have five tries to get the word correct")
  print("You must enter a word that if SIX CHARACTERS long")
  print("If a letter is in the correct place, it will be green")
  print("If a letter is in the word but NOT in the correct place it will be yellow")
  print("If the letter is NOT in the word, it will be red")
  print("")

# Function that prints out a letter with a colorful background
def printColorfulLetter(letter, isLetterInWord, isLetterInCorrectPlace = False):
  if(not isLetterInWord):
    print(Back.RED + Fore.WHITE + f" {letter} ", end="")
  else:
    if(isLetterInCorrectPlace):
      print(Back.LIGHTGREEN_EX + Fore.WHITE + f" {letter} ", end="")
    else:
      print(Back.LIGHTYELLOW_EX + Fore.BLACK + f" {letter} ", end="")

# Display a guess, where each letter is color-coded by it's accuracy
def printGuessAccuracy(guess, actual):
  count = 0
  for index in range(6):
    letter = guess[index]
    if(letter in actual):
      if(letter == actual[index]):
        printColorfulLetter(letter, True, True)
      else:
        printColorfulLetter(letter, True, False)
    else:
      printColorfulLetter(letter, False, False)
    print(Style.RESET_ALL + " ", end="")
  print("")

# TO-DO: Write a Function that takes in a six-lettered word from the user
def sixLetterGuess():
  print("Enter a six-lettered word")
  guess = input(": ")
  invalid = True
  while (invalid):
    # Check for validity
    if (guess.isalpha() == True and len(guess) == 6):
      invalid = False
    else:
      print("Invalid Entry: Please enter a six-lettered word")
      guess = input(": ")
  return guess

### Main Program ###
intro()
# Boring!
# actual = "health"
# Lets spice it up a bit
wordList = ["health", "safari", "friend", "flower"]
actual = random.choice(wordList)
# Helps for debug
#print(actual)

for x in range(5):
  guess = sixLetterGuess()
  printGuessAccuracy(guess, actual)
  if (guess == actual):
    break
