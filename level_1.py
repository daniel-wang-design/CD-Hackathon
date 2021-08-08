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

        pile1 = arcade.SpriteSolidColor(75, 150, arcade.csscolor.LIGHT_STEEL_BLUE)
        pile1.position = 250, 200
        self.pile_mat_list.append(pile1)

        pile2 = arcade.SpriteSolidColor(75, 150, arcade.csscolor.LIGHT_STEEL_BLUE)
        pile2.position = 400, 200
        self.pile_mat_list.append(pile2)

        pile3 = arcade.SpriteSolidColor(75, 150, arcade.csscolor.LIGHT_STEEL_BLUE)
        pile3.position = 550, 200
        self.pile_mat_list.append(pile3)

        compost = Trash("images/compost_bin.png", 0.5)
        self.pile1.append(compost)
        compost.position = self.pile_mat_list[0].position

        garbage = Trash("images/garbage_bin.png", 0.5)
        self.pile2.append(garbage)
        garbage.position = self.pile_mat_list[1].position

        recycling = Trash("images/recycling_bin.png", 0.5)
        self.pile3.append(recycling)
        recycling.position = self.pile_mat_list[2].position

    def on_draw(self):
        arcade.start_render()
        self.pile_mat_list.draw()
        self.sprite_list.draw()

    def on_mouse_press(self, x, y, button, key_modifiers):
        trash = arcade.get_sprites_at_point((x, y), self.sprite_list)
        if len(trash) > 0:
            self.item.append(trash)
            self.item_original_position = [self.item[0].position]

    def on_mouse_release(self, x: float, y: float, button: int,
                         modifiers: int):
        if len(self.item) == 0:
            return
        pile, distance = arcade.get_closest_sprite(self.item[0], self.pile_mat_list)

        if arcade.check_for_collision((self.item[0], pile)):
            reset_position = False
        else:
            reset_position = True

        if reset_position:
            self.item.position = self.item_original_position[0]

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.item.center_x += dx
        self.item.center_y += dy


class Trash(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename=filename, scale=scale)


def main():
    # main method
    window = Main()
    window.setup()
    arcade.run()

main()
