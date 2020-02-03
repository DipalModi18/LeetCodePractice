"""
    Merge two sorted linked lists and return it as a new list.
    The new list should be made by splicing together the nodes of the first two lists.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def print_list(l):
        while l is not None:
            print("l.val: {} l.next: {}".format(l.val, l.next))
            l = l.next


class Solution(object):

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(x=None)
        my_list = l3

        while l1 and l2:
            if l1.val < l2.val:
                my_list.next = ListNode(l1.val)
                l1 = l1.next
            else:
                my_list.next = ListNode(l2.val)
                l2 = l2.next
            my_list = my_list.next
        my_list.next = l1 or l2
        return l3.next


l1 = ListNode(x=1)
l1.next = ListNode(x=2)
l1.next.next = ListNode(x=4)
# ListNode.print_list(l=l1)

l2 = ListNode(x=1)
l2.next = ListNode(x=3)
l2.next.next = ListNode(x=4)
# ListNode.print_list(l=l2)

ListNode.print_list(Solution().mergeTwoLists(l1=l1, l2=l2))
