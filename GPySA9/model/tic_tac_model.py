class TicTacToe:
    tic_tac_toe_board = []
    order: int
    begin: int

    def __init__(self, order: int):
        self.tic_tac_toe_board = [["-", "-", "-"],
                                  ["-", "-", "-"], ["-", "-", "-"]]
        self.order = order
