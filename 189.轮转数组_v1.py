#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 轮转数组
#
# 我的解法：
# 在数组后面拼接一个新的相同的数组，然后裁剪头尾，得到轮转结果。
# 需要注意：轮转的位数 k 可能大于数组长度，所以要先进行判断并求余数，以避免非法情况出现。
#

from typing import List


# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        k = k % len_nums
        nums[:] = nums[-k:] + nums[:-k]


# @lc code=end
