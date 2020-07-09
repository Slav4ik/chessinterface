from abc import abstractmethod, ABC
from typing import List

from game.player import Color


class ChessFigure(ABC):
    def __init__(self, color: Color):
        self._color = color

    @abstractmethod
    def get_possible_moves(self, current_x: int, current_y: int) -> List[(int, int)]:
        """
        Given the figure and its current location returns all possible moves for this figure
        :param current_x: current x placement
        :param current_y: current y placement
        :return: List of (x,y) tuples
        """
        pass


class PawnFigure(ChessFigure):

    def get_possible_moves(self, current_x: int, current_y: int) -> List[(int, int)]:
        """
        This method will calculate all possible moves for a pawn (including diagonal attacks)
        :param current_x:  current x placement
        :param current_y: current y placement
        :return: List of (x,y) tuples
        """
        pass


class RookFigure(ChessFigure):
    def get_possible_moves(self, current_x: int, current_y: int) -> List[(int, int)]:
        """
        This method will calculate all possible moves for a rook
        :param current_x:  current x placement
        :param current_y: current y placement
        :return: List of (x,y) tuples
        """
        pass


class KnightFigure(ChessFigure):
    def get_possible_moves(self, current_x: int, current_y: int) -> List[(int, int)]:
        """
        This method will calculate all possible moves for a knight
        :param current_x:  current x placement
        :param current_y: current y placement
        :return: List of (x,y) tuples
        """
        pass


class BishopFigure(ChessFigure):
    def get_possible_moves(self, current_x: int, current_y: int) -> List[(int, int)]:
        """
        This method will calculate all possible moves for a bishop
        :param current_x:  current x placement
        :param current_y: current y placement
        :return: List of (x,y) tuples
        """
        pass


class QueenFigure(ChessFigure):
    def get_possible_moves(self, current_x: int, current_y: int) -> List[(int, int)]:
        """
        This method will calculate all possible moves for a queen
        :param current_x:  current x placement
        :param current_y: current y placement
        :return: List of (x,y) tuples
        """
        pass


class KingFigure(ChessFigure):
    def get_possible_moves(self, current_x: int, current_y: int) -> List[(int, int)]:
        """
        This method will calculate all possible moves for a king
        :param current_x:  current x placement
        :param current_y: current y placement
        :return: List of (x,y) tuples
        """
        pass
