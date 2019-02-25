# -*- coding:utf-8 -*-
# 每年六一儿童节,牛客都会准备一些小礼物去看望孤儿院的小朋友,今年亦是如此。
# HF作为牛客的资深元老,自然也准备了一些小游戏。
# 其中,有个游戏是这样的:首先,让小朋友们围成一个大圈。然后,他随机指定一个数m,让编号为0的小朋友开始报数。
# 每次喊到m-1的那个小朋友要出列唱首歌,然后可以在礼品箱中任意的挑选礼物,并且不再回到圈中,
# 从他的下一个小朋友开始,继续0...m-1报数....这样下去....直到剩下最后一个小朋友,可以不用表演,
# 并且拿到牛客名贵的“名侦探柯南”典藏版(名额有限哦!!^_^)。请你试着想下,哪个小朋友会得到这份礼品呢？(注：小朋友的编号是从0到n-1)

# 思路: 1. 链表 2.数组存小朋友，如果不为1，一直转，记录下当前转到的index，每次转到谁t出
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n == 0 or m == 0:
            return -1
        data = [i for i in range(0, n)]
        begin = 0
        while len(data) != 1:
            index = (begin + m - 1) % len(data)
            data.pop(index)
            begin = index
        return data[0]

s = Solution()
print s.LastRemaining_Solution(4, 3)
