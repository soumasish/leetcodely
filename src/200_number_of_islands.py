"""Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
"""


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        visited = [[0 for _ in range(len(grid[i]))] for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1' and visited[i][j] == 0:
                    self.dfs(grid, visited, i, j)
                    count += 1
        return count

    def dfs(self, grid, visited, row, col):
        visited[row][col] = 1
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]) or visited[row][col] == 1 or grid[row][col] == '0':
            return
        self.dfs(grid, visited, row + 1, col)
        self.dfs(grid, visited, row - 1, col)
        self.dfs(grid, visited, row, col + 1)
        self.dfs(grid, visited, row, col - 1)


if __name__ == '__main__':
    grid = [['1', '1', '0', '0', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '1', '0', '0'],
            ['0', '0', '0', '1', '1']
            ]
    s = Solution()
    print(s.numIslands(grid))
