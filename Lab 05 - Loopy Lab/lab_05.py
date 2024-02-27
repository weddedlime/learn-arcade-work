import arcade


def draw_section_outlines():
    # Draw squares on bottom
    for i in range(4):
        x = 300 * i + 150
        y = 150
        arcade.draw_rectangle_outline(x, y, 300, 300, arcade.color.BLACK)

    # Draw squares on top
    for i in range(4):
        x = 300 * i + 150
        y = 450
        arcade.draw_rectangle_outline(x, y, 300, 300, arcade.color.BLACK)


def draw_section_1():
    for row in range(30):
        for column in range(30):
            x = column * 10
            y = row * 10
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_2():
    for row in range(30):
        for column in range(30):
            x = column * 10 + 300
            y = row * 10
            if (column + row) % 2 == 0:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)
            else:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_3():
    for row in range(30):
        for column in range(30):
            x = column * 10 + 600
            y = row * 10
            if (column % 2 == 0) and (row % 2 == 0):
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)
            else:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_4():
    for row in range(30):
        for column in range(30):
            x = column * 10 + 900
            y = row * 10
            if (column % 2 == 0) and (row % 2 == 0):
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)
            elif (column % 2 != 0) and (row % 2 != 0):
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)
            else:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_5():
    for row in range(30):
        for column in range(30):
            x = column * 10
            y = row * 10 + 300
            color = (column * 255 // 30, row * 255 // 30, 128)
            arcade.draw_rectangle_filled(x, y, 5, 5, color)


def draw_section_6():
    for row in range(30):
        for column in range(30):
            x = column * 10 + 300
            y = row * 10 + 300
            color = (column * 255 // 30, row * 255 // 30, 128)
            arcade.draw_rectangle_filled(x, y, 5, 5, color)


def draw_section_7():
    for row in range(30):
        for column in range(30):
            x = column * 10 + 600
            y = row * 10 + 300
            color = (column * 255 // 30, row * 255 // 30, 128)
            arcade.draw_rectangle_filled(x, y, 5, 5, color)


def draw_section_8():
    for row in range(30):
        for column in range(30):
            x = column * 10 + 900
            y = row * 10 + 300
            color = (column * 255 // 30, row * 255 // 30, 128)
            arcade.draw_rectangle_filled(x, y, 5, 5, color)


def main():
    # Create a window
    arcade.open_window(1200, 600, "Lab 05 - Loopy Lab")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    arcade.start_render()

    # Draw the outlines for the sections
    draw_section_outlines()

    # Draw the sections
    draw_section_1()
    draw_section_2()
    draw_section_3()
    draw_section_4()
    draw_section_5()
    draw_section_6()
    draw_section_7()
    draw_section_8()

    arcade.finish_render()

    # Print count-up and count-down
    print("Count up!")
    for i in range(10):
        print(i)

    print("Count down, even if i is going up")
    for i in range(10):
        x = 9 - i
        print("i is", i, "and 9-i is", x)
