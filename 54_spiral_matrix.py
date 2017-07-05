"""Created by sgoswami on 4/15/17 as part of leetcode"""
"""Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order."""
"""For example, Given the following matrix:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5]"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        if len(matrix) == 1:
            return matrix[0]
        if len(matrix[0]) == 1:
            return [item[0] for item in matrix]
        end_row = len(matrix)
        end_col = len(matrix[0])
        result = []
        return self.helper(matrix, result, 0, 0, end_row, end_col)

    def helper(self, matrix, result, start_row, start_col, end_row, end_col):
        if end_row - start_row == 1 or end_col - start_col == 1:
            result.append(matrix[start_row][start_col])
            return result
        elif end_row - start_row == 0 or end_col - start_col == 0:
            return result

        for i in range(end_col):
            result.append(matrix[start_row][i])
        for i in range(end_row):
            if i == start_row:
                continue
            else:
                result.append(matrix[i][end_col-1])
        count = end_col - 2
        while count >= 0:
            result.append(matrix[end_row -1][count])
            count -= 1
        count = end_row - 2
        while count >= start_row + 1:
            result.append(matrix[count][start_col])
            count -= 1
        return self.helper(matrix, result, start_row + 1, start_col + 1, end_row -1, end_col -1)


if __name__ == '__main__':
    s = Solution()
    print(s.spiralOrder([
 [1, 2 ], [3, 4]
]))


