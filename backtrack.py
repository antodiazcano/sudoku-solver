from sudoku import Sudoku
from typing import List



def backtrack(sudokus: List[Sudoku]) -> List[Sudoku]:
    
    """
    Backtrack algorithm.
    
    Parameters
    ----------
    boards : List of sudokus.
    
    Returns
    -------
    Winning sudokus (or False if there is no solution).
    """
    
    if len(sudokus) == 0:
        return False
    
    # Go through the board until we find a 0
    flag = False
    for x in range(sudokus[0].n):
        for y in range(sudokus[0].n):
            if sudokus[0].board[x][y] == 0:
                coord_x = x
                coord_y = y
                flag = True
                break
        if flag:
            break
    
    # Obtain all new possible sudokus
    new_sudokus = []
    for sudoku in sudokus:
        # Try all nums        
        for num in range(1, 10):
            if sudoku.possible_move(coord_x, coord_y, num):
                sudoku.add_number(coord_x, coord_y, num)
                board = [[sudoku.board[x][y] for y in range(sudoku.n)]
                          for x in range(sudoku.n)]
                new_sudokus.append(Sudoku(board))
    
    # Verbose
    zeros = sum(1 for row in new_sudokus[0].board for cell in row if cell == 0)
    if zeros == 1:
        print(zeros, "cell left")
    else:
        print(zeros, "cells left")
    print("Current sudokus:", len(new_sudokus))
    possible_sudokus = len(new_sudokus)*9**zeros
    if possible_sudokus > 10**6:
        print("Possible sudokus:", "{:.2e}".format(possible_sudokus), "\n")
    else:
        print("Possible sudokus:", possible_sudokus, "\n")
        
    # Solutions
    solutions = []
    if zeros == 0:
        for sudoku in new_sudokus:
            if sudoku.win():
                solutions.append(sudoku)
        return solutions
    
    return backtrack(new_sudokus)
