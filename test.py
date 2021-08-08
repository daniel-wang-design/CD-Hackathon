import arcade

width = 800
height = 400
title = "Test"

class Main(arcade.Window):
    """
    Main game application class
    """
    def __init__(self):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.LIGHT_STEEL_BLUE)
        self.sprite_list = arcade.SpriteList()


    def setup(self):
        temp = Trash("images/3.png", 0.5)
        temp.set_position(0,0 )
        self.sprite_list.append(temp)

    def on_draw(self):
        arcade.start_render()
        self.sprite_list.draw()

class Trash(arcade.Sprite):
    def __init__(self,filename, scale):
        super().__init__(filename=filename, scale=scale)

def main():
    # main method
    window = Main()
    window.setup()
    arcade.run()

main()