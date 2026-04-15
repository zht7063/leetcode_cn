#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
# 
# 合并区间，参考灵神题解
# 

from typing import List


# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # --- sort with left endpoint. ---
        intervals.sort(key=lambda p: p[0])
        ans = []

        # --- traverse elems in intervals. ---
        for p in intervals:
            if ans and p[0] <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], p[1])
            else:
                ans.append(p)  # append new interval into ans
        return ans


# @lc code=end
