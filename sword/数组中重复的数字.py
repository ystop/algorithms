# -*- coding:utf-8 -*-
# 在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。
# 请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。

# 思路 1: 正好和下标对应，从头开始把数字和下标对好，如果后面还出现冲突就是。
# 2. 如果不允许修改原始数组的话， 取n的一半 ，读一遍计算两边count(n的复杂度），算出结果
# 其他： 排序/哈希表
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        for i in range(0, len(numbers)):
            while numbers[i] != i:
                if numbers[i] == numbers[numbers[i]]:
                    duplication[0] = numbers[i]
                    return True
                numbers[numbers[i]], numbers[i] = numbers[i], numbers[numbers[i]]
        return False


s = Solution()
duplication = [0]
print s.duplicate([2,3,1,0,2,5,3], duplication)
print duplication