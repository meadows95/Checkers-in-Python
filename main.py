from board import Board
from cell import Cell
from inspect import currentframe
import math
import time
from re import X
from tracemalloc import reset_peak
import pygame
from config import *

from game import Game

# Define possible colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARKGREEN = (34, 69, 36)

current_time = None
start_time = None

# Initialize pygame
pygame.init()


BIG_FONT = pygame.font.Font(None, 80)
SMALL_FONT = pygame.font.Font(None, 45)
CELL_FONT = pygame.font.SysFont('Arial', 24)
END_OF_GAME_FONT = pygame.font.SysFont('Arial', 80, bold=True)

# Set the HEIGHT and WIDTH of the screen
video_infos = pygame.display.Info()
width, height = video_infos.current_w, video_infos.current_h
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

# Set title of screen
pygame.display.set_caption("Checkers")

done = False
mine_clicked = False
has_started_stopwatch = False
win_lose_time = None

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

board = Board()
board.populate_board()

game = Game(board)

# -------- Main Program Loop -----------
while not done:
    current_time = time.time()

    screen_width, screen_height = pygame.display.get_surface().get_size()
    cell_side_length = (screen_height // board.length) - DISTANCE_BETWEEN_CELLS
    width_of_grid = cell_side_length * board.length + \
        ((board.length - 1) * DISTANCE_BETWEEN_CELLS)
    margin = math.floor((screen_width - width_of_grid) / 2)

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            x_pixels = pos[0]
            y_pixels = pos[1]
            # Change the x/y screen coordinates to grid coordinates
            cell_x = (x_pixels - margin) // (cell_side_length +
                                             DISTANCE_BETWEEN_CELLS)
            cell_y = y_pixels // (cell_side_length + DISTANCE_BETWEEN_CELLS)
            clicked_cell = board.find_cell_by_x_and_y_grid_coordinates(
                cell_x, cell_y)

            if clicked_cell:
                game.cell_clicked(clicked_cell)

        elif event.type == pygame.KEYDOWN:
            pass
            # if event.key == pygame.K_r:
            #     if mine_clicked or game1.did_player_win():
            #         reset_game()

    # Set the screen background
    screen.fill(DARKGREEN)

    game.draw(screen, screen_width, screen_height, CELL_FONT)

    # if mine_clicked:
    #     display_end_game_text(screen, screen_width, screen_height, False)
    #     if not win_lose_time:
    #         win_lose_time = time.time()

    # if game1.did_player_win():
    #     display_end_game_text(screen, screen_width, screen_height, True)
    #     if not win_lose_time:
    #         win_lose_time = time.time()

    # if has_started_stopwatch:
    #     display_stopwatch()

    # Limit to 24 frames per second
    clock.tick(24)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()


pygame.quit()
