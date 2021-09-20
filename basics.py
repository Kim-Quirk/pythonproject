import random
import keyboard
# import arcade

def startGame():
    over = False
    word = randomWordGen()
    print("_ " * len(word))   
    print("Welcome to Hangman!")
    correct_guess = []
    incorrect_guess = []
    return over, word, correct_guess, incorrect_guess
    

def randomWordGen():
    word_file = open("words.txt", "r")
    words = word_file.readlines()
    word_file.close()
    random_word = random.choice(words)
    return random_word

def checkGuess(guess, word):
    correct = False
    for index in range(0, len(word)):
        if guess == word[index]:
            correct = True
    return correct

def enterLetter():
    # print("Enter your guess.")
    # guess = keyboard.read_key()
    guess = "No guess"
    while len(guess) > 1:
        guess = input("Enter your guess: ")
        if len(guess) > 1:
            "Please enter only one letter. You cannot enter numbers or symbols."
    return guess
    
def runGame(word, correct_guess, incorrect_guess):
    guess = enterLetter()
    correct = checkGuess(guess, word)
    if correct == True:
        print("Correct!")
        correct_guess.append(guess)
    else:
        print("Incorrect!")
        incorrect_guess.append(guess)
    display = ""
    for i in range(0, len(word)):
        for j in range(0, len(correct_guess)):
            if word[i] == correct_guess[j]:
                display += correct_guess[j]
            else:
                display += "_"




def main():
    """ Main method """
    result = startGame()
    over = result[0]
    word = result[1]
    correct_guess = result[2]
    incorrect_guess = result[3]
    
    while over == False:
        runGame(word, correct_guess, incorrect_guess)

main()
