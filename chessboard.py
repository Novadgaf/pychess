from cmath import rect
from email.mime import image
import pygame
import sys

from zmq import DRAFT_API
from figures import *



class Chessboard:
    def __init__(self, screen: pygame.Surface) -> None:
        self.SURFACE = screen
        self.SQUARE_SIZE = 80
        self.COLOR_BLACK, self.COLOR_WHITE = "#674932", "#BA9E7A"
        self.LINE_COLOR = (255, 0, 0)

        self.create_board()

    def create_board(self):
        """
        create_board draws / resets chessboard
        """
        count = 0
        for row in range(8):
            for col in range(8):
                if count % 2 == 0:
                    color = self.COLOR_BLACK
                else:
                    color = self.COLOR_WHITE
                self.draw_rect(color, col, row)
                count += 1
            count -= 1
        pygame.display.update()

    def draw_rect(self, color, cord_y: int, cord_x: int):
        """
        draw_rect draws a rectangle on the board with specific color

        :param color: color of the rectangle
        :type color: rgb tuple or hex str
        :param cord_y: y cord of rectangle (0-7)
        :type cord_y: int
        :param cord_x: x cord of rectangle (0-7)
        :type cord_x: int
        """
        pygame.draw.rect(self.SURFACE, color, [self.SQUARE_SIZE*cord_x, self.SQUARE_SIZE*cord_y, self.SQUARE_SIZE, self.SQUARE_SIZE])

    def mouse_left_clicked(self, cord_y: int, cord_x: int):
        """
        mouse_left_clicked colors the clicked rectangle in a yellow color to visualize the click

        :param y_cord: y cord of click
        :type y_cord: int
        :param x_cord: x cord of click
        :type x_cord: int
        """
        self.create_board()
        self.draw_rect("#C19C4D", cord_y, cord_x)
        pygame.display.update()


        
