import random
import keyboard
# import arcade

def startGame():
    over = False
    word = randomWordGen()
    display = ["_"] * len(word)
    string = printWord(display)
    print("Welcome to Hangman! \nYou have six lives. Every incorrect guess will take away a life. Once your lives reach zero, you will lose the game.")
    print(string)  
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
            print("Please enter only one letter. Do not enter numbers or symbols.")
    guess = guess.lower()
    return guess

def updateLives(incorrect_guess):
    lives = 6
    lives -= len(incorrect_guess)
    return lives
    
def runGame(word, correct_guess, incorrect_guess, over):
    guess = enterLetter()
    correct = checkGuess(guess, word)
    if correct == True:
        print("Correct!")
        print("\n")
        correct_guess.append(guess)
    else:
        print("Incorrect!")
        print("\n")
        incorrect_guess.append(guess)
        print("Incorrect guesses: " + str(incorrect_guess))
    lives = updateLives(incorrect_guess)
    print("Lives: " + str(lives))
    display = ["_"] * len(word)
    for i in range(0, len(word)):
        for j in range(0, len(correct_guess)):
            if word[i] == correct_guess[j]:
                display[i] = correct_guess[j]
    string = printWord(display)
    print(string)
    if str(string) == str(word[0:-1]):
        over = True
        print("Congrats! You win! The game will now end.")
    if lives == 0:
        over =  True
        print("Uh-oh, you died! Game over.")
    return over
    

def printWord(array):
    string = ""
    for i in range(0, len(array) - 1):
        string += array[i]
    return string


def main():
    """ Main method """
    result = startGame()
    over = result[0]
    word = result[1]
    correct_guess = result[2]
    incorrect_guess = result[3]
    
    while over == False:
        over = runGame(word, correct_guess, incorrect_guess, over)

main()