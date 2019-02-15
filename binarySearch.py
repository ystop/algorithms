class Search(object):
    def binarySearch(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) / 2
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                return mid
        return -1

    def binarySearchRecursive(self, nums, target):
        return self._recursive(nums, 0, len(nums) - 1, target)


    def _recursive(self, nums, start, end, target):
        if start <= end:
            mid = start + (end - start) / 2
            if target < nums[mid]:
                return self._recursive(nums, start, mid - 1, target)
            elif target > nums[mid]:
                return self._recursive(nums, mid + 1, end, target)
            else:
                return mid
        else:
            return -1

s = Search()
print s.binarySearch([1,3,5,7,9], 9)
print s.binarySearchRecursive([1,3,5,7,9], 9)
