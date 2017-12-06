"""Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum
enemies you can kill using one bomb. The bomb kills all the enemies in the same row and column from the planted point
until it hits the wall since the wall is too strong to be destroyed.
Note that you can only put the bomb at an empty cell."""

class Solution:
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        max_kills = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][i] == '0':
                    kills = self.total_kills(i, j, grid)
                    max_kills = max(max_kills, kills)
        return max_kills

    def total_kills(self, row, col, grid):
        count = 0
        #col kill
        for i in range(len(grid)):
            if grid[row][i] == 'E':
                count += 1
            if grid[row][i] == 'W':
                break

        for j in range(len(grid)):
            pass




