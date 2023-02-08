from board import Board
import math
import time
import pygame
from colors import *
from config import *
from game import Game

# Initialize pygame
pygame.init()

CELL_FONT = pygame.font.SysFont('Arial', 24)

# Set the HEIGHT and WIDTH of the screen
video_infos = pygame.display.Info()
width, height = video_infos.current_w, video_infos.current_h
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

# Set title of screen
pygame.display.set_caption("Checkers")

done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

board = Board()
board.populate_board()

game = Game(board)

# -------- Main Program Loop -----------
while not done:

    screen_width, screen_height = pygame.display.get_surface().get_size()
    cell_side_length = (screen_height // board.length) - DISTANCE_BETWEEN_CELLS
    width_of_grid = cell_side_length * board.length + \
        ((board.length - 1) * DISTANCE_BETWEEN_CELLS)
    margin = math.floor((screen_width - width_of_grid) / 2)

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True 
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

    # Set the screen background
    screen.fill(DARKGREEN)

    game.draw(screen, screen_width, screen_height, CELL_FONT)

    # Limit to 24 frames per second
    clock.tick(24)

    # Update the screen with latest changes
    pygame.display.flip()


pygame.quit()
