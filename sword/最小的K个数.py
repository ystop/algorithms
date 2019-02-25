# -*- coding:utf-8 -*-
# 输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。

# 思路: 大顶堆，读一遍
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if not tinput or k <= 0 or k > len(tinput):
            return []
        heap = tinput[:k]
        p = self._parent(k - 1)
        while p >= 0:
            self._down(heap, p)
            p = p - 1
        for i in tinput[k:]:
            if i < self.getMax(heap):
                self._replace(heap, i)
        return sorted(heap)

    def getMax(self, heap):
        return heap[0]

    def _replace(self, heap, i):
        heap[0] = i
        self._down(heap, 0)

    def _down(self, heap, i):
        left = self._left(i)
        right = self._right(i)
        maxIndex = i
        if left < len(heap) and heap[left] > heap[i]:
            maxIndex = left
        if right < len(heap) and heap[right] > heap[maxIndex]:
            maxIndex = right
        if maxIndex != i:
            heap[maxIndex], heap[i] = heap[i], heap[maxIndex]
            self._down(heap, maxIndex)

    def _left(self, i):
        return i * 2 + 1

    def _right(self, i):
        return i * 2 + 2

    def _parent(self, i):
        return (i - 1) / 2

s = Solution()
print s.GetLeastNumbers_Solution([4,5,1,6,2,7,3,8], 4)