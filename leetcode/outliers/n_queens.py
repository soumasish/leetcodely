"""Given nxn board place n queens on this board so that they don't attack each other. Find ONE placement of
queens which do not attack each other. """


class Solution:
    def findNQueens(self, n: int)->list:
        positions = [None for _ in range(n)]
        has_solution = self.helper(n, 0, positions)
        if has_solution:
            return positions
        else:
            return []

    def helper(self, n, row, positions):
        if n == row:
            return True
        col = 0
        for i in range(n):
            found_safe = True
            for j in range(row):
                if positions[j].col == col or (positions[j].row - positions[j].col == row - col) or (positions[j].row + positions[j].col == row + col):
                    found_safe = False
                    break
            if found_safe:
                positions[row] = Position(row, col)
                if self.helper(n, row+1, positions):
                    return True
        return False


class Position:
    def __init__(self, row, col):
        self.row = row
        self.col = col


if __name__ == '__main__':
    solution = Solution()
    print(solution.findNQueens(4))