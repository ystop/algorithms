# -*- coding:utf-8 -*-
# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。
# 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

# 思路:  index不相交的情况一直找;当左右差1的时候，右边就是最小值。 如果中间值比最左边要大或者相等，说明在右边；否则，中间值比最左边小，说明在左边
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        i = 0
        j = len(rotateArray) - 1
        if rotateArray[0] < rotateArray[-1]:
            return rotateArray[0]
        while i < j:
            if j - i == 1:
                return rotateArray[j]
            mid = i + (j - i) / 2
            if rotateArray[mid] >= rotateArray[i]:
                i = mid
            else:
                j = mid
        return False

s = Solution()
print s.minNumberInRotateArray([3, 4, 5, 1, 2])