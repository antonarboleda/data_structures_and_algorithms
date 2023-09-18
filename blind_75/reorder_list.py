# https://leetcode.com/problems/reorder-list/ 
# problem 143 Linked List 
# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves 
# may be changed.
"""
------ Session Notes
This was a failed interview for sure. 
I fumbled over several things
1. Getting dividing the list in half
2. Asserting when to use a dummy node Dummy > Node1 > Node2
3. Merging two lists

My take away here was that I need to refreshing translating linked lists 
ideas to code. I knew the algorithm but failed on implementation.

Starting at 3:30pm 9/8/23
Finished at 4:30?
"""
class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None
def reverse_list(l):
    old_root = l
    prev, cur = Node(-1), l
    while cur and prev:
        tmp = cur.next
        cur.next = prev
        prev = cur
        cur = tmp
    
    old_root.next = None
    return prev


def merge_two_lists(l1, l2):
    # l1 is longer
    dummy_head = cur = Node(-1)
    while l1 and l2:
        tmp_l1 = l1.next
        tmp_l2 = l2.next
        cur.next = l1
        cur = cur.next
        cur.next = l2
        l1 = tmp_l1
        l2 = tmp_l2
    return dummy_head.next

def reorder_list(root):
    dummy = Node(-1)
    dummy.next = root 
    fast, slow = root, dummy
    prev = dummy
    while fast and fast.next:
        fast = fast.next.next
        prev = prev.next.next
        slow = slow.next

    slow.next = None

    head2 = fast if fast else prev
    head2 = reverse_list(head2)
    return merge_two_lists(head2, root)





