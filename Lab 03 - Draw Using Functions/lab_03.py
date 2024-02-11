import arcade

def draw_circle(x, y):

    arcade.draw_circle_filled(x, y, 30, arcade.color.BLUE)

def draw_triangle(x, y):

    arcade.draw_triangle_filled(x, y + 30, x - 30, y - 30, x + 30, y - 30, arcade.color.RED)

def draw_square(x, y):

    arcade.draw_rectangle_filled(x, y, 40, 40, arcade.color.GREEN)


arcade.open_window(600, 600, "Drawing Functions Example")
arcade.set_background_color(arcade.color.WHITE)


draw_circle(100, 100)


draw_triangle(300, 300)


draw_square(500, 500)


draw_circle(400, 200)


draw_square(200, 400)


draw_triangle(100, 500)


arcade.draw_point(100, 100, arcade.color.BLACK, 5)


arcade.finish_render()


arcade.run()
