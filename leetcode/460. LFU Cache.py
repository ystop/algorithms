# -*- coding:utf-8 -*-

# 思路: 想用1个ht和1个list发现list必须遍历，即便用堆(logn)。那么就拆list,根据频率拆成n个list,频率之间用list或者ht再维护下。
# 3个数据结构+1个最小频率的维护: 1. cache用来维护基础数据 2.keyCounts 哈希表，用来维护每个key的频率
# 3.countKeyMapList用来维护每个count下面的元素。
class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.keyCounts = {}
        self.countKeyMapList = {}
        self.countKeyMapList[1] = []
        self.min = 1

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.capacity <= 0:
            return -1

        if key not in self.cache:
            return -1
        ret = self.cache[key]

        # 更新keyCount
        nowCount = self.keyCounts[key]
        self.keyCounts[key] = nowCount + 1

        # 更新countKeyMapSet
        self.countKeyMapList[nowCount].remove(key)
        if nowCount + 1 not in self.countKeyMapList:
            self.countKeyMapList[nowCount + 1] = []
        self.countKeyMapList[nowCount + 1].append(key)

        if nowCount == self.min and len(self.countKeyMapList[self.min]) == 0:
            self.min = nowCount + 1

        return ret

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.capacity <= 0:
            return -1

        if key in self.cache:
            self.cache[key] = value
            self.get(key)
        else:
            if self.capacity == len(self.cache):
                removeKey = self.countKeyMapList[self.min].pop(0)
                self.cache.pop(removeKey)
                self.keyCounts.pop(removeKey)
            self.cache[key] = value
            self.keyCounts[key] = 1
            self.countKeyMapList[1].append(key)
            self.min = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# cache = LFUCache(2)
#
# cache.put(1, 1)
# cache.put(2, 2)
# print cache.get(1)      # returns 1
# cache.put(3, 3)   # evicts key 2
# print cache.get(2)     # returns -1 (not found)
# print cache.get(3)     # returns 3.
# cache.put(4, 4)   # evicts key 1.
# print cache.get(1)      # returns -1 (not found)
# print cache.get(3)      # returns 3
# print cache.get(4)      # returns 4

cache = LFUCache(2)

cache.put(2, 1)
cache.put(3, 2)
print cache.get(3)      # returns 1
print cache.get(2)     # returns -1 (not found)

cache.put(4, 3)   # evicts key 1.
print cache.get(2)     # returns 3.
print cache.get(3)      # returns -1 (not found)
print cache.get(4)      # returns 3
#[null,null,null,2,1,null,1,-1,3]