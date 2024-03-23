import arcade

class Room:
    def __init__(self, name="", description="", north=None, east=None, south=None, west=None):
        self.name = name
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west

class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.room_list = []

        # Creating rooms
        room = Room("Starting Room", "You are in the starting room. There is a passage to the north.", 1, 2, 3, 4)
        self.room_list.append(room)

        room = Room("Second Room", "You are in another room. There is a passage to the south.", None, None, 0, None)
        self.room_list.append(room)

        room = Room("East Room", "You are in a room with a door to the east.", None, None, None, 0)
        self.room_list.append(room)

        room = Room("West Room", "You are in a room. There is a passage to the west.", 0, None, None, None)
        self.room_list.append(room)

        self.current_room = 0

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(self.room_list[self.current_room].name, 20, 500, arcade.color.WHITE, 20)
        arcade.draw_text(self.room_list[self.current_room].description, 20, 450, arcade.color.WHITE, 12)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            arcade.close_window()
        elif key == arcade.key.UP:
            self.move("north")
        elif key == arcade.key.DOWN:
            self.move("south")
        elif key == arcade.key.LEFT:
            self.move("west")
        elif key == arcade.key.RIGHT:
            self.move("east")

    def move(self, direction):
        next_room = getattr(self.room_list[self.current_room], direction)
        if next_room is not None:
            self.current_room = next_room

def main():
    window = GameWindow(800, 600, "Arcade Room Game")
    arcade.run()

if __name__ == "__main__":
    main()
