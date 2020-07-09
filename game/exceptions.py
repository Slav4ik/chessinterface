class InvalidMoveException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class IllegalGameStateException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
