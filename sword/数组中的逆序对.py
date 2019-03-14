# -*- coding:utf-8 -*-
# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。
# 并将P对1000000007取模的结果输出。 即输出P%1000000007

# 思路: 比较难理解，就是归并排序，注意多了一个计数：如果左边比右边大，那么左边后面的都比右边这个大（有序），那么关于右边这个数的逆序对，就是 (左边总数 - 已经入的数量)
class Solution:
    def __init__(self):
        self.c = 0

    def InversePairs(self, data):
        # write code here
        self.merge(data)
        return self.c % 1000000007

    def merge(self, data):
        if len(data) <= 1:
            return data
        mid = len(data) // 2
        left = self.merge(data[:mid])
        right = self.merge(data[mid:])

        i = 0
        j = 0
        ret = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                ret.append(left[i])
                i = i + 1
            else:
                ret.append(right[j])
                j = j + 1
                self.c = self.c + len(left) - i
                if self.c >= 1000000007:
                    self.c %= 1000000007

        while i < len(left):
            ret.append(left[i])
            i = i + 1

        while j < len(right):
            ret.append(right[j])
            j = j + 1

        return ret

s = Solution()
print s.InversePairs([1,2,3,4,5,6,7,0])