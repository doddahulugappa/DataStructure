class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        head = self.head
        while head is not None:
            print(head.data)
            head = head.next


list1 = SLinkedList()
list1.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
e4 = Node("Thu")
e5 = Node("Fri")
e6 = Node("Sat")
e7 = Node("Sun")


# Link first Node to second node
list1.head.next = e2
e2.next = e3
e3.next = e4
e4.next = e5
e5.next = e6
e6.next = e7

list1.print_list()
