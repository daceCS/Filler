#!/usr/bin/env python3
from math import inf as infinity
from random import choice
import platform
import time
from os import system

"""
An implementation of Minimax AI Algorithm in Tic Tac Toe,
using Python.
This software is available under GPL license.
Author: Clederson Cruz
Year: 2017
License: GNU GENERAL PUBLIC LICENSE (GPL)
"""

HUMAN = -1
COMP = +1
board = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]


# Called at start of ai turn to move.
def evaluate(state):
    """
    Function to heuristic evaluation of state.
    :param state: the state of the current board
    :return: +1 if the computer wins; -1 if the human wins; 0 draw
    """
    if wins(state, COMP):
        score = +1
    elif wins(state, HUMAN):
        score = -1
    else:
        score = 0
    #    print("in evaluate = " + str(score))
    return score


def wins(state, player):
    """
    This function tests if a specific player wins. Possibilities:
    * Three rows    [X X X] or [O O O]
    * Three cols    [X X X] or [O O O]
    * Two diagonals [X X X] or [O O O]
    :param state: the state of the current board
    :param player: a human or a computer
    :return: True if the player wins
    """
    win_state = [
        [state[0][0], state[0][1], state[0][2], state[0][3]],
        [state[1][0], state[1][1], state[1][2], state[1][3]],
        [state[2][0], state[2][1], state[2][2], state[2][3]],
        [state[3][0], state[3][1], state[3][2], state[3][3]],
    ]
    if [player, player, player, player] in win_state:
        return True
    else:
        return False


def game_over(state):
    """
    This function test if the human or computer wins
    :param state: the state of the current board
    :return: True if the human or computer wins
    """
    return wins(state, HUMAN) or wins(state, COMP)


def empty_cells(state):
    """
    Each empty cell will be added into cells' list
    :param state: the state of the current board
    :return: a list of empty cells
    """
    cells = []

    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])

    return cells


def valid_move(x, y):
    """
    A move is valid if the chosen cell is empty
    :param x: X coordinate
    :param y: Y coordinate
    :return: True if the board[x][y] is empty
    """
    if [x, y] in empty_cells(board):
        return True
    else:
        return False


def set_move(x, y, player):
    """
    Set the move on board, if the coordinates are valid
    :param x: X coordinate
    :param y: Y coordinate
    :param player: the current player
    """
    if valid_move(x, y):
        board[x][y] = player
        return True
    else:
        return False


tries = 0


# Recursive code that does the Minimax algorithm.
def minimax(state, depth, player):
    global tries
    """
    AI function that choice the best move
    :param state: current state of the board
    :param depth: node index in the tree (0 <= depth <= 9),
    but never nine in this case (see iaturn() function)
    :param player: an human or a computer
    :return: a list with [the best row, best col, best score]
    """
    tries += 1
    if tries % 1000000 == 999999:
        print(tries)

    if player == COMP:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    # print("depth = " + str(depth))
    if depth == 0 or game_over(state):
        score = evaluate(state)

        return [-1, -1, score]

    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = minimax(state, depth - 1, -player)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == COMP:
            if score[2] > best[2]:
                best = score  # max value
                if best[2] == 1:
                    return best

        else:
            if score[2] < best[2]:
                best = score  # min value
                if best[2] == -1:
                    return best

    return best


def render(state, c_choice, h_choice):
    """
    Print the board on console
    :param state: current state of the board
    """

    chars = {
        -1: h_choice,
        +1: c_choice,
        0: ' '
    }
    str_line = '--------------------'

    print('\n' + str_line)
    for row in state:
        for cell in row:
            symbol = chars[cell]
            print(f'| {symbol} |', end='')
        print('\n' + str_line)


# Main code for ai to move.
def ai_turn(c_choice, h_choice):
    global tries
    """
    It calls the minimax function if the depth < 9,
    else it choices a random coordinate.
    :param c_choice: computer's choice X or O
    :param h_choice: human's choice X or O
    :return:
    """
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    render(board, c_choice, h_choice)

    if depth == 16:
        # If AI gets 1st choice then pick a random location to start game.
        x = choice([0, 1, 2, 3])
        y = choice([0, 1, 2, 3])
    # else:
    tries = 0
    move = minimax(board, depth, COMP)
    print("total tries = " + str(tries))

    x, y = move[0], move[1]

    set_move(x, y, COMP)
    time.sleep(1)


doai_turn = False


def ai_turn2(c_choice, h_choice):
    global doai_turn
    """
    The Human plays choosing a valid move.
    :param c_choice: computer's choice X or O
    :param h_choice: human's choice X or O
    :return:
    """
    if doai_turn:
        ai_turn(c_choice, h_choice)
        return

    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    # Dictionary of valid moves
    move = -1
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [0, 3],
        5: [1, 0], 6: [1, 1], 7: [1, 2], 8: [1, 3],
        9: [2, 0], 10: [2, 1], 11: [2, 2], 12: [2, 3],
        13: [3, 0], 14: [3, 1], 15: [3, 2], 16: [3, 3],
    }

    render(board, c_choice, h_choice)

    while move < 1 or move > 16:
        try:
            print("top move = " + str(move))
            move = int(input('AI use numpad (1..16) or 0 for ai to move:'))
            print("move = " + str(move))
            if move == 0:  # Have the ai make the move.
                doai_turn = True
                ai_turn(c_choice, h_choice)
                return

            coord = moves[move]
            print("coord = " + str(coord))
            can_move = set_move(coord[0], coord[1], COMP)

            if not can_move:
                print('Bad move')
                move = -1
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')


def human_turn(c_choice, h_choice):
    """
    The Human plays choosing a valid move.
    :param c_choice: computer's choice X or O
    :param h_choice: human's choice X or O
    :return:
    """
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    # Dictionary of valid moves
    move = -1
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [0, 3],
        5: [1, 0], 6: [1, 1], 7: [1, 2], 8: [1, 3],
        9: [2, 0], 10: [2, 1], 11: [2, 2], 12: [2, 3],
        13: [3, 0], 14: [3, 1], 15: [3, 2], 16: [3, 3],
    }

    render(board, c_choice, h_choice)

    while move < 1 or move > 16:
        try:
            print("top move = " + str(move))
            move = int(input('Human use numpad (1..16): '))
            print("move = " + str(move))
            coord = moves[move]
            print("coord = " + str(coord))
            can_move = set_move(coord[0], coord[1], HUMAN)

            if not can_move:
                print('Bad move')
                move = -1
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')


def main():
    """
    Main function that calls all functions
    """
    h_choice = ''  # X or O
    c_choice = ''  # X or O
    first = ''  # if human is the first

    # Human may starts first
    while first != 'Y' and first != 'N':
        try:
            first = input('First to start?[y/n]: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    if first == 'Y':
        h_choice = 'X'
        c_choice = 'O'
    else:
        h_choice = 'O'
        c_choice = 'X'

    # Main loop of this game
    if first == 'N':
        ai_turn2(c_choice, h_choice)
    while len(empty_cells(board)) > 0 and not game_over(board):
        human_turn(c_choice, h_choice)
        ai_turn2(c_choice, h_choice)

    # Game over message
    if wins(board, HUMAN):
        render(board, c_choice, h_choice)
        print('YOU WIN!')
    elif wins(board, COMP):
        render(board, c_choice, h_choice)
        print('YOU LOSE!')
    else:
        render(board, c_choice, h_choice)
        print('DRAW!')

    exit()


if __name__ == '__main__':
    main()