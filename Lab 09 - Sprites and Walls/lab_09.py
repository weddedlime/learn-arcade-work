import arcade

# Game constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Custom Maze Game"

PLAYER_SCALING = 0.5
TILE_SCALING = 0.5
PLAYER_SPEED = 5

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        # Player setup
        self.player_sprite = None
        self.physics_engine = None

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png", PLAYER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        self.player_list.append(self.player_sprite)

        # Create walls around the perimeter and additional walls to navigate
        for x in range(0, SCREEN_WIDTH, 64):
            # Bottom and top rows
            for y in (64, SCREEN_HEIGHT - 64):
                wall = arcade.Sprite(":resources:images/tiles/grassMid.png", TILE_SCALING)
                wall.center_x = x
                wall.center_y = y
                self.wall_list.append(wall)

        # Left and right columns
        for y in range(128, SCREEN_HEIGHT - 64, 64):
            for x in (64, SCREEN_WIDTH - 64):
                wall = arcade.Sprite(":resources:images/tiles/grassMid.png", TILE_SCALING)
                wall.center_x = x
                wall.center_y = y
                self.wall_list.append(wall)

        # Add more walls as needed to create a maze

        # Initialize the physics engine
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        self.wall_list.draw()
        self.player_list.draw()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if key == arcade.key.UP:
            self.player_sprite.change_y = PLAYER_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -PLAYER_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -PLAYER_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = PLAYER_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        if key in [arcade.key.UP, arcade.key.DOWN]:
            self.player_sprite.change_y = 0
        elif key in [arcade.key.LEFT, arcade.key.RIGHT]:
            self.player_sprite.change_x = 0

    def update(self, delta_time):
        """ Movement and game logic """
        self.physics_engine.update()

        # Keep the player on the screen
        if self.player_sprite.left < 0:
            self.player_sprite.left = 0
        elif self.player_sprite.right > SCREEN_WIDTH:
            self.player_sprite.right = SCREEN_WIDTH
        if self.player_sprite.bottom < 0:
            self.player_sprite.bottom = 0
        elif self.player_sprite.top > SCREEN_HEIGHT:
            self.player_sprite.top = SCREEN_HEIGHT

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
