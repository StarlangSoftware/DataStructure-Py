from abc import abstractmethod
from typing import Callable

from DataStructure.Heap.HeapNode import HeapNode


class Heap:
    __array: list
    __count: int
    __N: int
    comparator: Callable[[object, object], int]

    def __init__(self, N: int, comparator: Callable[[object, object], int]):
        """
        Constructor of the heap. According to the comparator, the heap could be min or max heap.
        :param N: Maximum number of elements in the heap.
        :param comparator: Comparator function to compare two elements.
        """
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
        """
        Swaps two heap nodes in the heap given their indexes.
        :param index1: Index of the first node to swap.
        :param index2: Index of the second node to swap.
        """
        tmp = self.__array[index1]
        self.__array[index1] = self.__array[index2]
        self.__array[index2] = tmp

    def percolateDown(self, no: int):
        """
        The function percolates down from a node of the tree to restore the max-heap property. Left or right children are
        checked, if one of them is larger than the current element of the heap, the iteration continues. The iteration is,
        determining the largest one of the node's children and switching that node's value with the current node's value.
        We need to check if current node's left and right children exist or not. These checks are done with for the left
        child and with for the right child.
        :param no: Index of the starting node to restore the max-heap property.
        """
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
        """
        The function percolates up from a node of the tree to restore the max-heap property. As long as the max-heap
        property is corrupted, the parent and its child switch their values. We need to pay attention that, the
        calculated index of the parent must be a valid number. In other words, while going upper levels,we need to see
        that we can not go up if we are at the root of the tree.
        :param no: Index of the starting node to restore the max-heap property.
        """
        parent = (no - 1) // 2
        while parent >= 0 and self.compare(self.__array[parent].getData(), self.__array[no].getData()) < 0:
            self.swapNode(parent, no)
            no = parent
            parent = (no - 1) // 2

    def delete(self) -> object:
        """
        The function will return the first element, therefore the first element is stored in the variable, and the first
        element of the heap is set to the last element of the heap. After that, in order to restore the max-heap
        property, we percolate down the tree using the function. As a last step, the number of element in the heap is
        decremented by one.
        :return: The first element
        """
        tmp = self.__array[0]
        self.__array[0] = self.__array[self.__count - 1]
        self.percolateDown(0)
        self.__count = self.__count - 1
        return tmp.getData()

    def insert(self, data: object):
        """
        The insertion of a new element to the heap, proceeds from the leaf nodes to the root node. First the new element
        is added to the end of the heap, then as long as the max-heap property is corrupted, the new element switches
        place with its parent.
        :param data: New element to be inserted.
        """
        if self.__count < self.__N:
            self.__count = self.__count + 1
        self.__array[self.__count - 1] = HeapNode(data)
        self.percolateUp(self.__count - 1)

    def __repr__(self):
        return f"{self.__array}"
