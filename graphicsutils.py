import math
from config import *

def convert_cell_position_to_pixel_position(cell_x, cell_y, screen_width, screen_height):
    cell_side_length = (screen_height // BOARD_LENGTH) - \
        DISTANCE_BETWEEN_CELLS
    width_of_grid = cell_side_length * BOARD_LENGTH + \
        ((BOARD_LENGTH - 1) * DISTANCE_BETWEEN_CELLS)
    margin = math.floor((screen_width - width_of_grid) / 2)

    x_pixel_pos = (DISTANCE_BETWEEN_CELLS + cell_side_length) * \
        cell_x + DISTANCE_BETWEEN_CELLS + margin
    y_pixel_pos = (DISTANCE_BETWEEN_CELLS + cell_side_length) * \
        cell_y + DISTANCE_BETWEEN_CELLS

    return (x_pixel_pos, y_pixel_pos)
