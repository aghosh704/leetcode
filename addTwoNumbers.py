# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def get_num_from_linked_list(self, node):
        nums = []
        while True:
            if node is not None:
                nums.append(str(node.val))
            else:
                break
            node = node.next
        nums = nums[::-1]
        return int(''.join(nums))
        # num = 0
        # for tmp in range(len(nums)):
        #     num = num + (nums[tmp] * pow(10, tmp))
        # return num

    def get_linked_list_from_num(self, n):
        n = str(n)
        n_rev = n[::-1]
        head = ListNode(int(n_rev[0:1]))
        last = head
        for idx in range(1, len(n_rev)):
            node = ListNode(int(n_rev[idx:idx+1]))
            last.next = node
            last = node
        return head


        return head

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = self.get_num_from_linked_list(l1)
        n2 = self.get_num_from_linked_list(l2)
        return self.get_linked_list_from_num(n1 + n2)

l1 = ListNode(3)
l2 = ListNode(4)
l3 = ListNode(2)
l4 = ListNode(5)

l1.next = l2
l2.next = l3
l3.next = l4


def prt_node(head):
    if head is None:
        return
    print('->', head.val, end=' ')
    prt_node(head.next)


def create_node_list_from_array(a):
    if a is None:
        return None
    head = ListNode(a[0])
    last = head
    for idx in range(1, len(a)):
        node = ListNode(a[idx])
        last.next = node
        last = node
    return head


a1 = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
a2 = [5,6,4]
nodes1 = create_node_list_from_array(a1)
nodes2 = create_node_list_from_array(a2)

n1 = Solution().get_num_from_linked_list(nodes1)
n2 = Solution().get_num_from_linked_list(nodes2)
s = n1 + n2
p = Solution().get_linked_list_from_num(s)
print(s)
prt_node(p)
