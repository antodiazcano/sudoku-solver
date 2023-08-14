from typing import List



class Sudoku:
    
    
    """ Class to create a sudoku board. 0 means an empty cell. """
    
    
    def __init__(self, board: List[List[int]]) -> None:
        
        """
        Constructor of the class.
        
        Parameters
        ----------
        board : Initial board.
        """
        
        self.board = board
        self.n = len(board)
        # Initial cells that are fixed
        self.fixed = [[True if self.board[x][y] != 0 else False
                       for y in range(self.n)] for x in range(self.n)]
        
    
    def __str__(self) -> str:
        
        """
        Str method.
        
        Returns
        -------
        ss : String representation of the board.
        """
        
        ss = ""
        
        for x in range(self.n):
            for y in range(self.n):
                ss += "[ " + str(self.board[x][y]) + " ]"
            ss += "\n"
        
        return ss
        
        
    def add_number(self, x: int, y: int, num: int) -> None:
        
        """
        Adds a number to a cell.
        
        Parameters
        ----------
        x, y : Coordinates of the cell we want to put the number.
        num  : Number we want to put.
        """
        
        if not self.fixed[x][y]:
            self.board[x][y] = num
        
    
    def possible_move(self, x: int, y: int, num: int) -> bool:
        
        """
        Tells if a movement is possible.
        
        Parameters
        ----------
        x, y : Coordinates of the cell we want to put the number.
        num  : Number we want to put.
        
        Returns
        -------
        True if the movement is possible, False otherwise.
        """
        
        # Fixed
        if self.fixed[x][y]:
            return False
        
        # Rows and columns ok
        for i in range(self.n):
            if self.board[x][i] == num or self.board[i][y] == num:
                return False
        
        # There are different numbers in the square
        if x % 3 == 0:
            center_x = x+1
        elif x % 3 == 1:
            center_x = x
        else:
            center_x = x-1
        if y % 3 == 0:
            center_y = y+1
        elif y % 3 == 1:
            center_y = y
        else:
            center_y = y-1
        # Check that the square has different numbers
        for x in range(3):
            for y in range(3):
                coord_x = center_x - 1 + x
                coord_y = center_y - 1 + y
                if self.board[coord_x][coord_y] == num:
                    return False
        
        return True
    
    
    def win(self) -> bool:
        
        """
        Tells if the game is finished.
        
        Returns
        -------
        True if the game is finished, False otherwise.
        """
        
        # All rows and columns have 9 different numbers
        for i in range(self.n):
            row = [self.board[i][x] for x in range(self.n)]
            column = [self.board[x][i] for x in range(self.n)]
            if 0 in row or 0 in column:
                return False
            if len(set(row)) < self.n or len(set(column)) < self.n:
                return False
        
        # Each square has 9 different numbers
        # Obtain the center of each square (there are 9)
        for x in range(3):
            for y in range(3):
                center_x = 3*x + 1
                center_y = 3*y + 1
                # Check that square has 9 different numbers
                nums = []
                for temp_x in range(3):
                    for temp_y in range(3):
                        coord_x = center_x - 1 + temp_x
                        coord_y = center_y - 1 + temp_y
                        num = self.board[coord_x][coord_y]
                        if num in nums:
                            return False
                        nums.append(num)
                        
        return True
        
