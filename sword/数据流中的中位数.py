# -*- coding:utf-8 -*-
# 如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
# 如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
# 我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。

# 思路：实际上就是分成2部分，每次插入一部分。如果发生冲突，必须插到另外一个部分，需要另一部分给一个后，才给出去。
#  python 只支持小堆， 2个堆。 1堆大顶堆，2堆小顶堆，一个堆存一半，奇数进1堆，偶数进2堆，
# 如果应该进1，却比2堆最小的大，需要2堆给1堆一个最小的后，把这个数据给2堆了。
import heapq
class Solution:
    def __init__(self):
        self.heap1 = []
        self.heap2 = []
        self.c = 0

    def Insert(self, num):
        # write code here
        self.c += 1
        if not self.heap1:
            heapq.heappush(self.heap1, num * (-1))
        else:
            if self.c & 1 == 1:
                if num < self.heap2[0]:
                    heapq.heappush(self.heap1, num * (-1))
                else:
                    heapq.heappush(self.heap1, heapq.heappop(self.heap2) * (-1))
                    heapq.heappush(self.heap2, num)
            else:
                if num > self.heap1[0] * (-1):
                    heapq.heappush(self.heap2, num)
                else:
                    heapq.heappush(self.heap1, num * (-1))
                    heapq.heappush(self.heap2, heapq.heappop(self.heap1) * (-1))

    def GetMedian(self, n = None):
        # write code here
        if self.heap1:
            if (len(self.heap1) + len(self.heap2)) & 1 == 1:
                return self.heap1[0] * (-1)
            else:
                return (self.heap1[0] * (-1) + self.heap2[0]) / 2.0