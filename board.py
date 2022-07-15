import random
import math

import pygame
from cell import Cell
from checker import Checker


class Board():
    # properties:

    # cells: list

    def __init__(self, length):
        if length % 2 is not 0:
            raise Exception("Board length must be even")
        self.cells = []
        self.length = length
        # list of cells used to make the grid
        for y in range(self.length):
            for x in range(self.length):
                # create new instance of the cell class with every x and y value in the range
                cell = Cell(x, y, False)
                # add new cell to list of cells
                self.cells.append(cell)

    # populates the grid to start a new game
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

    def print_board(self):
        for cell in self.cells:
            if cell.x == (self.length - 1):
                print(cell.occupant)
            else:
                # when adding (end = "") as a parameter, it will print on the same line
                print(cell.occupant + " ", end="")

    # Moves 1 checker from one cell to another
    def move_checker(self, from_cell, to_cell):
        to_cell.occupant = from_cell.occupant
        from_cell.occupant = None

    # def count_mines(self):
    #     number_of_mines = 0
    #     for cell in self.cells:
    #         if cell.occupant == "M":
    #             number_of_mines += 1
    #     return number_of_mines

    def find_cell_by_x_and_y_grid_coordinates(self, cell_x, cell_y):
        for cell in self.cells:
            if cell.x == cell_x and cell.y == cell_y:
                return cell

    def did_player_win(self):
        for cell in self.cells:
            if cell.occupant == "0" and cell.hidden == True:
                return False
        return True
