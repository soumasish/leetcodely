"""Write a program to solve a Sudoku puzzle by filling the empty cells.
Empty cells are indicated by the character '.'."""
import datetime


class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or len(board) == 0:
            return
        start_time = datetime.datetime.now()
        self.helper(board)
        end_time = datetime.datetime.now()
        print((end_time - start_time).total_seconds())

    def helper(self, board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '.':
                    for c in range(1, 10):
                        if self.is_valid(str(c), i, j, board):
                            board[i][j] = str(c)
                            if self.helper(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False
        return True

    def is_valid(self, val, row, col, board):
        for i in range(len(board)):
            if board[row][i] == val or board[i][col] == val:
                return False
            if board[3 * (row // 3) + i // 3][3 * (col // 3) + i // 3] == val:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    board = [['.', '.', '.', '3', '.', '7', '4', '.', '.'],
             ['9', '.', '.', '.', '.', '4', '.', '.', '8'],
             ['3', '7', '8', '.', '.', '.', '', '6', '.'],
             ['8', '2', '.', '9', '.', '.', '6', '.', '.'],
             ['.', '.', '1', '2', '.', '.', '9', '.', '4'],
             ['.', '4', '.', '.', '3', '8', '.', '5', '.'],
             ['2', '.', '8', '6', '9', '.', '7', '.', '.'],
             ['.', '9', '.', '.', '.', '.', '.', '.', '.'],
             ['7', '5', '.', '.', '.', '.', '.', '.', '.', '6']
             ]
    solution.solveSudoku(board)
    print(board)
