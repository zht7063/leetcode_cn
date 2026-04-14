#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#
# 灵神大佬的 前缀和+哈希 的解法
# 第一个循环用来构建前缀和数组，从而将本题目转变为“两数之和”问题，
# 第二个循环用哈希表的方式解决两数之和问题，从而解决本题。
# 

from typing import List
from collections import defaultdict


# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s = [0] * (len(nums) + 1)  # 前缀和数组
        for i, x in enumerate(nums):  # 构建前缀和数组
            s[i + 1] = s[i] + x

        # 构建好子数组后，接下来就可以将题目转化为两数之和的解法（哈希
        cnt = defaultdict(int)  # 哈希表
        ans = 0
        for sj in s:
            ans += cnt[sj - k]
            cnt[sj] += 1

        return ans


# @lc code=end
