"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    counterX = 0
    counterO = 0
    for raw in board:
        for cell in raw:
            if cell == 'X':
                counterX+=1
            elif cell == 'O':
                counterO+=1
    if counterX == counterO:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    row = 0
    column = 0
    for i in board:
        for j in i:
            if j == None:
                actions.append(((row),(column)))
            column+=1
        row+=1
        column = 0
    return set(actions)


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise ActionNotPossible
    else:
        board_copy = copy.deepcopy(board)
        if player(board) == 'X':
            board_copy[action[0]][action[1]]= 'X'
        else:
            board_copy[action[0]][action[1]]= 'O'
    return board_copy

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    x_list = []
    o_list = []
    row = 0
    column = 0
    for i in board:
        for j in i:
            if j == 'X':
                x_list.append(((row),(column)))
            elif j == 'O':
                o_list.append(((row),(column)))
            column+=1
        row+=1
        column = 0

    ### Vertical and horizontal line winner
    for j in range(3):
        if sum(1 for i in x_list if i[1]==j)==3 or sum(1 for i in x_list if i[0]==j)==3:
            result = 'X'
            break
        elif sum(1 for i in o_list if i[1]==j)==3 or sum(1 for i in o_list if i[0]==j)==3:
            result = 'O'
            break

    ### Diagonal winner
    if (0,0) in o_list and (1,1) in o_list and (2,2) in o_list:
        result = 'O'
    if (0,0) in x_list and (1,1) in x_list and (2,2) in x_list:
        result = 'X'
    if (0,2) in o_list and (1,1) in o_list and (2,0) in o_list:
        result = 'O'
    if (0,2) in x_list and (1,1) in x_list and (2,0) in x_list:
        result = 'X'

    if 'result' in locals():
        return result
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    x_list = []
    row = 0
    column = 0
    for i in board:
        for j in i:
            if j == 'X':
                x_list.append(((row),(column)))
            column+=1
        row+=1
        column = 0
    if len(x_list) == 5 or winner(board) == 'X' or winner(board) == 'Y':
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == 'X':
        return 1
    elif winner(board) == 'O':
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return (utility(board), None)
    else:
        if player(board) == 'X':
            value = float("-inf")
            for action in actions(board):
                move = minimax(result(board, action))[0]
                if (value < move):
                    value = move
                    step = action
        if player(board) == 'O':
            value = float("inf")
            for action in actions(board):
                move = minimax(result(board, action))[0]
                if (value > move):
                    value = move
                    step = action
        print ((value, step))
        return (value, step)
