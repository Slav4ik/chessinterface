import random
from copy import deepcopy

from game.board import Board
from game.exceptions import IllegalGameStateException
from game.player import (
    Player,
    Color
)


class Simulator:
    def __init__(self, white_player: Player, black_player: Player):
        self._white_player = white_player
        self._black_player = black_player

    def run(self) -> Player:
        """
        This method starts a chess game, and returns the winner

        On each turn, a player is given an COPY of the Board and returns the MOVE he wants to make.
        Any changes to the COPIED board are neglected.
        Malicious player gets automatically disqualified.

        This reminds of the frontend/backend validations,
        where the end-user may submit something malicious in the FE, so the validations are done on the BE.
        """
        current_player = self._white_player if bool(random.getrandbits(1)) else self._black_player
        board = Board()
        winner = None
        while not winner:
            board_copy = deepcopy(board)
            old_x, old_y, new_x, new_y = current_player.calculate_next_step(board_copy)

            try:
                board.validate_move(current_player, old_x, old_y, new_x, new_y)
            except IllegalGameStateException:
                if current_player == self._white_player:
                    return self._black_player
                else:
                    return self._white_player

            board.move_figure(old_x, old_y, new_x, new_y)
            winner = board.check_winner()

        return winner


if __name__ == '__main__':
    white_p = Player(Color.white)
    black_p = Player(Color.black)
    simulator = Simulator(white_p, black_p)
    simulator.run()
