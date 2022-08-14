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

    def draw_rect(self, color, x_cord: int, y_cord: int):
        """
        draw_rect draws a rectangle on the board with specific color

        :param color: color of the rectangle
        :type color: rgb tuple or hex str
        :param x_cord: x cord of rectangle (0-7)
        :type x_cord: int
        :param y_cord: y cord of rectangle (0-7)
        :type y_cord: int
        """
        pygame.draw.rect(self.SURFACE, color, [self.SQUARE_SIZE*x_cord, self.SQUARE_SIZE*y_cord, self.SQUARE_SIZE, self.SQUARE_SIZE])

    def mouse_left_clicked(self, event: pygame.event):
        """
        mouse_left_clicked colors the clicked rectangle in a yellow color to visualize the click

        :param event: event that happened
        :type event: pygame.event
        """
        self.create_board()
        x,y = event.pos
        x_cord, y_cord = int(x/self.SQUARE_SIZE), int(int(y/self.SQUARE_SIZE))
        self.draw_rect("#C19C4D", x_cord, y_cord)
        pygame.display.update()


        
