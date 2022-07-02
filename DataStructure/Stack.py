class Stack:

    __stack: list

    def __init__(self):
        self.__stack = []

    def push(self, item: object):
        self.__stack.append(item)

    def pop(self) -> object:
        if len(self.__stack) > 0:
            return self.__stack.pop()
        else:
            return None

    def isEmpty(self) -> bool:
        return len(self.__stack) == 0
