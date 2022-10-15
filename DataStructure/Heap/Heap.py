from abc import abstractmethod
from typing import Callable

from DataStructure.Heap.HeapNode import HeapNode


class Heap:

    __array: list
    __count: int
    __N: int
    comparator: Callable[[object, object], int]

    def __init__(self, N: int, comparator: Callable[[object, object], int]):
        self.comparator = comparator
        self.__count = 0
        self.__array = []
        self.__N = N
        for i in range(N):
            self.__array.append(None)

    @abstractmethod
    def compare(self, data1: object, data2: object) -> int:
        pass

    def isEmpty(self) -> bool:
        return self.__count == 0

    def swapNode(self, index1: int, index2: int):
        tmp = self.__array[index1]
        self.__array[index1] = self.__array[index2]
        self.__array[index2] = tmp

    def percolateDown(self, no: int):
        left = 2 * no + 1
        right = 2 * no + 2
        while (left < self.__count and self.compare(self.__array[no].getData(), self.__array[left].getData()) < 0) or \
                (right < self.__count and self.compare(self.__array[no].getData(), self.__array[right].getData()) < 0):
            if right >= self.__count or self.compare(self.__array[left].getData(), self.__array[right].getData()) > 0:
                self.swapNode(no, left)
                no = left
            else:
                self.swapNode(no, right)
                no = right
            left = 2 * no + 1
            right = 2 * no + 2

    def percolateUp(self, no: int):
        parent = (no - 1) // 2
        while parent >= 0 and self.compare(self.__array[parent].getData(), self.__array[no].getData()) < 0:
            self.swapNode(parent, no)
            no = parent
            parent = (no - 1) // 2

    def delete(self) -> object:
        tmp = self.__array[0]
        self.__array[0] = self.__array[self.__count - 1]
        self.percolateDown(0)
        self.__count = self.__count - 1
        return tmp.getData()

    def insert(self, data: object):
        if self.__count < self.__N:
            self.__count = self.__count + 1
        self.__array[self.__count - 1] = HeapNode(data)
        self.percolateUp(self.__count - 1)

    def __repr__(self):
        return f"{self.__array}"
