import arcade


def draw_scene():

    draw_tree(100, 200)


    draw_house(300, 200)


def draw_tree(x, y):

    arcade.draw_rectangle_filled(x, y, 20, 40, arcade.color.BROWN)  # Tree trunk
    arcade.draw_triangle_filled(x - 30, y + 30, x, y + 100, x + 30, y + 30, arcade.color.GREEN)  # Tree leaves


def draw_house(x, y):

    arcade.draw_rectangle_filled(x, y, 60, 60, arcade.color.BROWN)  # House base
    arcade.draw_triangle_filled(x - 30, y + 30, x + 30, y + 30, x, y + 90, arcade.color.RED)  # Roof
    arcade.draw_rectangle_filled(x - 15, y - 15, 10, 20, arcade.color.BLUE)  # Door


def main():
    arcade.open_window(600, 400, "Lab 02 Drawing")
    arcade.set_background_color(arcade.color.WHITE)

    arcade.start_render()
    draw_scene()
    arcade.finish_render()

    arcade.run()


if __name__ == "__main__":
    main()