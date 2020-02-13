from __future__ import annotations


class CacheNode(object):

    __key: object
    __data: object
    __previous: CacheNode
    __next: CacheNode

    def __init__(self, key: object, data: object):
        """
        A constructor of CacheNode class which takes a key and a data as inputs and initializes private fields with
        these inputs.

        PARAMETERS
        ----------
        key : object
            K type input for representing keys.
        data : object
            T type input values represented by keys.
        """
        self.__key = key
        self.__data = data
        self.__previous = None
        self.__next = None

    def getData(self) -> object:
        """
        Getter for data value.

        RETURNS
        -------
        object
            data value.
        """
        return self.__data

    def getKey(self) -> object:
        """
        Getter for key value.

        RETURNS
        -------
        object
            key value.
        """
        return self.__key

    def getPrevious(self) -> CacheNode:
        """
        Getter for the previous CacheNode.

        RETURNS
        -------
        CacheNode
            previous CacheNode.
        """
        return self.__previous

    def getNext(self) -> CacheNode:
        """
        Getter for the next CacheNode.

        RETURNS
        -------
        CacheNode
            next CacheNode.
        """
        return self.__next

    def setPrevious(self, previous: CacheNode):
        """
        Setter for the previous CacheNode.

        PARAMETERS
        ----------
        previous : CacheNode
            previous CacheNode.
        """
        self.__previous = previous

    def setNext(self, next: CacheNode):
        """
        Setter for the next CacheNode.

        PARAMETERS
        ----------
        next : CacheNode
            next CacheNode.
        """
        self.__next = next
