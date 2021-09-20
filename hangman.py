import random
import keyboard
import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Starting Template"
WIDTH = 800
HEIGHT = 600

def randomWordGen():
    word_file = open("words.txt", "r")
    words = word_file.readlines()
    word_file.close()
    random_word = random.choice(words)
    return random_word

WORD = randomWordGen()

def checkGuess(guess, word):
    correct = False
    for index in range(0, len(word)):
        if guess == word[index]:
            correct = True
    return correct

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)


    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        # Create your sprites and sprite lists here
        pass

    def on_draw(self):
        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()
        arcade.draw_text("Press a letter to guess a letter in the random word.", WIDTH/2, HEIGHT/2,
                         arcade.color.BLACK, font_size=15, anchor_x="center")

        # Call draw() on all your sprite lists below

    # def on_update(self, delta_time):
    #     """
    #     All the logic to move, and the game logic goes here.
    #     Normally, you'll call update() on the sprite lists that
    #     need it.
    #     """
    #     pass

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://arcade.academy/arcade.key.html
        """
        arcade.draw_text("Guess: " + keyboard.read_key(), WIDTH/2, HEIGHT/2,
                         arcade.color.BLACK, font_size=30, anchor_x="center")
        guess = keyboard.read_key()
        # guess = input("Enter your guess: ")
        correct = checkGuess(guess, WORD)

        if correct == True:
            arcade.draw_text("Correct!", WIDTH/2, HEIGHT/2,
                         arcade.color.BLACK, font_size=30, anchor_x="center")
        else:
            arcade.draw_text("Incorrect!", WIDTH/2, HEIGHT/2,
                         arcade.color.BLACK, font_size=30, anchor_x="center")



def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()