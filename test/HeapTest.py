import unittest

from DataStructure.Heap.MaxHeap import MaxHeap
from DataStructure.Heap.MinHeap import MinHeap


class MyTestCase(unittest.TestCase):

    def test_maxHeap(self):
        max_heap = MaxHeap(8, lambda x1, x2: 1 if x1>x2 else (0 if x1 == x2 else -1))
        max_heap.insert(4)
        max_heap.insert(6)
        max_heap.insert(2)
        max_heap.insert(5)
        max_heap.insert(3)
        max_heap.insert(1)
        max_heap.insert(7)
        self.assertEqual(7, max_heap.delete())
        self.assertEqual(6, max_heap.delete())
        self.assertEqual(5, max_heap.delete())

    def test_minHeap(self):
        min_heap = MinHeap(8, lambda x1, x2: 1 if x1>x2 else (0 if x1 == x2 else -1))
        min_heap.insert(4)
        min_heap.insert(6)
        min_heap.insert(2)
        min_heap.insert(5)
        min_heap.insert(3)
        min_heap.insert(1)
        min_heap.insert(7)
        self.assertEqual(1, min_heap.delete())
        self.assertEqual(2, min_heap.delete())
        self.assertEqual(3, min_heap.delete())


if __name__ == '__main__':
    unittest.main()
