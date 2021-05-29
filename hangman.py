import random
from words import words
import string

def getValidWord(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():

    word = getValidWord(words)
    wordLetters = set(word)
    alphabet = set(string.ascii_uppercase)
    usedLetters = set()
    lives = 6
    while len(wordLetters) > 0 and lives > 0:

        if len(usedLetters) == 0:
            print("You haven't guessed any letter yet.")
        else:
            print("You have guessed these letters: ", " ".join(usedLetters))

        wordList = [letter if letter in usedLetters else "_" for letter in word]

        print("Current word: ", " ".join(wordList))

        userLetter = input("Guess a letter: ").upper()

        if userLetter in alphabet - usedLetters:
            usedLetters.add(userLetter)
            if userLetter in wordLetters:
                wordLetters.remove(userLetter)
            else:
                lives -= 1
                print(f"Your letter is wrong. You have {lives} left")
        elif userLetter in usedLetters:
            print("You have already guessed that letter")
        else:
            print("Invalid character")
    if lives == 0:
        print("Game over. You died!")
    else:
        print("You guessed it!")


hangman()