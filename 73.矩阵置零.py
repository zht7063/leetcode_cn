#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
# 不使用额外数组实现
# 

from typing import List


# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        first_row_has_zero = 0 in matrix[0]  # 记录第一行是否包含 0
        first_col_has_zero = any(row[0] == 0 for row in matrix)  # 记录第一列是否包含 0

        # 用第一行 matrix[0][i] 保存 row_has_zero[i]
        # 用第一列 matrix[i][0] 保存 col_has_zero[j]
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if first_col_has_zero:
            for row in matrix:
                row[0] = 0

        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0


# @lc code=end
