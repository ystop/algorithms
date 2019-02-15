# -*- coding:utf-8 -*-
# sort
class Sort(object):
    def bubble(self, nums):
        for i in range(0, len(nums) - 1):
            flag = 0
            for j in range(0, len(nums) - 1 - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    flag = 1
            if flag == 0:
                break
        return nums

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

    def merge(self, nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.merge(nums[:mid])
        right = self.merge(nums[mid:])
        return self._merge(left, right)

    def _merge(self, left, right):
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
        while i < len(left):
            ret.append(left[i])
            i = i + 1
        while j < len(right):
            ret.append(right[j])
            j = j + 1
        return ret

    def heap(self, nums):
        i = self._heapParent(len(nums) - 1)
        while i >= 0:
            self._heapDown(nums, i)
            i = i - 1
        ret = []
        while nums:
            ret.append(nums[0])
            nums[0] = nums[-1]
            nums.pop()
            self._heapDown(nums, 0)
        return ret

    def _heapDown(self, heap, i):
        left = self._heapLeft(i)
        right = self._heapRight(i)
        minIndex = i
        while left < len(heap) and heap[left] < heap[minIndex]:
            minIndex = left
        while right < len(heap) and heap[right] < heap[minIndex]:
            minIndex = right

        if minIndex != i:
            heap[minIndex], heap[i] = heap[i], heap[minIndex]
            self._heapDown(heap, minIndex)

    def _heapLeft(self, i):
        return i * 2 + 1

    def _heapRight(self, i):
        return i * 2 + 2

    def _heapParent(self, i):
        return (i - 1) / 2

    def select(self, nums):
        for i in range(0, len(nums)):
            minIndex = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[minIndex]:
                    minIndex = j
            if minIndex != i:
                nums[minIndex], nums[i] = nums[i], nums[minIndex]
        return nums

    def insert(self, nums):
        for i in range(1, len(nums)):
            j = i
            while j > 0 and nums[j] < nums[j - 1]:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
                j = j - 1
        return nums

    def shell(self, nums):
        step = len(nums) // 2
        while step > 0:
            for i in range(step, len(nums)):
                j = i
                while j > 0 and nums[j] < nums[j - step]:
                    nums[j - step], nums[j] = nums[j], nums[j - step]
                    j = j - step
            step = step // 2
        return nums

s = Sort()
print s.bubble([1,3,5,2,6,7,8,4])
print s.quick([4,3,5,2,6,7,8,1])
print s.merge([4,3,5,2,6,7,8,1])
print s.heap([4,3,5,2,6,7,8,1])
print s.select([4,3,5,2,6,7,8,1])
print s.insert([4,3,5,2,6,7,8,1])
print s.shell([4,3,5,2,6,7,8,1])