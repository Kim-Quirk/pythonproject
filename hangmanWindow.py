from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import Qt
import sys
import random

# Initlize arrays to hold the user's incorrect and correct guesses
correct_guess = []
incorrect_guess = []

# A random word generator.
# It reads from a file and selects a random word from the list.
def randomWordGen():
    word_file = open("words.txt", "r")
    words = word_file.readlines()
    word_file.close()
    random_word = random.choice(words)
    return random_word

# Initilize the random word vairable
word = randomWordGen()

# Converts an array to a string
def listToString(list): 
    string = "" 
    for i in list: 
        string += i  
    return string

# Figures out how many lives the user has left.
def getLives():
    lives = 6 #Start out with six lives
    lives -= len(incorrect_guess) #How ever many wrong guesses you have made determines your remaining lives
    return lives

#Check the user's guess against the random word
def checkGuess(guess, word):
    correct = False
    #Loop through each letter in the random word
    for index in range(0, len(word)):
        #compare the letter guessed
        if guess == word[index]:
            correct = True #If they match, the guess was correct!
    return correct

# Gets the string read for display
def printWord(array):
    string = ""
    # Cycles through, eleminating the newline character stored at the end
    for i in range(0, len(array) - 1):
        string += array[i]
    return string

# Creates a display version of the string
def displayWord(array):
    string = ""
    for i in range(0, len(array) - 1):
        string += array[i]
        string += " " # This is the main difference, it adds a space between each underscore to improve readability
    return string

# The window class from PyQt5
class MyWindow(QMainWindow):
    
    # Initilize the window class
    def __init__(self):
        
        super(MyWindow, self).__init__()
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle("Hangman!")
        self.initUI(word)

        # Detect a key press event (or a guess formt he user)
    def keyPressEvent(self, event):
        guess = event.text()
        guess = guess.lower() #Make sure the guess is lower case
        correct = checkGuess(guess, word) # Check the guess/keyboard input
        runGame(guess, correct, self) # Run the game!

    # Initilize the window display
    def initUI(self, word):
        display = ["_"] * len(word)
        displayS = listToString(display)
        displaySpaces = displayWord(displayS)

        # Show the underscores for each letter
        self.display = QtWidgets.QLabel(self)
        self.display.setText(displaySpaces)
        self.display.move(15, 200)

        # Display game isntructions
        self.directions = QtWidgets.QLabel(self)
        self.directions.setText("Welcome to Hangman!\n\nYou have six lives. Every incorrect guess will take \naway a life. Once your lives reach zero, you will \nlose the game.\n\nHint: None of the words will contain any special\ncharacters or numbers.")
        self.directions.move(100, 5)

        # Display a list of incorrect guesses
        guess = listToString(incorrect_guess)
        self.guesses = QtWidgets.QLabel(self)
        self.guesses.setText("Incorrect guesses: ")
        self.guesses.move(100, 150)

        # Display the hangman!
        self.hang = QtWidgets.QLabel(self)
        self.hang.setText("  ___\n |     |\n       |\n       |\n       |\n")
        self.hang.move(15, 5)

        # Display the number of lives remaining
        self.lives = QtWidgets.QLabel(self)
        self.lives.move(100, 180)
        self.lives.setText("Lives: 6")

        # Initilize the game over text, but keep it empty
        self.end = QtWidgets.QLabel(self)
        self.end.move(100, 150)
        self.end.setText("")

        # Update lives
        self.updateLives(word)

    # Update the in correct guess list
    def updateGuess(self):
        guess = listToString(incorrect_guess)
        self.guesses.setText("Incorrect guesses: " + guess)
        self.guesses.move(100, 150)
        self.update()
    
    # Update the underscore placeholder display
    def updateDisplay(self, display):
        self.display.setText(display)
        self.update()
    
    # Update the number of lives
    def updateLives(self, word):
        lives = getLives()
        # Switch between pre-made hangman displays to slowly draw the stick figure
        if lives == 0:
            self.hang.setText("  ___\n |    |\n O   |\n-|-  |\n/ \   |\n")
        if lives == 1:
            self.hang.setText("  ___\n |     |\n O    |\n-|-   |\n/      |\n")
        if lives == 2:
            self.hang.setText("  ___\n |     |\n O    |\n-|-   |\n       |\n")
        if lives == 3:
            self.hang.setText("  ___\n |     |\n O    |\n-|    |\n       |\n")
        if lives == 4:
            self.hang.setText("  ___\n |     |\n O    |\n |     |\n       |\n")
        if lives == 5:
            self.hang.setText("  ___\n |     |\n O    |\n       |\n       |\n")
        if lives == 6:
             self.hang.setText("  ___\n |     |\n       |\n       |\n       |\n")
        self.hang.adjustSize()
        self.lives.setText("Lives: " + str(lives))
        self.lives.adjustSize()
        self.update()
        return lives
    
    # End the game!
    def endGame(self, end):
        self.lives.setText("")
        self.guesses.setText("")
        self.directions.setText("") # Makes the extra text vanish and display an end screen
        self.end.setText("Game over! You " + end)
        self.end.adjustSize()

    # Updates all displays
    def update(self):
        self.hang.adjustSize()
        self.lives.adjustSize()
        self.display.adjustSize()
        self.guesses.adjustSize()
        self.end.adjustSize()
        self.directions.adjustSize()
# Run the game
def runGame(guess, correct, win):
    if correct == True:
        correct_guess.append(guess) #Keep track of correct guesses
    else:
        incorrect_guess.append(guess)
        win.updateGuess() #Keep track of incorrect guesses and update the window
    lives = win.updateLives(word)
    display = ["_"] * len(word) #Create the underscore place holder display
    for i in range(0, len(word)):
        for j in range(0, len(correct_guess)):
            if word[i] == correct_guess[j]:
                display[i] = correct_guess[j] #If the word's letter matches the guesses letter, replace that display position with the letter
    
    # Some string/array conversions to make everything look and run nice
    string = printWord(display)
    stringSpaces = listToString(display)
    displaySpaces = displayWord(stringSpaces)
    
    # Update the underscore display
    win.updateDisplay(displaySpaces)
    end = "err" #Set the end to "error" because the game isn't over yet!
    if str(string) == str(word[0:-1]):
        end = "win." #If the display (without the spaces) matches the randomly generated word, you've won!
        win.endGame(end)
    if lives <= 0:
        end = "lose." # If you run out of lives, you have lost and died
        win.endGame(end)

# Start the window and run
def window():
    app = QApplication(sys.argv)
    win = MyWindow()    
    win.show()
    sys.exit(app.exec_())
    
window()