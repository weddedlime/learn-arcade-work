import arcade

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Final Lab Game"

# Scaling constants
CHARACTER_SCALING = 1.0
ENEMY_SCALING = 0.8
POWERUP_SCALING = 0.5

# Paths to the custom assets
PLAYER_SPRITE_PATH = "path/to/custom_player_image.png"
ENEMY_SPRITE_PATH = "path/to/custom_enemy_image.png"
OBSTACLE_SPRITE_PATH = "path/to/custom_obstacle_image.png"
POWERUP_SPRITE_PATH = "path/to/custom_powerup_image.png"
HIT_SOUND_PATH = "path/to/custom_hit_sound.wav"
POINT_SOUND_PATH = "path/to/custom_point_sound.wav"

# Power-up types
POWERUP_INVINCIBILITY = "invincibility"
POWERUP_MULTIPLIER = "multiplier"

class Player(arcade.Sprite):
    """ Player class """
    def __init__(self, image_path, scaling):
        super().__init__(image_path, scaling)
        self.score = 0
        self.score_multiplier = 1
        self.invincible = False

class PowerUp(arcade.Sprite):
    """ Power-Up class """
    def __init__(self, image_path, scaling, effect):
        super().__init__(image_path, scaling)
        self.effect = effect

    def apply_effect(self, player):
        if self.effect == POWERUP_INVINCIBILITY:
            player.invincible = True
            arcade.schedule(self.end_invincibility, 5, player)  # Invincible for 5 seconds
        elif self.effect == POWERUP_MULTIPLIER:
            player.score_multiplier = 2
            arcade.schedule(self.end_multiplier, 5, player)  # Double points for 5 seconds

    @staticmethod
    def end_invincibility(delta_time, player):
        player.invincible = False

    @staticmethod
    def end_multiplier(delta_time, player):
        player.score_multiplier = 1

class AdvancedEnemy(arcade.Sprite):
    """ Advanced enemy class with random movement """
    def __init__(self, image_path, scaling):
        super().__init__(image_path, scaling)
        self.change_x = arcade.random.randrange(-3, 4)
        self.change_y = arcade.random.randrange(-3, 4)

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.left < 0 or self.right > SCREEN_WIDTH:
            self.change_x *= -1
        if self.bottom < 0 or self.top > SCREEN_HEIGHT:
            self.change_y *= -1

class FinalGame(arcade.Window):
    """ Main game window """
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.player = None
        self.player_list = None
        self.enemy_list = None
        self.powerup_list = None

        self.hit_sound = None
        self.point_sound = None

    def setup(self):
        # Load the player sprite and initialize lists
        self.player = Player(PLAYER_SPRITE_PATH, CHARACTER_SCALING)
        self.player.center_x = SCREEN_WIDTH // 2
        self.player.center_y = SCREEN_HEIGHT // 2
        self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.powerup_list = arcade.SpriteList()
        self.player_list.append(self.player)

        # Load sounds
        self.hit_sound = arcade.load_sound(HIT_SOUND_PATH)
        self.point_sound = arcade.load_sound(POINT_SOUND_PATH)

        # Create enemies and power-ups
        self.create_enemies()
        self.create_powerups()

    def create_enemies(self):
        """ Create enemies for the level """
        for _ in range(5):
            enemy = AdvancedEnemy(ENEMY_SPRITE_PATH, ENEMY_SCALING)
            enemy.center_x = arcade.random.randrange(SCREEN_WIDTH)
            enemy.center_y = arcade.random.randrange(SCREEN_HEIGHT)
            self.enemy_list.append(enemy)

    def create_powerups(self):
        """ Create power-ups for the level """
        powerup_inv = PowerUp(POWERUP_SPRITE_PATH, POWERUP_SCALING, POWERUP_INVINCIBILITY)
        powerup_inv.center_x = arcade.random.randrange(SCREEN_WIDTH)
        powerup_inv.center_y = arcade.random.randrange(SCREEN_HEIGHT)
        self.powerup_list.append(powerup_inv)

        powerup_mult = PowerUp(POWERUP_SPRITE_PATH, POWERUP_SCALING, POWERUP_MULTIPLIER)
        powerup_mult.center_x = arcade.random.randrange(SCREEN_WIDTH)
        powerup_mult.center_y = arcade.random.randrange(SCREEN_HEIGHT)
        self.powerup_list.append(powerup_mult)

    def on_draw(self):
        """ Render the screen """
        arcade.start_render()
        self.player_list.draw()
        self.enemy_list.draw()
        self.powerup_list.draw()

        # Draw the player's score
        arcade.draw_text(f"Score: {self.player.score}", 10, 20, arcade.color.WHITE, 14)

    def on_key_press(self, key, modifiers):
        """ Handle keyboard input for player movement """
        if key == arcade.key.UP:
            self.player.change_y = 5
        elif key == arcade.key.DOWN:
            self.player.change_y = -5
        elif key == arcade.key.LEFT:
            self.player.change_x = -5
        elif key == arcade.key.RIGHT:
            self.player.change_x = 5

    def on_key_release(self, key, modifiers):
        """ Stop player movement on key release """
        if key in (arcade.key.UP, arcade.key.DOWN):
            self.player.change_y = 0
        elif key in (arcade.key.LEFT, arcade.key.RIGHT):
            self.player.change_x = 0

    def update(self, delta_time):
        """ Update the game state """
        self.player_list.update()
        self.enemy_list.update()

        # Check for collisions between the player and enemies
        if not self.player.invincible:
            hit_list = arcade.check_for_collision_with_list(self.player, self.enemy_list)
            if hit_list:
                arcade.play_sound(self.hit_sound)

        # Check for collisions with power-ups
        powerup_hit_list = arcade.check_for_collision_with_list(self.player, self.powerup_list)
        for powerup in powerup_hit_list:
            powerup.apply_effect(self.player)
            arcade.play_sound(self.point_sound)
            powerup.remove_from_sprite_lists()

# Main function to run the game
def main():
    """ Main function to create and run the game """
    window = FinalGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
