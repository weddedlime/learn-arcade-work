import arcade

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CHARACTER_SCALE = 0.5
MOVEMENT_SPEED = 5

class KeyboardControlledObject:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, 30, arcade.color.BLUE)

    def update(self):
        pass

    def move(self, key):
        if key == arcade.key.UP:
            self.y += MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.y -= MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.x -= MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.x += MOVEMENT_SPEED

        # Keep the object within the screen bounds
        self.x = max(0, min(self.x, SCREEN_WIDTH))
        self.y = max(0, min(self.y, SCREEN_HEIGHT))

class MouseControlledObject:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, 60, 40, arcade.color.RED)

    def update(self):
        pass

    def on_mouse_motion(self, x, y, dx, dy):
        self.x = x
        self.y = y

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "My Arcade Game")
        self.background = None
        self.keyboard_object = None
        self.mouse_object = None
        self.background_music = None

    def setup(self):
        self.background = arcade.load_texture("background.png")
        self.keyboard_object = KeyboardControlledObject()
        self.mouse_object = MouseControlledObject()
        self.background_music = arcade.load_sound("background_music.mp3")
        self.background_music.play(volume=0.5, loop=True)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.keyboard_object.draw()
        self.mouse_object.draw()

    def update(self, delta_time):
        self.keyboard_object.update()

def main():
    game = MyGame()
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
