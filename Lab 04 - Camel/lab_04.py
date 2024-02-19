import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class CamelGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Camel Game")

        # Game variables
        self.done = False
        self.miles_traveled = 0
        self.thirst = 0
        self.camel_tiredness = 0
        self.natives_distance = -20
        self.drinks_in_canteen = 3

    def on_draw(self):
        arcade.start_render()

        # Display game information
        arcade.draw_text("A. Drink from your canteen.", 50, 500, arcade.color.WHITE, 16)
        arcade.draw_text("B. Ahead moderate speed.", 50, 470, arcade.color.WHITE, 16)
        arcade.draw_text("C. Ahead full speed.", 50, 440, arcade.color.WHITE, 16)
        arcade.draw_text("D. Stop for the night.", 50, 410, arcade.color.WHITE, 16)
        arcade.draw_text("E. Status check.", 50, 380, arcade.color.WHITE, 16)
        arcade.draw_text("Q. Quit.", 50, 350, arcade.color.WHITE, 16)

        arcade.draw_text(f"Miles traveled: {self.miles_traveled}", 50, 300, arcade.color.WHITE, 16)
        arcade.draw_text(f"Drinks in canteen: {self.drinks_in_canteen}", 50, 270, arcade.color.WHITE, 16)
        arcade.draw_text(f"The natives are {self.natives_distance + self.miles_traveled} miles behind you.", 50, 240, arcade.color.WHITE, 16)

    def update(self, delta_time):
        if not self.done:
            user_choice = input("What is your choice? ")

            if user_choice.upper() == "Q":
                self.done = True
                print("You quit the game.")
            elif user_choice.upper() == "E":
                self.status_check()
            elif user_choice.upper() == "D":
                self.stop_for_night()
            elif user_choice.upper() == "C":
                self.ahead_full_speed()
            elif user_choice.upper() == "B":
                self.ahead_moderate_speed()
            elif user_choice.upper() == "A":
                self.drink_from_canteen()
            else:
                print("Invalid choice. Try again.")

    def status_check(self):
        print(f"\nMiles traveled: {self.miles_traveled}")
        print(f"Drinks in canteen: {self.drinks_in_canteen}")
        print(f"The natives are {self.natives_distance + self.miles_traveled} miles behind you.\n")

    def stop_for_night(self):
        print("You stopped and rested. Your camel is happy.")
        self.camel_tiredness = 0
        self.natives_distance += random.randint(7, 14)

    def ahead_full_speed(self):
        distance = random.randint(10, 20)
        self.miles_traveled += distance
        self.thirst += 1
        self.camel_tiredness += random.randint(1, 3)
        self.natives_distance += random.randint(7, 14)
        print(f"You traveled {distance} miles.")

    def ahead_moderate_speed(self):
        distance = random.randint(5, 12)
        self.miles_traveled += distance
        self.thirst += 1
        self.camel_tiredness += 1
        self.natives_distance += random.randint(7, 14)
        print(f"You traveled {distance} miles.")

    def drink_from_canteen(self):
        if self.drinks_in_canteen > 0:
            self.drinks_in_canteen -= 1
            self.thirst = 0
            print("You drank from your canteen.")
        else:
            print("Error: No drinks left in the canteen.")

if __name__ == "__main__":
    game = CamelGame()
    arcade.run()
