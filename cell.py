from config import *
import math
import pygame
from colors import *

class Cell():
    # properties: data type
    # x: int
    # y: int
    # occupant: Checker or None. None means unoccupied
    # color: tuple

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.occupant = None
        self.color = GAMEBOARD_COLOR if self.is_playable() else NOT_GAMEBOARD_COLOR

    def is_playable(self):
        is_x_and_y_even = (self.x + 1) % 2 == 0 and (self.y + 1) % 2 == 0
        is_x_and_y_odd = (self.x + 1) % 2 != 0 and (self.y + 1) % 2 != 0

        if is_x_and_y_even or is_x_and_y_odd:
            return False
        else:
            return True

    def draw(self, screen, screen_width, screen_height, board_length, is_selected_cell):
        cell_side_length = (screen_height // board_length) - \
            DISTANCE_BETWEEN_CELLS
        width_of_grid = cell_side_length * board_length + \
            ((board_length - 1) * DISTANCE_BETWEEN_CELLS)
        margin = math.floor((screen_width - width_of_grid) / 2)

        x_pixel_pos = (DISTANCE_BETWEEN_CELLS + cell_side_length) * \
            self.x + DISTANCE_BETWEEN_CELLS + margin
        y_pixel_pos = (DISTANCE_BETWEEN_CELLS + cell_side_length) * \
            self.y + DISTANCE_BETWEEN_CELLS

        self.draw_rectangle(
            screen,
            self.color if not is_selected_cell else SELECTED_CELL_COLOR,
            x_pixel_pos,
            y_pixel_pos,
            cell_side_length)

    def draw_occupant(self, screen, screen_width, screen_height, board_length):
        cell_side_length = (screen_height // board_length) - \
            DISTANCE_BETWEEN_CELLS
        width_of_grid = cell_side_length * board_length + \
            ((board_length - 1) * DISTANCE_BETWEEN_CELLS)
        margin = math.floor((screen_width - width_of_grid) / 2)

        x_pixel_pos = (DISTANCE_BETWEEN_CELLS + cell_side_length) * \
            self.x + DISTANCE_BETWEEN_CELLS + margin
        y_pixel_pos = (DISTANCE_BETWEEN_CELLS + cell_side_length) * \
            self.y + DISTANCE_BETWEEN_CELLS

        if self.occupant != None:
            self.occupant.draw(screen, screen_width, screen_height, x_pixel_pos,
                               y_pixel_pos, cell_side_length)

    def draw_rectangle(self, screen, color, x_position, y_position, cell_side_length):
        pygame.draw.rect(
            screen,
            color,
            [
                x_position,
                y_position,
                cell_side_length,
                cell_side_length
            ])

    def __eq__(self, other):
        if not other:
            return False

        return self.x == other.x and self.y == other.y
