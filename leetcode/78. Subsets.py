class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        ret = []
        path = []
        self.dfs(nums, 0, path, ret)
        return ret

    def dfs(self, nums, start, path, ret):
        ret.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            self.dfs(nums, i + 1, path, ret)
            path.pop()





s = Solution()
print s.subsets([1,2,3])