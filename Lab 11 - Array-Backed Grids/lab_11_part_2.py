import arcade

# Constants
WIDTH = 600
HEIGHT = 600
ROWS = 10
COLS = 10
CELL_WIDTH = WIDTH // COLS
CELL_HEIGHT = HEIGHT // ROWS


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, "Array-Backed Grid Example")
        self.grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

    def on_draw(self):
        arcade.start_render()
        for row in range(ROWS):
            for col in range(COLS):
                x = col * CELL_WIDTH + CELL_WIDTH // 2
                y = row * CELL_HEIGHT + CELL_HEIGHT // 2
                color = arcade.color.WHITE if self.grid[row][col] == 0 else arcade.color.BLUE
                arcade.draw_rectangle_filled(x, y, CELL_WIDTH - 1, CELL_HEIGHT - 1, color)

    def on_mouse_press(self, x, y, button, modifiers):
        col = x // CELL_WIDTH
        row = y // CELL_HEIGHT
        if 0 <= col < COLS and 0 <= row < ROWS:
            self.toggle_cells(row, col)

    def toggle_cells(self, row, col):
        # Toggle the clicked cell
        self.grid[row][col] = 1 - self.grid[row][col]
        # Toggle adjacent cells
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    if (dr != 0 or dc != 0):  # Avoid retoggling the original cell
                        self.grid[nr][nc] = 1 - self.grid[nr][nc]

def on_mouse_press(self, x, y, button, modifiers):
    col = x // CELL_WIDTH
    row = y // CELL_HEIGHT
    if 0 <= col < COLS and 0 <= row < ROWS:
        self.toggle_cells(row, col)
        # Counting cells
        total_selected = sum(sum(row) for row in self.grid)
        print(f"Total of {total_selected} cells are selected.")
        for idx, row in enumerate(self.grid):
            count_in_row = sum(row)
            print(f"Row {idx} has {count_in_row} cells selected.")
        # Add column count and continuous count as needed


def main():
    window = MyGame()
    arcade.run()


if __name__ == "__main__":
    main()


