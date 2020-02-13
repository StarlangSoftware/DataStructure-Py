from DataStructure.Cache.CacheNode import CacheNode
from DataStructure.Cache.CacheLinkedList import CacheLinkedList


class LRUCache(object):

    __cacheSize: int
    __map: dict
    __cache: CacheLinkedList

    def __init__(self, cacheSize: int):
        """
        A constructor of LRUCache class which takes cacheSize as input. It creates new CacheLinkedList and
        HashMap.

        PARAMETERS
        ----------
        cacheSize : int
            Integer input defining cache size.
        """
        self.__cacheSize = cacheSize
        self.__cache = CacheLinkedList()
        self.__map = {}

    def contains(self, key: object) -> bool:
        """
        The contains method takes a object type input key and returns true if the dictionary has the given key, false
        otherwise.

        PARAMETERS
        ----------
        key : object
            object type input key.

        RETURNS
        -------
            true if the HashMap has the given key, false otherwise.
        """
        return key in self.__map

    def get(self, key: object) -> object:
        """
        The get method takes object type input key and returns the least recently used value. First it checks whether the
        dictionary has the given key, if so it gets the corresponding cacheNode. It removes that cacheNode from
        LinkedList and adds it again to the beginning of the list since it is more likely to be used again. At the end,
        returns the data value of that cacheNode.

        PARAMETERS
        ----------
        key : object
            object type input key.

        RETURNS
        -------
        object
            data value if the dictionary has the given key, None otherwise.
        """
        if key in self.__map:
            cacheNode = self.__map[key]
            self.__cache.removeGiven(cacheNode)
            self.__cache.add(cacheNode)
            return cacheNode.getData()
        else:
            return None

    def add(self, key: object, data: object):
        """
        The add method take a key and a data as inputs. First it checks the size of the dictionary, if it is full (i.e
        equal to the given cacheSize) then it removes the last cacheNode in the list. If it has space for new entries,
        it creates new cacheNode with given inputs and adds this cacheNode to the linked list and also puts
        it to the dictionary.

        PARAMETERS
        ----------
        key : object
            object type input.
        data : object
            object type input
        """
        if len(self.__map) == self.__cacheSize:
            removed = self.__cache.remove()
            self.__map.pop(removed.getKey())
        cacheNode = CacheNode(key, data)
        self.__cache.add(cacheNode)
        self.__map[key] = cacheNode
