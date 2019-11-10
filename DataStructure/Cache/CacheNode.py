from __future__ import annotations


class CacheNode(object):

    _key : object
    _data : object
    _previous : CacheNode
    _next : CacheNode

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
    def __init__(self, key: object, data: object):
        self._key = key
        self._data = data
        self._previous = None
        self._next = None

    """
    Getter for data value.

    RETURNS
    -------
    object
        data value.
    """
    def getData(self) -> object:
        return self._data

    """
    Getter for key value.

    RETURNS
    -------
    object
        key value.
    """
    def getKey(self) -> object:
        return self._key

    """
    Getter for the previous CacheNode.

    RETURNS
    -------
    CacheNode
        previous CacheNode.
    """
    def getPrevious(self) -> CacheNode:
        return self._previous

    """
    Getter for the next CacheNode.

    RETURNS
    -------
    CacheNode
        next CacheNode.
    """
    def getNext(self) -> CacheNode:
        return self._next

    """
    Setter for the previous CacheNode.

    PARAMETERS
    ----------
    previous : CacheNode
        previous CacheNode.
    """
    def setPrevious(self, previous: CacheNode):
        self._previous = previous

    """
    Setter for the next CacheNode.

    PARAMETERS
    ----------
    next : CacheNode
        next CacheNode.
    """
    def setNext(self, next: CacheNode):
        self._next = next