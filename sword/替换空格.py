# -*- coding:utf-8 -*-
# 请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

# 思路:
# 1. 直接replace  或者 从前往后，每次都需要移动n
# 2. 计算出空格的数量，开辟足够的空间。 2个指针，从后往前放数据。
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        #return s.replace(' ', '%20')

        spaceCount = s.count(' ')
        addS = [None] * spaceCount * 2

        p1 = len(s) - 1
        s = list(s) + addS
        p2 = len(s) - 1
        while p1 != p2:
            if s[p1] != ' ':
                s[p2] = s[p1]
            else:
                s[p2] = '0'
                p2 -= 1
                s[p2] = '2'
                p2 -= 1
                s[p2] = '%'
            p1 -= 1
            p2 -= 1

        return ''.join(s)

s = Solution()
print s.replaceSpace("We Are Happy")