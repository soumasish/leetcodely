"""Created by sgoswami on 6/9/17."""


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        results = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        self.helper(0, results, board)

    def helper(self, col, board, result):
        if col == len(board):
            pass
        for i in range(len(board)):
            if self.validate(board, i, col):
                board[i][col] = 'Q'
                self.helper(board, i+1, col)

    def validate(self, board, x, y):
        for i in range(len(board)):
            if board[x][i] == 'Q' or board[i][y] == 'Q':
                return False
        i, j = 0, 0
        while x - i >= 0 and y - j >= 0:
            if board[x-i][y-j] == 'Q':
                return False
            i += 1
            j += 1
        i, j = 0, 0
        while x + i < len(board) and y - j >= 0:
            if board[x + i][y - j] == 'Q':
                return False
            i += 1
            y += 1
        return True

if __name__ == '__main__':
    solution = Solution()
    print(solution.solveNQueens(4))

def findNQueens():
    pass




