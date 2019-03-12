# -*- coding:utf-8 -*-
# 给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。

# 思路: 构建2个数组，b1,b2. b1是A[i]的之前的乘积,b2是A[i]之后的乘积，最后把他两再乘以起来就可以了。

class Solution:
    def multiply(self, A):
        # write code here
        b1 = [1]
        for i in range(0, len(A) - 1):
            b1.append(A[i] * b1[i])

        b2 = [1]
        A = list(reversed(A))
        for i in range(0, len(A) - 1):
            b2.append(A[i] * b2[i])
        b2 = list(reversed(b2))



        b = []
        i = 0
        while i <= len(A) - 1:
            b.append(b1[i] * b2[i])
            i = i + 1
        return b

s = Solution()
print s.multiply([1,2,3,4,5])
#[120,60,40,30,24]