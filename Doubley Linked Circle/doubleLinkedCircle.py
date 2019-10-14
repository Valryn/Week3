class DoubleLinkedCircle:
    """A double-linked circular list"""

    @property
    def head(self):
        return self.__head

    def __init__(self):
        self.__head = None

    def __str__(self):
        return self.head

    def __iter__(self):
        self.iterNode = self.head
        self.firstpass = True
        return self

    def __next__(self):
        if self.iterNode is self.head and not self.firstpass:
            raise StopIteration
        self.firstpass = False
        self.iterNode = self.iterNode.next
        return self.iterNode.previous

    def isEmpty(self):
        return self.head is None

    def append(self, data):
        """Adds a node to the end of the list"""
        # Check for empty list, then add the new node.
        if self.isEmpty():
            # Begin the list with a new node pointing to itself.
            self.__head = Node(data)
            self.__head.next = self.head
            self.__head.previous = self.head
        else:
            # Create new node and insert it at the end of the list by updating pointers.
            new = Node(data)
            end = self.head.previous

            new.next = self.head
            new.previous = end

            self.head.previous = new
            end.next = new

    def remove(self):
        """Removes a node from the end of the list"""
        end = self.head.previous

        # Update end node neighbors to point at eachother rather than the end node.
        self.head.previous = end.previous
        end.previous = self.head

    def remove(self, value):
        """Finds a node with a certain value, and removes it."""
        target = self.find(value)
        nextNode = target.next
        prevNode = target.previous

        nextNode.previous = prevNode
        prevNode.next = nextNode

    def size(self):
        """Counts the number of nodes in the list"""
        count = 0
        if self.isEmpty():
            pass
        else:
            current = self.head.next
            count = 1
            while current is not self.head:
                count += 1
                current = current.next
        return count

    def find(self, value):
        """Returns a node with the given value"""
        current = self.head
        found = None

        while current != self.head and not found:
            if current.contents == value:
                found = current
            else:
                current = current.next

        return found

    def contains(self, value):
        """Returns true if the given value exists in the list"""
        exists = not self.find(value) is None
        return exists


class Node:
    def __init__(self, data):
        self.contents = data
        self.next = None
        self.previous = None

    def __str__(self):
        return self.contents

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


myCircleList = DoubleLinkedCircle()
myCircleList.append("Hi! ")
myCircleList.append("How ")
myCircleList.append("are ")
myCircleList.append("you?")
print(myCircleList.size())
node = myCircleList.head
myMessage = ""
for node in myCircleList:
    myMessage = myMessage + str(node)
print(myMessage)

myCircleList2 = DoubleLinkedCircle()
myCircleList2.append("Hey!")
print(myCircleList2.size())
print(myCircleList2.head)

myCircleList3 = DoubleLinkedCircle()
print(myCircleList3.size())
print(myCircleList3.head)
