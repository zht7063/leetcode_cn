#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#

from typing import List
from collections import defaultdict

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        ans = s = 0
        for x in nums:
            cnt[s] += 1
            s += x
            ans += cnt[s - k]
        return ans

# @lc code=end

