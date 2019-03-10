# -*- coding:utf-8 -*-
# 思路：维护好一个dp数组，表示当前的最大利润，一个之前的最小价格，每一天，看今天的最大利润

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        minPrice = prices[0]
        dp = [None for i in range(0, len(prices))]
        dp[0] = 0
        for i in range(1, len(prices)):
            dp[i] = max(dp[i - 1], prices[i] - minPrice)
            minPrice = min(minPrice, prices[i])
        return dp[-1]


s = Solution()
print s.maxProfit([7,1,5,3,6,4])