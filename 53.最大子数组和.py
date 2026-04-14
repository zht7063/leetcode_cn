#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

from typing import List
from math import inf


# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -inf  # 注意答案可以是负数，不能初始化成 0
        f = 0
        for x in nums:
            f = max(f, 0) + x
            ans = max(ans, f)
        return ans


# @lc code=end
