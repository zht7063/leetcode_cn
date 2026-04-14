#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

from typing import List

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 计算两个数组长度
        len_s, len_p = len(s), len(p)

        if len_s < len_p:
            return []

        differ = 0
        ans = []
        count = [0] * 26  # 字符统计
        for i in range(len_p):
            count[ord(s[i]) - ord("a")] += 1  # 改为对 s 的字符做正向计数
            count[ord(p[i]) - ord("a")] -= 1  # 改为对 p 的字符做负向计数

        differ = [c != 0 for c in count].count(True)

        if differ == 0:
            ans.append(0)

        for i in range(len_s - len_p):  # 遍历次数
            # 此时 i 指向滑动窗口时候即将被排除的数字
            if count[ord(s[i]) - ord("a")] == 1:
                differ -= 1
            elif count[ord(s[i]) - ord("a")] == 0:
                differ += 1
            count[ord(s[i]) - ord("a")] -= 1

            # i+len_p 指向即将进入窗口的值
            if count[ord(s[i + len_p]) - ord("a")] == -1:
                differ -= 1
            elif count[ord(s[i + len_p]) - ord("a")] == 0:
                differ += 1
            count[ord(s[i + len_p]) - ord("a")] += 1

            if differ == 0:
                ans.append(i + 1)

        return ans


# @lc code=end
