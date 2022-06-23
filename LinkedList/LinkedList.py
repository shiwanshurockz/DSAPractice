class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, newData):
        new_node = Node(newData)
        new_node.next = self.head
        self.head = new_node

    def InsertAfter(self, prevNode, newData):

        if prevNode is None:
            print("GIven Node not in linked List")
            return
        newNode = Node(newData)
        newNode.next = prevNode.next
        prevNode.next = newNode

    def Append(self, newData):
        new_node = Node(newData)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def PrintList(self):
        last = self.head
        while last is not None:
            print(last.data)
            last = last.next

list = LinkedList()
list.push(100)
list.Append(6)
list.push(7)
list.push(1)
list.Append(4)
list.InsertAfter(list.head.next.next.next, 8)
list.PrintList()