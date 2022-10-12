from typing import Callable

from DataStructure.Heap.Heap import Heap


class MinHeap(Heap):

    def __init__(self, N: int, comparator: Callable[[object, object], int]):
        super().__init__(N, comparator)

    def compare(self, data1: object, data2: object) -> int:
        return -self.comparator(data1, data2)
