#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#
# 「来自灵神大佬的题解 2」
# 基于动态规划的题解(空间优化版本)
#

from math import inf
from typing import List


# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -inf  # 答案可以是负数，不能初始化为 0
        f = 0
        for x in nums:
            f = max(0, f) + x
            ans = max(ans, f)
        return ans


# @lc code=end
