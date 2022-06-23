"""
Input : 1 -> 5 -> 4 -> 3
Returned list : 1 -> 3 -> 4 -> 5
"""
class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

def sortList(head):
    if head is None or head.next is None:
        return head
    preslow = None
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        preslow = slow
        slow = slow.next
        fast = fast.next.next
    preslow.next = None
    return mergeTwoLists(sortList(head), sortList(slow))

def mergeTwoLists(head, slow):
    sortedList = Node(-1)
    sortedCounter = sortedList
    while head is not None and slow is not None:
        if head.val < slow.val:
            temp = Node(head.val)
            sortedCounter.next = temp
            head = head.next
        else:
            temp = Node(slow.val)
            sortedCounter.next = temp
            slow = slow.next
        sortedCounter = sortedCounter.next
    if head is not None:
        sortedCounter.next = head
    if slow is not None:
        sortedCounter.next = slow
    return sortedList.next



head = Node(1)
counter = head
counter.next = Node(4)
counter = counter.next
counter.next = Node(3)
counter = counter.next
counter.next = Node(2)
counter = counter.next
counter.next = Node(5)
counter = counter.next
counter.next = Node(2)

new_head = sortList(head)
while new_head != None:
    print(new_head.val)
    new_head = new_head.next