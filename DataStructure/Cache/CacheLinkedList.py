from DataStructure.Cache.CacheNode import CacheNode

class CacheLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None

    """
    The removeGiven method takes a CacheNode type input cacheNode. If cacheNode has a previous node, then assigns 
    cacheNode's next node as previous node's next node. If cacheNode has not got a previous node, then assigns its 
    next node as head node. Moreover, if cacheNode has a next node, then assigns cacheNode's previous node as next 
    node's previous node; if not assigns tail node's previous node as tail. By doing so it removes the cacheNode 
    from doubly list.

    PARAMETERS
    ----------
    cacheNode : CacheNode
        CacheNode type input to remove.
    """
    def removeGiven(self, cacheNode: CacheNode):
        previous = cacheNode.getPrevious()
        next = cacheNode.getNext()
        if previous is not None:
            previous.setNext(next)
        else:
            self.head = self.head.getNext()
        if next is not None:
            next.setPrevious(previous)
        else:
            self.tail = self.tail.getPrevious()

    """
    The add method adds given CacheNode type input cacheNode to the beginning of the doubly list.
    First it sets cacheNode's previous node as null and cacheNode's next node as head node. If head node is not null 
    then it assigns cacheNode's previous node as head node and if tail is null then it assigns cacheNode as tail.

    PARAMETERS
    ----------
    cacheNode : CacheNode
        CacheNode type input to add to the doubly list.
    """
    def add(self, cacheNode: CacheNode):
        cacheNode.setPrevious(None)
        cacheNode.setNext(self.head)
        if self.head is not None:
            self.head.setPrevious(cacheNode)
        self.head = cacheNode
        if self.tail is None:
            self.tail = cacheNode

    """
    The remove method removes the last element of the doubly list. It assigns the previous node of
    current tail as new tail. If the current tail is null then it assigns head to null.

    RETURNS
    -------
    CacheNode
        CacheNode type output tail which is removed from doubly list.
    """
    def remove(self) -> CacheNode:
        removed = self.tail
        self.tail = self.tail.getPrevious
        if self.tail is None:
            self.head = None
        return removed
