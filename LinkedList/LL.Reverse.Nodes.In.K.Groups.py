def reverse(start, end):
    if start.next is not None:
        return start
    prev = None
    cur = start
    n = start.next
    while (start != end):
        cur.next = prev
        prev = cur
        cur = n
        if n is not None:
            n = n.next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start = head
        end = head
        temp = 0
        while temp < k:
            end = end.next
            if end is None:
                return head
            k += 1
        newHead = reverseKGroup(end.next, k)
        reverse(start, end)
        start.next = newHead
        return end