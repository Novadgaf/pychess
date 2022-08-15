from tkinter.messagebox import NO
import pygame
import sys

from chessboard import Chessboard
from figures import *

class Pychess():
    def __init__(self) -> None:    
        self.WIDTH = 640
        self.HEIGHT = 640
        self.SQUARE_SIZE = 80
        self.chessboard_array: Figure = [[None for x in range(8)] for y in range(8)] 
        self.selected_y_x=None
        #In Order to keep track of the current player
        self.current_move = 0
        self.main()

    def main(self):
        """
        main main function to run the game
        """
        self.setup_pygame()
        self.chessboard = Chessboard(self.CHESSBOARD_LAYER)
        self.draw_initial_setup()
        self.update_win()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.left_click(event)
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
            self.chessboard_array[1][col] = Pawn(self.FIGURE_LAYER, "black", 1, col)
            self.chessboard_array[6][col] = Pawn(self.FIGURE_LAYER, "white", 6, col)

        #rooks
        self.chessboard_array[0][0] = Rook(self.FIGURE_LAYER, "black", 0, 0)
        self.chessboard_array[0][7] = Rook(self.FIGURE_LAYER, "black", 0, 7)
        self.chessboard_array[7][0] = Rook(self.FIGURE_LAYER, "white", 7, 0)
        self.chessboard_array[7][7] = Rook(self.FIGURE_LAYER, "white", 7, 7)

        #knights
        self.chessboard_array[0][1] = Knight(self.FIGURE_LAYER, "black", 0, 1)
        self.chessboard_array[0][6] = Knight(self.FIGURE_LAYER, "black", 0, 6)
        self.chessboard_array[7][1] = Knight(self.FIGURE_LAYER, "white", 7, 1)
        self.chessboard_array[7][6] = Knight(self.FIGURE_LAYER, "white", 7, 6)

        #bishops
        self.chessboard_array[0][2] = Bishop(self.FIGURE_LAYER, "black", 0, 2)
        self.chessboard_array[0][5] = Bishop(self.FIGURE_LAYER, "black", 0, 5)
        self.chessboard_array[7][2] = Bishop(self.FIGURE_LAYER, "white", 7, 2)
        self.chessboard_array[7][5] = Bishop(self.FIGURE_LAYER, "white", 7, 5)

        #Queens
        self.chessboard_array[0][3] = Queen(self.FIGURE_LAYER, "black", 0, 3)
        self.chessboard_array[7][3] = Queen(self.FIGURE_LAYER, "white", 7, 3)

        #Kings
        self.chessboard_array[0][4] = King(self.FIGURE_LAYER, "black", 0, 4)
        self.chessboard_array[7][4] = King(self.FIGURE_LAYER, "white", 7, 4)

    def update_win(self):
        """
        update_win updates the content
        """
        self.WIN.fill("#000000")
        self.WIN.blit(self.CHESSBOARD_LAYER,(0,0))
        self.WIN.blit(self.FIGURE_LAYER,(0,0))
        pygame.display.update()

    def left_click(self, event: pygame.event):
        x,y = event.pos
        cord_y, cord_x = int(y/self.SQUARE_SIZE), int(int(x/self.SQUARE_SIZE))
        self.chessboard.mouse_left_clicked(cord_y, cord_x)

        if self.chessboard_array[cord_y][cord_x] != None and self.selected_y_x==None:
            self.selected_y_x = (cord_y, cord_x)
        #clicked square after clicking figure
        elif self.selected_y_x != None:
            #figure at pos {piece_cord_y}, {piece_cord_x}
            piece_cord_y, piece_cord_x = self.selected_y_x
            #trying to move {step_y_x}
            step_y_x = (cord_y-piece_cord_y, cord_x-piece_cord_x)

            #clicked on itself
            if step_y_x == (0,0):
                return
            
            piece: Figure = self.chessboard_array[piece_cord_y][piece_cord_x]

            #collides with something on the way
            collision = self.check_for_collision(piece, step_y_x[0], step_y_x[1])
            #collision
            if  collision == 2:
                return
            #works but no capture
            elif collision == 1:
                capture_move = False
                pass
            #capture move
            elif collision == 0:
                capture_move = True

            found_valid_move = False
            if piece.__class__.__name__ == "Pawn":
                moves = piece.moves(capture_move)
            else:
                moves = piece.moves()
            for move in moves:
                tmp_move = (0,0)
                for x in range(7):
                    tmp_move = tuple(map(lambda i, j: i + j, move, tmp_move))
                    if piece.COLOR == "white" and tmp_move == step_y_x:
                        if self.current_move % 2 == 0:
                            found_valid_move = True
                    elif piece.COLOR == "black" and tmp_move == step_y_x:
                        if self.current_move % 2 == 1:
                            found_valid_move = True
                    if not piece.can_move_multiple_squares:
                        break

            if found_valid_move:
                self.current_move += 1
                self.move_figure(piece, step_y_x[0], step_y_x[1])
            self.selected_y_x = None
        #nothing selected before
        else:
            pass

    def move_figure(self, piece: Figure, step_y: int, step_x: int):
        old_y, old_x = piece.get_cords()
        piece.move_figure(step_y, step_x)
        new_y, new_x = piece.get_cords()
        self.chessboard_array[new_y][new_x] = piece
        self.chessboard_array[old_y][old_x] = None
        self.chessboard_array = self.chessboard_array[::-1]

        for row in self.chessboard_array:
            for piece in row:
                if piece != None:
                    piece.cord_y = 7 - piece.cord_y
                    piece.draw_figure()  
        for row in self.chessboard_array:
            for piece in row:
                if piece != None:
                    piece.draw_figure()            

    def check_for_collision(self, piece: Figure, step_y: int, step_x: int):
        pos_y, pos_x = piece.get_cords()
        end_pos_fig = self.chessboard_array[pos_y+step_y][pos_x+step_x]
        if end_pos_fig != None:
            if end_pos_fig.COLOR != piece.COLOR:
                return 0
            else:
                return 2
        else:
            print("wont capture anything")
            
        
        if not piece.can_jump:
            if abs(step_x) == abs(step_y):
                for i in range(1,abs(step_x+1)):
                    if step_x < 0:
                        tmp_x = pos_x - i
                    elif step_x > 0:
                        tmp_x = pos_x + i
                    if step_y < 0:
                        tmp_y = pos_y - i
                    elif step_y > 0:
                        tmp_y = pos_y + i
                    if self.chessboard_array[tmp_y][tmp_x] != None:
                        return 2
                return 1
            elif step_x == 0:
                for i in range(1,abs(step_y+1)):
                    if step_y < 0:
                        print(pos_y)
                        tmp_y = pos_y - i
                        print(tmp_y)
                    elif step_y > 0:
                        tmp_y = pos_y + i
                    if self.chessboard_array[tmp_y][tmp_y] != None:
                        return 2
                return 1
            elif step_y == 0:
                for i in range(1,abs(step_x+1)):
                    if step_x < 0:
                        tmp_x = pos_x - i
                    elif step_x > 0:
                        tmp_x = pos_x + i
                    if self.chessboard_array[pos_y+step_y][pos_x+step_x] != None:
                        return 2
                return 1