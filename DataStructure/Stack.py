class Stack:

    __stack: list

    def __init__(self):
        self.__stack = []

    def push(self, item: object):
        """
        When we push an element on top of the stack, we only need to increase the field top by 1 and place the new
        element on this new position. If the stack is full before this push operation, we can not push.
        :param item: Item to insert.
        """
        self.__stack.append(item)

    def pop(self) -> object:
        """
        When we remove an element from the stack (the function also returns that removed element), we need to be careful
        if the stack was empty or not. If the stack is not empty, the topmost element of the stack is returned and the
        field top is decreased by 1. If the stack is empty, the function will return null.
        :return: The removed element
        """
        if len(self.__stack) > 0:
            return self.__stack.pop()
        else:
            return None

    def isEmpty(self) -> bool:
        """
        The function checks whether an array-implemented stack is empty or not. The function returns true if the stack is
        empty, false otherwise.
        :return: True if the stack is empty, false otherwise.
        """
        return len(self.__stack) == 0
