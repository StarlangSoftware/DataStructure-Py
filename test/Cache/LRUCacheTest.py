import unittest
import time
from random import randrange

from DataStructure.Cache.LRUCache import LRUCache


class LRUCacheTest(unittest.TestCase):

    def test_1(self):
        cache = LRUCache(5)
        cache.add("item1", "1")
        cache.add("item2", "2")
        cache.add("item3", "3")
        self.assertTrue(cache.contains("item2"))
        self.assertFalse(cache.contains("item4"))

    def test_2(self):
        cache = LRUCache(2)
        cache.add("item1", "1")
        cache.add("item2", "2")
        cache.add("item3", "3")
        self.assertTrue(cache.contains("item2"))
        self.assertFalse(cache.contains("item1"))

    def test_3(self):
        cache = LRUCache(10000)
        for i in range(10000):
            cache.add(i, i)
        for i in range(1000):
            self.assertTrue(cache.contains(randrange(10000)))

    def test_4(self):
        cache = LRUCache(1000000)
        for i in range(1000000):
            cache.add(randrange(1000000), i)
        count = 0
        for i in range(1000000):
            if cache.contains(i):
                count = count + 1
        self.assertAlmostEqual(0.632, count / 1000000.0, 3)

    def test_5(self):
        cache = LRUCache(1000000)
        for i in range(1000000):
            cache.add(i, i)
        for j in range(1000):
            time1 = int(round(time.time() * 1000))
            for i in range(100000):
                data = randrange(1000000, 2000000)
                cache.add(data, data)
            print(int(round(time.time() * 1000)) - time1)

if __name__ == '__main__':
    unittest.main()
