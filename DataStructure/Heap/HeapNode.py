class HeapNode:

    __data: object

    def __init__(self, data: object):
        self.__data = data

    def getData(self) -> object:
        return self.__data
