"""Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
"""


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        num_islands = 0
        visited = [[0] * len(grid[0]) for _ in range(len(grid))]

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == '1' and visited[row][col] == '0':
                    num_islands += 1
                    self.dfs(grid, visited, row, col)
        return num_islands

    def dfs(self, grid, visited, row, col):
        if row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0]) and grid[row][col] == '1' and visited[row][
            col] == '0':
            visited[row][col] = '1'
            self.dfs(grid, visited, row, col + 1)
            self.dfs(grid, visited, row + 1, col)
            self.dfs(grid, visited, row, col - 1)
            self.dfs(grid, visited, row - 1, col)


def app():
    grid1 = [[1, 1, 1, 1, 0],
             [1, 1, 0, 1, 0],
             [1, 1, 0, 0, 0],
             [0, 0, 0, 0, 0]
             ]
    grid2 = [['11000'],
             ['11000'],
             ['00100'],
             ['00011']
             ]
    s = Solution()
    print(s.numIslands(grid1))
    print(s.numIslands(grid2))


if __name__ == '__main__':
    app()
