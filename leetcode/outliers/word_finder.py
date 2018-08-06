"""
Find a word within a grid of alphabets and count all the possible paths
Directions: horizontal, vertical or diagonal to any coordinate with a distance 1
Constraint: Path has to be a unique set of coordinates

S T A R
A R T Y
X K C S
T R A P

START

mahesh@zenefits.com
"""


class WordFinder:
    def __init__(self):
        self.neighbors = [[-1, 1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]

    def find_all_paths(self, grid, word):
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == word[0]:
                    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
                    result = []
                    self.helper(grid, 0, 0, visited, word, 0, result)
                    count += len(result)
        return count

    def helper(self, grid, row, col, visited, word, index, result):
        if index == len(word):
            result.append(1)
        adjacent = []
        for item in self.neighbors:
            adjacent.append([row + item[0], col + item[1]])
        for adj in adjacent:
            if 0 <= adj[0] < len(grid) and 0 <= adj[1] < len(grid[0]):
                if not visited[adj[0]][adj[1]]:
                    if index + 1 < len(word) and grid[adj[0]][adj[1]] == word[index + 1]:
                        visited[adj[0]][adj[1]] = True
                        self.helper(grid, adj[0], adj[1], visited, word, index + 1, result)
                        visited[adj[0]][adj[1]] = False


if __name__ == '__main__':
    word_finder = WordFinder()
    print(word_finder.find_all_paths(
        [['s', 't', 'a', 'r'], ['a', 'r', 't', 'y'], ['x', 'k', 'c', 's'], ['t', 'r', 'a', 'p']],
        "start"))
