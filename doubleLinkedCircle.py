class doubleLinkedCircle:
    def __init__(self):
        pass

    def add

class node:
    def __init__(self, data):
        self.contents = data
        self.next = None
        self.previous = None

    @property
    def contents(self):
        return self.__contents

    @contents.setter
    def contents(self, newcontents):
        self.__contents = newcontents

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, newnode):
        self.__next = newnode

    @property
    def previous(self):
        return self.__previous

    @previous.setter
    def previous(self, newnode):
        self.__previous = newnode
