"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def partition(A, B):
    firstList = ListNode(-1)
    secondList = ListNode(-1)
    firstCounter = firstList
    secondCounter = secondList
    while A != None:
        if A.val < B:
            temp = ListNode(A.val)
            firstCounter.next = temp
            firstCounter = firstCounter.next
        else:
            temp = ListNode(A.val)
            secondCounter.next = temp
            secondCounter = secondCounter.next
        A = A.next
    firstCounter.next = secondList.next
    head = firstList.next
    return head
head = ListNode(1)
counter = head
counter.next = ListNode(4)
counter = counter.next
counter.next = ListNode(3)
counter = counter.next
counter.next = ListNode(2)
counter = counter.next
counter.next = ListNode(5)
counter = counter.next
counter.next = ListNode(2)
ans = partition(head, 3)

while ans != None:
    print(ans.val)
    ans = ans.next