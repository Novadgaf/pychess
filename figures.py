from msilib.schema import Error
import pygame

class Figure():
    """
    Figure super class for every figure
    """
    def __init__(self, surface: pygame.Surface, cord_y: int = 0, cord_x: int = 0) -> None:
        self.SURFACE = surface
        self.SQUARE_SIZE = 80

        self.cord_y = cord_y
        self.cord_x = cord_x
        
    def draw_figure(self, image_path: str, cord_y: int, cord_x: int) -> None:
        """
        draw_figure draws a figure on the board

        :param image_path: path to the figure image
        :type image_path: str
        :param cord_y: y cord where to draw the figure (0-7)
        :type cord_y: int
        :param cord_x: x cord where to draw the figure (0-7)
        :type cord_x: int
        """
        img = pygame.image.load(image_path)
        x_cord = cord_x*self.SQUARE_SIZE
        y_cord = cord_y*self.SQUARE_SIZE
        img = pygame.transform.scale(img, (80, 80))
        rec = pygame.Rect(x_cord,y_cord,80,80)
        self.SURFACE.blit(img, rec)
        pygame.display.flip()

class Pawn(Figure):
    """
    Pawn class for a pawn figure

    :param Figure: superclass for this figure
    :type Figure: Figure
    """
    def __init__(self, surface: pygame.Surface, color: str, cord_y: int = 0, cord_x: int = 0) -> None:
        super().__init__(surface, cord_y, cord_x)
        self.image = fr"images/{color}_pawn.png"
        self.draw_figure(self.image, self.cord_y, self.cord_x)

    def move(self) -> list[tuple]:
        """
        move possible minimal movement of figure

        :return: list of min x,y move value
        :rtype: list[tuple]
        """
        return [(0,1)]

class Rook(Figure):
    """
    Rook class for a rook figure

    :param Figure: superclass for this figure
    :type Figure: Figure
    """
    def __init__(self, surface: pygame.Surface, color: str, cord_y: int = 0, cord_x: int = 0) -> None:
        super().__init__(surface, cord_y, cord_x)
        self.image = fr"images/{color}_rook.png"
        self.draw_figure(self.image, self.cord_y, self.cord_x)

    def move(self) -> list[tuple]:
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
        super().__init__(surface, cord_y, cord_x)
        self.image = fr"images/{color}_knight.png"
        self.draw_figure(self.image, self.cord_y, self.cord_x)

    def move(self) -> list[tuple]:
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
        super().__init__(surface, cord_y, cord_x)
        self.image = fr"images/{color}_bishop.png"
        self.draw_figure(self.image, self.cord_y, self.cord_x)

    def move(self) -> list[tuple]:
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
        super().__init__(surface, cord_y, cord_x)
        self.image = fr"images/{color}_queen.png"
        self.draw_figure(self.image, self.cord_y, self.cord_x)

    def move(self) -> list[tuple]:
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
        super().__init__(surface, cord_y, cord_x)
        self.image = fr"images/{color}_king.png"
        self.draw_figure(self.image, self.cord_y, self.cord_x)

    def move(self) -> list[tuple]:
        """
        move possible minimal movement of figure

        :return: list of min x,y move values
        :rtype: list[tuple]
        """
        return [(1,0),(0,1),(-1,0),(0,-1),
                (1,1),(1,-1),(-1,1),(-1,-1)]