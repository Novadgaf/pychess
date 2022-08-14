from turtle import update
import pygame
import sys
import numpy as np

from chessboard import Chessboard
from figures import *

class Pychess():
    def __init__(self) -> None:    
        self.WIDTH = 640
        self.HEIGHT = 640
        self.chessboard_array = [[None for x in range(8)] for y in range(8)] 
        self.main()

    def main(self):
        """
        main main function to run the game
        """
        self.setup_pygame()
        self.draw_initial_setup()
        chessboard = Chessboard(self.CHESSBOARD_LAYER)
        self.update_win()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    chessboard.mouse_left_clicked(event)
            self.update_win()

    def setup_pygame(self):
        """
        setup_pygame creates the main window aswell as the layers for the chessboard and figures
        """
        self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.CHESSBOARD_LAYER = pygame.Surface((self.WIDTH,self.HEIGHT), pygame.SRCALPHA)
        self.FIGURE_LAYER = pygame.Surface((self.WIDTH,self.HEIGHT), pygame.SRCALPHA)

    def draw_initial_setup(self):
        """
        draw_initial_setup draws initial game setup
        """
        #pawns
        for col in range(8):
            self.chessboard_array[1][col] = Pawn(self.FIGURE_LAYER, "white", 1, col)
            self.chessboard_array[6][col] = Pawn(self.FIGURE_LAYER, "black", 6, col)

        #rooks
        self.chessboard_array[0][0] = Rook(self.FIGURE_LAYER, "white", 0, 0)
        self.chessboard_array[0][7] = Rook(self.FIGURE_LAYER, "white", 0, 7)
        self.chessboard_array[7][0] = Rook(self.FIGURE_LAYER, "black", 7, 0)
        self.chessboard_array[7][7] = Rook(self.FIGURE_LAYER, "black", 7, 7)

        #knights
        self.chessboard_array[0][1] = Knight(self.FIGURE_LAYER, "white", 0, 1)
        self.chessboard_array[0][6] = Knight(self.FIGURE_LAYER, "white", 0, 6)
        self.chessboard_array[7][1] = Knight(self.FIGURE_LAYER, "black", 7, 1)
        self.chessboard_array[7][6] = Knight(self.FIGURE_LAYER, "black", 7, 6)

        #bishops
        self.chessboard_array[0][2] = Bishop(self.FIGURE_LAYER, "white", 0, 2)
        self.chessboard_array[0][5] = Bishop(self.FIGURE_LAYER, "white", 0, 5)
        self.chessboard_array[7][2] = Bishop(self.FIGURE_LAYER, "black", 7, 2)
        self.chessboard_array[7][5] = Bishop(self.FIGURE_LAYER, "black", 7, 5)

        #Queens
        self.chessboard_array[0][3] = Queen(self.FIGURE_LAYER, "white", 0, 3)
        self.chessboard_array[7][3] = Queen(self.FIGURE_LAYER, "black", 7, 3)

        #Kings
        self.chessboard_array[0][4] = King(self.FIGURE_LAYER, "white", 0, 4)
        self.chessboard_array[7][4] = King(self.FIGURE_LAYER, "black", 7, 4)

    def update_win(self):
        """
        update_win updates the content
        """
        self.WIN.fill("#000000")
        self.WIN.blit(self.CHESSBOARD_LAYER,(0,0))
        self.WIN.blit(self.FIGURE_LAYER,(0,0))
        pygame.display.update()