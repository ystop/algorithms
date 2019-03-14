# -*- coding:utf-8 -*-
# 输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。

# 思路1： 全排序
#     2. 先将数字列表转化成字符串链表，这样便于在一个字符串后面直接加上另外一个字符串。也就是 "3"+"321"="3321" 。
#   （2）构造一个比较函数，当 str1+str2>str2+str1 时我们认为字符串 str1>str2 。
#   （3）将字符串列表按照比较函数的规定进行冒泡排序（或其它方法排序），将定义为”大”的字符串放到最后。而”小”的字符串放在前面。最后将字符串列表链接起来，便是所求。
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        path = []
        ret = []
        self.dfs(numbers, path, ret)
        return min(ret)

    def dfs(self, numbers, path, ret):
        if len(path) == len(numbers):
            ret.append(''.join(path))
        for i in numbers:
            if str(i) in path:
                continue
            path.append(str(i))
            self.dfs(numbers, path,ret)
            path.pop()

    def PrintMinNumber1(self, numbers):
        # write code here
        def cmp(str1, str2):
            return 1 if str1 + str2 > str2 + str1 else -1
        numbers = map(str, numbers)
        numbers.sort(cmp)
        return ''.join(numbers)



s = Solution()
print s.PrintMinNumber([3,32,321])