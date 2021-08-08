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
        self.pile_mat_list: arcade.SpriteList = arcade.SpriteList()
        pile = arcade.SpriteSolidColor(75, 150, arcade.csscolor.LIGHT_STEEL_BLUE)
        pile.position = 250, 200
        self.pile_mat_list.append(pile)

        self.pile_mat_list: arcade.SpriteList = arcade.SpriteList()
        pile = arcade.SpriteSolidColor(75, 150, arcade.csscolor.LIGHT_STEEL_BLUE)
        pile.position = 400, 200
        self.pile_mat_list.append(pile)

        self.pile_mat_list: arcade.SpriteList = arcade.SpriteList()
        pile = arcade.SpriteSolidColor(75, 150, arcade.csscolor.LIGHT_STEEL_BLUE)
        pile.position = 550, 200
        self.pile_mat_list.append(pile)

        self.piles = [[] for _ in range(3)]

        greenbin = Trash("images/8.png", 0.5)
        bins.set_position(400,200)
        egg = Trash("images/3.png", 0.1)
        egg.set_position(100,100)
        self.sprite_list.append(egg)
        self.sprite_list.append(bins)

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
