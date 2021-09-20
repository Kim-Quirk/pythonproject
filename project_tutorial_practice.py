# import random
# import arcade

# """
# Platformer Game
# """
# import arcade

# # Constants
# SCREEN_WIDTH = 1000
# SCREEN_HEIGHT = 650
# SCREEN_TITLE = "Platformer"
# MOVEMENT_SPEED = 4
# SPRITE_SCALING = 0.5
# GRAVITY = -6
# JUMP = 8


# class MyGame(arcade.Window):
#     """
#     Main application class.
#     """

#     def __init__(self):

#         # Call the parent class and set up the window
#         super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

#         arcade.set_background_color(arcade.csscolor.BISQUE)

#          # Variables that will hold sprite lists
#         self.player_list = None

#         # Set up the player info
#         self.player_sprite = None

#     def setup(self):
#         """Set up the game here. Call this function to restart the game."""
#         # Sprite lists
#         self.player_list = arcade.SpriteList()

#         # Set up the player
#         self.player_sprite = Player(":resources:images/animated_characters/female_person/femalePerson_idle.png", SPRITE_SCALING)
#         self.player_sprite.center_x = 50
#         self.player_sprite.center_y = 0
#         self.player_list.append(self.player_sprite)

#     def on_draw(self):
#         """Render the screen."""

#         arcade.start_render()
#         # Code to draw the screen goes here

#         # Draw all the sprites.
#         self.player_list.draw()
    
#     def on_update(self, delta_time):
#         """ Movement and game logic """

#         # Move the player
#         self.player_list.update()

#     def on_key_press(self, key, modifiers):
#         """Called whenever a key is pressed. """

#         # If the player presses a key, update the speed
#         if key == arcade.key.UP:
#             self.player_sprite.change_y = JUMP
#         elif key == arcade.key.DOWN:
#             self.player_sprite.change_y = -MOVEMENT_SPEED
#         elif key == arcade.key.LEFT:
#             self.player_sprite.change_x = -MOVEMENT_SPEED
#         elif key == arcade.key.RIGHT:
#             self.player_sprite.change_x = MOVEMENT_SPEED

#     def on_key_release(self, key, modifiers):
#         """Called when the user releases a key. """

#         # If a player releases a key, zero out the speed.
#         # This doesn't work well if multiple keys are pressed.
#         # Use 'better move by keyboard' example if you need to
#         # handle this.
#         if key == arcade.key.UP or key == arcade.key.DOWN:
#             self.player_sprite.change_y = GRAVITY
#         elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
#             self.player_sprite.change_x = 0


# class Player(arcade.Sprite):
#     # Player class
#     def update(self):
#         self.center_x += self.change_x
#         self.center_y += self.change_y

#         if self.left < 0:
#             self.left = 0
#         elif self.right > SCREEN_WIDTH - 1:
#             self.right = SCREEN_WIDTH -1
        
#         if self.bottom < 0:
#             self.bottom = 0
#         elif self.top > SCREEN_HEIGHT - 1:
#             self.top = SCREEN_HEIGHT - 1

# def main():
#     """Main method"""
#     window = MyGame()
#     window.setup()
#     arcade.run()


# if __name__ == "__main__":
#     main()