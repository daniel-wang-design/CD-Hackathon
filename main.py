import arcade

width = 800
height = 500
title = "Game"

class Main(arcade.Window):
    """
    Main game application class
    """
    def __init__(self):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLUE)

    def setup(self):
        pass

    def on_draw(self):
        arcade.start_render()

def main():
    # main method
    window = Main()
    window.setup()
    arcade.run()

main()