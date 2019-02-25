# -*- coding:utf-8 -*-
# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
# 思路: 注意是 搜索树: 所以满足 左 右边 根;小 大 中间 的规律。 获取到根的数据，然后遍历一遍，遍历到大于根的时候，就是前半部分，
# 再判断后半部分是否合法。 如果i比0大，说明sequence还有左，如果i比sequence的长度还小，说明有右，递归。 ?
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence) == 0:
            return False

        root = sequence[-1]

        i = 0
        for i in range(0, len(sequence)):
            if sequence[i] > root:
                break

        for j in range(i, len(sequence)):
            if sequence[j] < root:
                return False

        left = True
        right = True

        if i > 0:
            left = self.VerifySquenceOfBST(sequence[:i])
        if i < len(sequence) - 1:
            right = self.VerifySquenceOfBST(sequence[i:len(sequence) - 1])
        return left and right

s = Solution()
print s.VerifySquenceOfBST([1,5,4,8,12,10,6])
