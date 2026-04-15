#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除了自身以外数组的乘积
#
# 灵神：前后缀分解法
# 

from typing import List

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        pre = [1] * len_nums
        for i in range(1, len_nums):
            pre[i] = pre[i-1] * nums[i-1]
        
        suf = [1] * len_nums
        for i in range(len_nums-2, -1, -1):
            suf[i] = suf[i + 1] * nums[i+1]
        
        return [p * s for p, s in zip(pre, suf)]

# @lc code=end

