import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Room Adventure"


class Room:
    def __init__(self, description="", north=None, east=None, south=None, west=None):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.current_room = 0
        self.rooms = []
        self.setup()

    def setup(self):
        # Room 0
        room = Room("You are in a brightly lit kitchen. There is a door to the north.", north=1)
        self.rooms.append(room)

        # Room 1
        room = Room("You are in a spacious living room with a cozy fireplace. A kitchen lies to the south.",
                    south=0)
        self.rooms.append(room)

    def on_draw(self):
        arcade.start_render()
        room_description = self.rooms[self.current_room].description
        arcade.draw_text(room_description, 50, SCREEN_HEIGHT // 2, arcade.color.BLACK, 12, align="center",
                         anchor_x="center", anchor_y="center", width=700)

    def on_key_press(self, key, modifiers):
        current_room = self.rooms[self.current_room]
        if key == arcade.key.UP:
            if current_room.north is not None:
                self.current_room = current_room.north
        elif key == arcade.key.DOWN:
            if current_room.south is not None:
                self.current_room = current_room.south
        elif key == arcade.key.LEFT:
            if current_room.west is not None:
                self.current_room = current_room.west
        elif key == arcade.key.RIGHT:
            if current_room.east is not None:
                self.current_room = current_room.east


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
