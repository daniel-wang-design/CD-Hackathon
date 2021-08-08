import arcade

width = 800
height = 400
title = "Test"

class Level_2(arcade.Window):
    """
    Main game application class
    """
    def __init__(self):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.LIGHT_STEEL_BLUE)
        self.sprite_list = arcade.SpriteList()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        pressed_item = arcade.get_sprites_at_point((x,y), self.sprite_list)
        if len(pressed_item) > 0:


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
    window = Level_2()
    window.setup()
    arcade.run()

main()