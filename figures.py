from msilib.schema import Error
from typing import Tuple
import pygame

class Figure():
    """
    Figure super class for every figure
    """
    def __init__(self, surface: pygame.Surface, color: str, cord_y: int = 0, cord_x: int = 0, can_move_multiple_squares: bool = False, can_jump: bool = False) -> None:
        self.SURFACE = surface
        self.SQUARE_SIZE = 80
        self.COLOR = color

        self.cord_y = cord_y
        self.cord_x = cord_x
        self.image_path = None
        self.moved = False

        # e.g bishop, queen, rook
        self.can_move_multiple_squares = can_move_multiple_squares
        # can jump (knight)
        self.can_jump = can_jump
    
    def setup_figure_drawing(self):
        self.img = pygame.image.load(self.image_path)
        self.img = pygame.transform.scale(self.img, (80, 80))
        
    def draw_figure(self) -> None:
        """
        draw_figure draws a figure on the board

        :param image_path: path to the figure image
        :type image_path: str
        """
        x_cord = self.cord_x*self.SQUARE_SIZE
        y_cord = self.cord_y*self.SQUARE_SIZE
        
        rec = pygame.Rect(x_cord,y_cord,80,80)
        self.SURFACE.blit(self.img, rec)
        pygame.display.update()
    
    def move_figure(self, cord_y: int, cord_x: int):
        """
        move_figure move a figure

        :param cord_y: amount of y cords to move
        :type cord_y: int
        :param cord_x: amount of x cords to move
        :type cord_x: int
        """
        self.cord_y += cord_y
        self.cord_x += cord_x

        self.SURFACE.fill(pygame.Color(0,0,0,0))
        self.moved = True

    def get_cords(self) -> Tuple:
        """
        get_cords returns position (y,x)

        :return: y,x position of figure
        :rtype: Tuple
        """
        return (self.cord_y, self.cord_x)
        

class Pawn(Figure):
    """
    Pawn class for a pawn figure

    :param Figure: superclass for this figure
    :type Figure: Figure
    """
    def __init__(self, surface: pygame.Surface, color: str, cord_y: int = 0, cord_x: int = 0) -> None:
        super().__init__(surface, color, cord_y, cord_x)
        self.image_path = fr"images/{color}_pawn.png"
        self.setup_figure_drawing()
        self.draw_figure()

    def moves(self, capture_move: bool) -> list[tuple]:
        """
        move possible minimal movement of figure

        :return: list of min x,y move value
        :rtype: list[tuple]
        """
        print(self.moved)
        if capture_move:
            return [(-1,1), (-1,-1)]
        elif not self.moved:
            return [(-2,0), (-1,0)]
        else:
            return [(-1,0)]

class Rook(Figure):
    """
    Rook class for a rook figure

    :param Figure: superclass for this figure
    :type Figure: Figure
    """
    def __init__(self, surface: pygame.Surface, color: str, cord_y: int = 0, cord_x: int = 0) -> None:
        super().__init__(surface, color, cord_y, cord_x, True)
        self.image_path = fr"images/{color}_rook.png"
        self.setup_figure_drawing()
        self.draw_figure()

    def moves(self) -> list[tuple]:
        """
        move possible minimal movement of figure

        :return: list of min x,y move values
        :rtype: list[tuple]
        """
        return [(1,0),(0,1),(-1,0),(0,-1)]

class Knight(Figure):
    """
    Knight class for a knight figure

    :param Figure: superclass for this figure
    :type Figure: Figure
    """
    def __init__(self, surface: pygame.Surface, color: str, cord_y: int = 0, cord_x: int = 0) -> None:
        super().__init__(surface, color, cord_y, cord_x, can_jump= True)
        self.image_path = fr"images/{color}_knight.png"
        self.setup_figure_drawing()
        self.draw_figure()

    def moves(self) -> list[tuple]:
        """
        move possible minimal movement of figure

        :return: list of min x,y move values
        :rtype: list[tuple]
        """
        return [(2,1),(2,-1),(1,2),(1,-2),
                (-2,1),(-2,-1),(-1,2),(-1,-2)]

class Bishop(Figure):
    """
    Bishop class for a bishop figure

    :param Figure: superclass for this figure
    :type Figure: Figure
    """
    def __init__(self, surface: pygame.Surface, color: str, cord_y: int = 0, cord_x: int = 0) -> None:
        super().__init__(surface, color, cord_y, cord_x, True)
        self.image_path = fr"images/{color}_bishop.png"
        self.setup_figure_drawing()
        self.draw_figure()

    def moves(self) -> list[tuple]:
        """
        move possible minimal movement of figure

        :return: list of min x,y move values
        :rtype: list[tuple]
        """
        return [(1,1),(1,-1),(-1,1),(-1,-1)]

class Queen(Figure):
    """
    Queen class for a queen figure

    :param Figure: superclass for this figure
    :type Figure: Figure
    """
    def __init__(self, surface: pygame.Surface, color: str, cord_y: int = 0, cord_x: int = 0) -> None:
        super().__init__(surface, color, cord_y, cord_x, True)
        self.image_path = fr"images/{color}_queen.png"
        self.setup_figure_drawing()
        self.draw_figure()

    def moves(self) -> list[tuple]:
        """
        move possible minimal movement of figure

        :return: list of min x,y move values
        :rtype: list[tuple]
        """
        return [(1,0),(0,1),(-1,0),(0,-1),
                (1,1),(1,-1),(-1,1),(-1,-1)]

class King(Figure):
    """
    King class for a king figure

    :param Figure: superclass for this figure
    :type Figure: Figure
    """
    def __init__(self, surface: pygame.Surface, color: str, cord_y: int = 0, cord_x: int = 0) -> None:
        super().__init__(surface, color, cord_y, cord_x)
        self.image_path = fr"images/{color}_king.png"
        self.setup_figure_drawing()
        self.draw_figure()

    def moves(self) -> list[tuple]:
        """
        move possible minimal movement of figure

        :return: list of min x,y move values
        :rtype: list[tuple]
        """
        return [(1,0),(0,1),(-1,0),(0,-1),
                (1,1),(1,-1),(-1,1),(-1,-1)]