#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#
# 「来自灵神大佬的题解 2」
# 基于动态规划的题解
#

from typing import List


# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        f = [0] * len(nums)
        f[0] = nums[0]
        for i in range(1, len(nums)):
            f[i] = max(0, f[i - 1]) + nums[i]
        return max(f)


# @lc code=end
