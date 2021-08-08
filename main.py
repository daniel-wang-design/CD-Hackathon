import arcade
import random

width = 1440
height = 844
title = "Game"

mask = ":resources:images/2.png"
egg = ":resources:images/3.png"
newspaper =":resources:images/4.png"
can = ":resources:images/5.png"
apple = ":resources:images/6.png"
takeout = ":resources:images/7.png"
glassbottle = ":resources:images/8.png"


class Trash(arcade.Sprite):
    def __init__(self, number):
        self.number = number
        self.image_file_name = f"images/{self.number}.png"
        super().__init__(self.image_file_name)


class Main(arcade.Window):
    """
    Main game application class
    """

    def __init__(self):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.LIGHT_STEEL_BLUE)

    def setup(self):
        self.trash = []
        self.trash_original_position = []
        self.alltrash = arcade.SpriteList()
        # mask.position = 50, 50

    def on_draw(self):
        arcade.start_render()
        self.alltrash.draw()

    def on_mouse_press(self, x, y, button, key_modifiers):
        garbage = arcade.get_sprites_at_point((x, y), self.alltrash)
        if len(garbage) > 0:
            self.trash = garbage
            self.trash_original_position = [self.trash[0].position]

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        for x in self.trash:
            x.center_x += dx
            x.center_y += dy

    def on_mouse_release(self, x: float, y: float, button: int,
                         modifiers: int):
        if len(self.trash) == 0:
            return
        self.trash = []

def main():
    # main method
    window = Main()
    window.setup()
    arcade.run()

main()

