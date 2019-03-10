class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.list = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.list.remove(key)
            self.list.insert(0, key)
            return self.cache[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        #print self.list
        if key in self.cache:
            self.list.remove(key)
            self.list.insert(0, key)
        else:
            if len(self.list) == self.capacity:
                self.cache.pop(self.list.pop())
            self.list.insert(0, key)
        self.cache[key] = value

cache = LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)
print cache.get(1)
cache.put(3, 3)
print cache.get(2)
cache.put(4, 4)
print cache.get(1)
print cache.get(3)
print cache.get(4)