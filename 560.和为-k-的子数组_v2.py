#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
# 
# 前缀和+哈希表 一次循环版本（一）
# 
# 使用 defaultdict 的必要性：不会返回 key-error 错误，而是直接返回 0
# 

from typing import List
from collections import defaultdict

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        cnt[0] = 1
        ans = s = 0  # s 用于记录滚动前缀和
        for x in nums:
            s += x
            ans += cnt[s - k]
            cnt[s] += 1
        return ans


# @lc code=end

