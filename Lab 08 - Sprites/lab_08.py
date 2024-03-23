import arcade

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SPEED = 5
GOOD_SPRITE_SPEED = 3
BAD_SPRITE_SPEED = 2


class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "My Arcade Game")
        self.set_mouse_visible(False)
        self.player_sprite = arcade.Sprite("player_sprite.png", 0.5)
        self.player_sprite.center_x = SCREEN_WIDTH // 2
        self.player_sprite.center_y = SCREEN_HEIGHT // 2
        self.good_sprite_list = arcade.SpriteList()
        self.bad_sprite_list = arcade.SpriteList()
        self.score = 0
        self.game_over = False

    def setup(self):
        # Create good sprites
        for _ in range(5):
            good_sprite = arcade.Sprite("good_sprite.png", 0.5)
            good_sprite.center_x = random.randint(0, SCREEN_WIDTH)
            good_sprite.center_y = random.randint(0, SCREEN_HEIGHT)
            self.good_sprite_list.append(good_sprite)

        # Create bad sprites
        for _ in range(3):
            bad_sprite = arcade.Sprite("bad_sprite.png", 0.5)
            bad_sprite.center_x = random.randint(0, SCREEN_WIDTH)
            bad_sprite.center_y = random.randint(0, SCREEN_HEIGHT)
            self.bad_sprite_list.append(bad_sprite)

    def on_draw(self):
        arcade.start_render()
        if not self.game_over:
            self.player_sprite.draw()
            self.good_sprite_list.draw()
            self.bad_sprite_list.draw()
            arcade.draw_text(f"Score: {self.score}", 10, SCREEN_HEIGHT - 20, arcade.color.WHITE, 14)
        else:
            arcade.draw_text("Game Over", SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2, arcade.color.WHITE, 20)

    def update(self, delta_time):
        if not self.game_over:
            self.player_sprite.update()
            self.good_sprite_list.update()
            self.bad_sprite_list.update()

            # Check for collisions with good sprites
            good_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.good_sprite_list)
            for good_sprite in good_hit_list:
                good_sprite.remove_from_sprite_lists()
                self.score += 1
                arcade.play_sound("good_sound.wav")

            # Check for collisions with bad sprites
            bad_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bad_sprite_list)
            for bad_sprite in bad_hit_list:
                bad_sprite.remove_from_sprite_lists()
                self.score -= 1
                arcade.play_sound("bad_sound.wav")

            # Check if all good sprites are collected
            if len(self.good_sprite_list) == 0:
                self.game_over = True

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player_sprite.change_y = PLAYER_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -PLAYER_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -PLAYER_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = PLAYER_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_mouse_motion(self, x, y, dx, dy):
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
