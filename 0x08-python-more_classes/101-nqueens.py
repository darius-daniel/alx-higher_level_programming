#!/usr/bin/python3
import sys

"""Solve the N queens problem by placing N non-attacking queens on an NxN
chessboard.
"""
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
elif not isinstance(sys.argv[1], int):
    print("N must be a number")
    sys.exit(1)
elif sys.arg[1] < 4:
    print("N must be at least 4")
    sys.exit(1)

queens_on_board = 0
N = sys.argv[1]

def isSafe(board, row, col):
    """Checks if the square on (row, col) are under attack by another queen on the board

    Args:
        board: the NxN board
        row: the row number of the square (counting starts from zero)
        col: the column number of the square (counting starts from zero)

    Returns:
        bool: True if not under attack, False if under attack
    """
    is_safe = True
    ## Check if there is already a queen on the row and column:
    
    # Check if another queen is already on column 'col'
    for r in range(N):
        if board[r][col] == 'Q':
            is_safe = False
            break
    # Check if another queen is already on row 'row'
    for c in range(N):
        if board[row][c] == 'Q':
            is_safe = False
            break

            

