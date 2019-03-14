# -*- coding:utf-8 -*-
# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

# 思路: 1 排序 2 一个代表该数组中的某个数（result），一个代表次数（times），当遍历该数组时对其进行一下几种情况的处理：
# （1）当下一个数和我们保存的result的数字相同时，times加1；
# （2）当下一个数和我们保存的result的数字不同时，times减1；
# （3）当times减到0时，我们标记下一个数为result，并且置times为1.
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        times = 1
        result = numbers[0]
        for i in range(1, len(numbers)):
            if times == 0:
                result = numbers[i]
                times = 1
            elif result == numbers[i]:
                times += 1
            else:
                times -= 1
        # numbers = self.quick(numbers)
        # print numbers
        # result = numbers[len(numbers) / 2]

        c = 0
        for i in numbers:
            if result == i:
                c = c + 1
        if c > len(numbers) / 2:
            return result
        return 0

    def quick(self, nums):
        self._quick(nums, 0, len(nums) - 1)
        return nums

    def _quick(self, nums, start, end):
        if start < end:
            i, j, base = start, end, nums[start]
            while i < j:
                while i < j and nums[j] > base:
                    j = j - 1
                if i < j:
                    nums[i] = nums[j]
                    i = i + 1
                while i < j and nums[i] < base:
                    i = i + 1
                if i < j:
                    nums[j] = nums[i]
                    j = j - 1
            nums[i] = base
            self._quick(nums, start, i - 1)
            self._quick(nums, i + 1, end)


s = Solution()
print s.MoreThanHalfNum_Solution([1,2,3,2,4,2,5,2,3])