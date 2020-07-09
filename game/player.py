from abc import ABC, abstractmethod
from enum import Enum

from game.board import Board


class Color(Enum):
    white = 1
    black = 2


class Player(ABC):
    def __init__(self, color: Color):
        self._color = color

    @abstractmethod
    def calculate_next_step(self, board: Board) -> (int, int, int, int):
        """
        This method will be implemented by the players

        Player receives a COPY of the game state (board) and returns the move he want to make
        :returns old_x, old_y, new_x, new_y
        """
        pass
