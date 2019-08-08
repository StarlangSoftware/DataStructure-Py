from DataStructure.Cache.CacheNode import CacheNode
from DataStructure.Cache.CacheLinkedList import CacheLinkedList


class LRUCache(object):

    """
    A constructor of LRUCache class which takes cacheSize as input. It creates new CacheLinkedList and
    HashMap.

    PARAMETERS
    ----------
    cacheSize : int
        Integer input defining cache size.
    """
    def __init__(self, cacheSize : int):
        self.cacheSize = cacheSize
        self.cache = CacheLinkedList()
        self.map = {}

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
    def contains(self, key: object) -> bool:
        return key in self.map

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
    def get(self, key: object) -> object:
        if key in self.map:
            cacheNode = self.get(key)
            self.cache.removeGiven(cacheNode)
            self.cache.add(cacheNode)
            return cacheNode.getData()
        else:
            return None

    """
    The add method take a key and a data as inputs. First it checks the size of the dictionary, if it is full (i.e
    equal to the given cacheSize) then it removes the last cacheNode in the list. If it has space for new entries,
    it creates new cacheNode with given inputs and adds this cacheNode to the linked list and also puts
    it to the dictionary.

    PARAMETERS
    ----------
    key : object
        object type input.
    data : objecy
        object type input
    """
    def add(self, key: object, data: object):
        if len(self.map) == self.cacheSize:
            removed = self.cache.remove()
            self.map.pop(removed.getKey())
        cacheNode = CacheNode(key, data)
        self.cache.add(cacheNode)
        self.map[key] = cacheNode