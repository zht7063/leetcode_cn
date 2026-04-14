#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#
from typing import List


# @lc code=start
class NumArray:
    def __init__(self, nums: List[int]):
        self.pre_sums = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.pre_sums[i + 1] = self.pre_sums[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.pre_sums[right + 1] - self.pre_sums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end
