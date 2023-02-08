import time
import pygame
from pygame.locals import *
from graphicsutils import *
from colors import *


class Checker():

    def __init__(self, player):
        self.is_queen = False
        self.is_animating = False
        self.animation_start_time = 0
        self.previous_cell_x = None
        self.previous_cell_y = None
        self.player = player
        self.color = BLACK if self.player == 1 else RED

    def draw(self, screen, screen_width, screen_height, cell_x, cell_y, cell_side_length):
        radius = (cell_side_length / 2) - 7

        if not self.is_animating:
            drawn_checker = pygame.draw.circle(screen, self.color,
                                               [cell_x + (cell_side_length / 2), cell_y + (cell_side_length / 2)], radius, 0)
        else:
            destination_x_pos = cell_x + (cell_side_length / 2)
            destination_y_pos = cell_y + (cell_side_length / 2)
            starting_pixel_position = convert_cell_position_to_pixel_position(
                self.previous_cell_x, self.previous_cell_y, screen_width, screen_height)
            starting_pixel_position_x = starting_pixel_position[0] + (
                cell_side_length / 2)
            starting_pixel_position_y = starting_pixel_position[1] + (
                cell_side_length / 2)
            animation_duration_so_far = int(
                time.time() * 1000) - self.animation_start_time
            percentage_completed = animation_duration_so_far / CHECKER_ANIMATION_DURATION

            x_difference = (destination_x_pos -
                            starting_pixel_position_x) * percentage_completed
            current_x = starting_pixel_position_x + x_difference

            y_difference = (destination_y_pos -
                            starting_pixel_position_y) * percentage_completed
            current_y = starting_pixel_position_y + y_difference

            drawn_checker = pygame.draw.circle(screen, self.color,
                                               [current_x, current_y], radius, 0)

            if percentage_completed > 1.00:
                self.is_animating = False

        if self.is_queen:
            font = pygame.font.Font('freesansbold.ttf', 30)
            text = font.render('Q', True, BLACK, self.color)
            screen.blit(text, drawn_checker)

    def __str__(self):
        return "Checker belonging to player " + str(self.player)
