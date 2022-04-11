# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head):
        linked_list_len = 0
        ptr = head
        while True:
            if ptr is not None:
                linked_list_len += 1
                ptr = ptr.next
            else:
                break
        mid = linked_list_len // 2
        for tmp in range(mid):
            head = head.next
        return head


l1 = ListNode("a")
l2 = ListNode("b")
l3 = ListNode("b")
l4 = ListNode("a")

l1.next = l2
l2.next = l3
l3.next = l4
print(Solution().middleNode(l1))