from typing import List

from game import BOARD_LENGTH, BOARD_WIDTH
from game.chess_figures import ChessFigure, PawnFigure, RookFigure
from game.player import Player, Color


class Board:
    def __init__(self):
        self._length = BOARD_LENGTH
        self._width = BOARD_WIDTH
        self._figures = self._init_figures()

    def _init_figures(self) -> List[List[ChessFigure]]:
        # TODO: Create all figures from classes and set them on table. For both parties
        figures: List[List[ChessFigure, None]] = []
        for i in range(0, BOARD_WIDTH):
            figures.append([])
            for j in range(0, BOARD_LENGTH):
                figures[i].append(None)
        # Pawns
        for i in range(0, BOARD_WIDTH):
            figures[1][i] = PawnFigure(Color.white)
            figures[BOARD_LENGTH - 2][i] = PawnFigure(Color.black)
        # Rooks
        figures[0][0] = RookFigure(Color.white)
        figures[0][BOARD_WIDTH - 1] = RookFigure(Color.white)
        figures[BOARD_LENGTH - 1][0] = RookFigure(Color.white)
        figures[BOARD_LENGTH - 1][BOARD_WIDTH - 1] = RookFigure(Color.black)
        # TODO: init the rest

        return figures

    def validate_move(self, current_player: Player, old_x: int, old_y: int, new_x: int, new_y: int) -> None:
        """
        Validate the desired move is legal
        This method checks if current player's next move is valid
        1. if figure on old_x,old_y belongs to current_player
        2. if the figure is allowed to make such move
        3. if there is no figure of the same color in the new place
        :param current_player: current player
        :param old_x: x placement of figure
        :param old_y: y placement of figure
        :param new_x: new x placement of figure
        :param new_y: new y placement of figure
        :return:  true if move is valid, false if move is invalid
        :raise IllegalGameStateException: raise exception if such move is invalid
        """
        pass

    def move_figure(self, old_x: int, old_y: int, new_x: int, new_y: int) -> None:
        """
        Move figure from old_x,old_y to new_x,new_y
        This method would only be called after a successful 'validate_move'

        :param old_x: x placement of figure
        :param old_y: y placement of figure
        :param new_x: new x placement of figure
        :param new_y: new y placement of figure
        """
        pass

    def check_winner(self) -> [Player, None]:
        """
        This method checks if there is a winner in the game (one king is alive and other is not)
        While both kings live, return None
        If one king is dead, return The Player with the living king
        """
        pass
