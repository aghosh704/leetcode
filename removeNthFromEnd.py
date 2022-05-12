#Given the head of a linked list, remove the nth node from the end of the list and return its head.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def _print_list(n):
    while n:
        print(str(n.val) + "->", end=' ')
        n = n.next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        idx = 0
        fast_ptr = head
        slow_ptr = dummy
        while n > 0 and fast_ptr:
            fast_ptr = fast_ptr.next
            n -= 1

        while fast_ptr:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next

        slow_ptr.next = slow_ptr.next.next
        return dummy.next
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

_print_list(Solution().removeNthFromEnd(n1, 2))

