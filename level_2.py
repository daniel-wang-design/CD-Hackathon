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
        self.counter = 0

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        pressed_items = arcade.get_sprites_at_point((x, y), self.sprite_list)
        if len(pressed_items) > 0:
            self.counter += 1
            return

    def setup(self):
        self.sprite_list_1 = arcade.SpriteList()
        self.sprite_list_2 = arcade.SpriteList()
        self.sprite_list_3 = arcade.SpriteList()
        self.sprite_list_4 = arcade.SpriteList()
        self.sprite_list_5 = arcade.SpriteList()

        self.pair1()
        self.pair2()
        self.pair3()
        self.pair4()
        self.pair5()

    def pair1(self):
        temp = Trash("images/11.png", 0.1)
        temp.set_position(200, 200)
        self.sprite_list_1.append(temp)
        temp = Trash("images/12.png", 0.1)
        temp.set_position(600, 200)
        self.sprite_list_1.append(temp)

    def pair2(self):
        temp = Trash("images/14.png", 0.1)
        temp.set_position(200, 200)
        self.sprite_list_2.append(temp)
        temp = Trash("images/15.png", 0.1)
        temp.set_position(600, 200)
        self.sprite_list_2.append(temp)

    def pair3(self):
        temp = Trash("images/17.png", 0.1)
        temp.set_position(200, 200)
        self.sprite_list_3.append(temp)
        temp = Trash("images/18.png", 0.1)
        temp.set_position(600, 200)
        self.sprite_list_3.append(temp)

    def pair4(self):
        temp = Trash("images/20.png", 0.1)
        temp.set_position(200, 200)
        self.sprite_list_4.append(temp)
        temp = Trash("images/21.png", 0.1)
        temp.set_position(600, 200)
        self.sprite_list_4.append(temp)

    def pair5(self):
        temp = Trash("images/23.png", 0.1)
        temp.set_position(133, 200)
        self.sprite_list_5.append(temp)
        temp = Trash("images/24.png", 0.1)
        temp.set_position(400, 200)
        self.sprite_list_5.append(temp)
        temp = Trash("images/25.png", 0.1)
        temp.set_position(667, 200)
        self.sprite_list_5.append(temp)

    def on_draw(self):
        print(self.counter)
        arcade.start_render()
        if self.counter == 0:
            self.sprite_list = self.sprite_list_1
            self.sprite_list.draw()
        if self.counter == 1:
            self.sprite_list = self.sprite_list_2
            self.sprite_list.draw()
        if self.counter == 2:
            self.sprite_list = self.sprite_list_3
            self.sprite_list.draw()
        if self.counter == 3:
            self.sprite_list = self.sprite_list_4
            self.sprite_list.draw()
        if self.counter == 4:
            self.sprite_list = self.sprite_list_5
            self.sprite_list.draw()
        if self.counter == 5:
            pass

class Trash(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename=filename, scale=scale)


def main():
    # main method
    window = Level_2()
    window.setup()
    arcade.run()


main()
