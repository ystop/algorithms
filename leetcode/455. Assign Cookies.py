# -*- coding:utf-8 -*-
# 思路:贪心算法 。
# 1 先排序，遍历所有的孩子，维持j作为cookie的最后点。如果cookie还有而且不满足孩子j++ 如果满足，总数+1，j+
# 2 先排序，遍历所有cookie，维持j作为孩子的位置。如果cookide满足不了孩子，cookie不要继续往下，如果cookie满足了孩子，总数+1，cookie往下走。
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = list(sorted(g))
        s = list(sorted(s))
        c = 0
        j = 0
        # for i in range(0, len(g)):
        #     while j < len(s) and s[j] < g[i]:
        #         j = j + 1
        #     if j < len(s):
        #         c = c + 1
        #         j = j + 1
        # return c
        for i in range(0, len(s)):
            if s[i] >= g[j]:
                j = j + 1
                c = c + 1
                if j >= len(g):
                    break
        return c


s = Solution()
print s.findContentChildren([10,9,8,7], [5,6,7,8])
print s.findContentChildren([1,2,3], [3])