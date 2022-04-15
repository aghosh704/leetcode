"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list.
The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
"""

# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_node_list_from_array(a):
    if a is None or len(a) == 0:
        return None
    head = ListNode(a[0])
    last = head
    for idx in range(1, len(a)):
        node = ListNode(a[idx])
        last.next = node
        last = node
    return head

def prt_node(head):
    if head is None:
        print("\n")
        return
    print('->', head.val, end=' ')
    prt_node(head.next)


class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        while list1 and list2:
            if list1.val <= list2.val:
                res.append(list1.val)
                list1 = list1.next
            else:
                res.append(list2.val)
                list2 = list2.next

        if list1 is None and list2 is not None:
            while list2:
                res.append(list2.val)
                list2 = list2.next
        if list2 is None and list1 is not None:
            while list1:
                res.append(list1.val)
                list1 = list1.next

        head = ListNode(res[0])
        p = head
        for idx in range(1, len(res)):
            head.next = ListNode(res[idx])
            head = head.next
        return p







ln1 = create_node_list_from_array([1,2,3])
ln2 = create_node_list_from_array([1, 3, 4])
xyz = Solution().mergeTwoLists(ln1, ln2)
prt_node(xyz)