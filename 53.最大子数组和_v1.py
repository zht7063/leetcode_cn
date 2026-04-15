#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#
# 「来自灵神大佬的题解 1」
# 基于前缀和的类 [121] 买卖股票的最佳时机 的解法
# 
from math import inf
from typing import List


# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -inf  # 初始化答案为负无穷，保证能被任何实际的子数组和更新
        min_pre_sum = pre_sum = (
            0  # 初始前缀和为0，最小前缀和也为0（代表空数组的前缀和）
        )

        for x in nums:
            # 1. 计算当前位置的前缀和
            pre_sum += x

            # 2. 尝试更新最大子数组和（核心逻辑）
            # 用「当前前缀和」减去「之前见过的最小前缀和」，就能得到以当前元素 x 结尾的最大子数组和
            ans = max(ans, pre_sum - min_pre_sum)

            # 3. 更新最小前缀和，供下一次循环使用
            # 注意：这一步必须在计算 ans 之后！
            # 因为你不能用当前的前缀和减去它自己（那代表空数组，而题目要求子数组至少包含一个元素）
            min_pre_sum = min(min_pre_sum, pre_sum)

        return ans


# @lc code=end
