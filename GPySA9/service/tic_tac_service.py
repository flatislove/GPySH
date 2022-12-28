from aiogram import types
from random import randint
from model.tic_tac_model import TicTacToe
from aiogram.utils.callback_data import CallbackData

call_back_info = CallbackData('tXO', 'c', 't_b')


def array_to_string(arr):
    line_board = ""
    for row in arr:
        for el in row:
            line_board += f"{el} "
    return line_board.rstrip()


def string_to_array(string: str):
    arr = [[0] * 3 for i in range(3)]
    arr_line = string.split(" ")
    counter = 0
    for i in range(3):
        for j in range(3):
            arr[i][j] = arr_line[counter]
            counter += 1
    return arr


def get_sea_battle_field(ttt_board):
    line_board = array_to_string(ttt_board)
    markup = types.InlineKeyboardMarkup()
    for idxx, valuex in enumerate(ttt_board):
        markup.add(
            types.InlineKeyboardButton(ttt_board[idxx][0], callback_data=call_back_info.new(
                c=f"t_t_t={idxx}{0}", t_b=line_board)),
            types.InlineKeyboardButton(ttt_board[idxx][1], callback_data=call_back_info.new(
                c=f"t_t_t={idxx}{1}", t_b=line_board)),
            types.InlineKeyboardButton(ttt_board[idxx][2], callback_data=call_back_info.new(c=f"t_t_t={idxx}{2}", t_b=line_board)))
    return markup


def get_sea_battle_cell(call: types.CallbackQuery):
    markup = call.inline_message_id
    return markup


def mark_cell_user_action(cell: str, tic_tac_toe_board):
    row = int(cell[-2])
    column = int(cell[-1])
    if tic_tac_toe_board[row][column] == "-":
        tic_tac_toe_board[row][column] = "X"
        return 0, tic_tac_toe_board
    else:
        return -1, tic_tac_toe_board


def mark_cell_bot_action(tic_tac_toe_board):
    if tic_tac_toe_board[1][1] == "-":
        tic_tac_toe_board[1][1] = "O"
        return tic_tac_toe_board
    else:
        row_arr, col_arr = [], []
        for i in range(3):
            row, col = "", ""
            for j in range(3):
                row += tic_tac_toe_board[i][j]
                col += tic_tac_toe_board[j][i]
            row_arr.append(row)
            col_arr.append(col)
        act_row, act_col = "", ""
        for indr, row in enumerate(row_arr):
            if "XX-" == row or "X-X" == row or "-XX" == row:
                act_row = indr
                act_col = row.index("-")
                if tic_tac_toe_board[act_row][act_col] == "-":
                    tic_tac_toe_board[act_row][act_col] = "O"
                    return tic_tac_toe_board
        for indc, col in enumerate(col_arr):
            if "XX-" == col or "X-X" == col or "-XX" == col:
                act_col = indc
                act_row = col.index("-")
                if tic_tac_toe_board[act_row][act_col] == "-":
                    tic_tac_toe_board[act_row][act_col] = "O"
                    return tic_tac_toe_board
        while (True):
            row = randint(0, 2)
            column = randint(0, 2)
            if tic_tac_toe_board[row][column] == "-":
                tic_tac_toe_board[row][column] = "O"
                return tic_tac_toe_board


def check_win_or_end(tic_tac_toe_board):
    all = ""
    for i in range(3):
        row, col = "", ""
        for j in range(3):
            row += tic_tac_toe_board[i][j]
            col += tic_tac_toe_board[j][i]
        all += row
        if row[0] == row[1] == row[2] and row[0] != "-":
            return row[0]
        if col[0] == col[1] == col[2] and col[0] != "-":
            return col[0]
    if tic_tac_toe_board[0][0] == tic_tac_toe_board[1][1] == tic_tac_toe_board[2][2] and tic_tac_toe_board[1][1] != "-":
        return tic_tac_toe_board[0][0]
    if tic_tac_toe_board[0][2] == tic_tac_toe_board[1][1] == tic_tac_toe_board[2][0] and tic_tac_toe_board[1][1] != "-":
        return tic_tac_toe_board[0][2]
    if "-" not in all:
        return "Draw"
