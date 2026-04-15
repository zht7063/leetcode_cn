#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 轮转数组
# 
# 三次反转大法，但是注意不要用切片（因为切片会开辟新空间存储数组）

from typing import List


# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(i: int, j: int) -> None:
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        len_nums = len(nums)
        k %= len_nums
        reverse(0, len_nums - 1)
        reverse(0, k - 1)
        reverse(k, len_nums - 1)


# @lc code=end
