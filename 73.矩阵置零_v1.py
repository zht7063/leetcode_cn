#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
# 使用额外数组实现
#

from typing import List

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_has_zero = [0 in row for row in matrix]
        col_has_zero = [0 in col for col in zip(*matrix)]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if row_has_zero[i] or col_has_zero[j]:
                    matrix[i][j] = 0

        for i, row0 in enumerate(row_has_zero):
            for j, col0 in enumerate(col_has_zero):
                if row0 or col0:
                    matrix[i][j] = 0

# @lc code=end

