import arcade

width = 1440
height = 845
title = "Game"

class Main(arcade.Window):
    """
    Main game application class
    """
    def __init__(self):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.LIGHT_STEEL_BLUE)

    def setup(self):


    def on_draw(self):
        arcade.start_render()

    def on_mouse_press(self, x, y, button, key_modifiers):
        self.trash = arcade.get_sprites_at_point((x, y), self.sprites)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        for trash in self.trash:
            trash.center_x += dx
            trash.center_y += dy

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

