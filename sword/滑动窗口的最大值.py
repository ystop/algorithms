# -*- coding:utf-8 -*-
# 给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，
# 那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}；
# 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个：
#  {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}，
# {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。

# 双端队列，存下标。 遍历num，每次都append到队列中，并且维护，队列的第一个一定是最大的数据。
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if not num or not size:
            return []
        queue = []
        ret = []
        for i in range(0, len(num)):
            if queue:
                if i - queue[0] >= size:
                    queue.pop(0)
            while queue and num[queue[-1]] < num[i]:
                queue.pop()
            queue.append(i)
            if i >= size - 1:
                ret.append(num[queue[0]])
        return ret
s = Solution()
print s.maxInWindows([2,3,4,2,6,2,5,1], 3)