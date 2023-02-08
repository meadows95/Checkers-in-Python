from cell import Cell
from checker import Checker
from config import BOARD_LENGTH

class Board():
    # properties:
    # cells: list
    # length: number

    def __init__(self):
        self.length = BOARD_LENGTH
        if self.length % 2 is not 0:
            raise Exception("Board length must be even")
        self.cells = []
        for y in range(self.length):
            for x in range(self.length):
                cell = Cell(x, y)
                self.cells.append(cell)

    # Populates the grid to start a new game
    def populate_board(self):
        for cell in self.cells:
            player_to_get_checker = None

            if (cell.y == 0 or cell.y == 1 or cell.y == 2) and cell.is_playable():
                player_to_get_checker = 1
            elif (cell.y == 5 or cell.y == 6 or cell.y == 7) and cell.is_playable():
                player_to_get_checker = 2

            if player_to_get_checker:
                checker_piece = Checker(player_to_get_checker)
                cell.occupant = checker_piece

    def find_cell_by_x_and_y_grid_coordinates(self, cell_x, cell_y):
        for cell in self.cells:
            if cell.x == cell_x and cell.y == cell_y:
                return cell
        return None

    def draw(self, screen, screen_width, screen_height, font, selected_cell):
        # Draw all the cells first so that the checkers can be drawn on top of them
        for cell in self.cells:
            is_selected_cell = (cell == selected_cell)
            cell.draw(screen, screen_width, screen_height, self.length, is_selected_cell)

        for cell in self.cells:
            cell.draw_occupant(screen, screen_width, screen_height, self.length)
