import unittest

from DataStructure.Cache.CacheLinkedList import CacheLinkedList
from DataStructure.Cache.CacheNode import CacheNode


class CacheLinkedListTest(unittest.TestCase):

    def test_1(self):
        cacheLinkedList = CacheLinkedList()
        cacheLinkedList.add(CacheNode("item1", "1"))
        cacheLinkedList.add(CacheNode("item2", "2"))
        removed = cacheLinkedList.remove()
        self.assertEquals("item1", removed.getKey())
        self.assertEquals("1", removed.getData())
        removed = cacheLinkedList.remove()
        self.assertEquals("item2", removed.getKey())
        self.assertEquals("2", removed.getData())

    def test_2(self):
        cacheLinkedList = CacheLinkedList()
        for i in range(1000):
            cacheLinkedList.add(CacheNode(i.__str__(), i.__str__()))
        for i in range(1000):
            removed = cacheLinkedList.remove()
            self.assertEquals(i.__str__(), removed.getKey())
            self.assertEquals(i.__str__(), removed.getData())


if __name__ == '__main__':
    unittest.main()
