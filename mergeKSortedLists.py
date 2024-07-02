from heapq import heappop, heappush

# Class definition for a singly-linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        """
        Merge k sorted linked lists and return it as one sorted list.

        :param lists: A list of ListNode objects, where each ListNode is the head of a sorted linked list.
        :return: ListNode object that is the head of the merged sorted list.
        """
        heap = [] 
        for l in lists:
            current = l
            while current:
                heappush(heap,current.val)
                current = current.next

        if len(heap) < 1:
            return
        
        update_root = ListNode(heappop(heap))
        current = update_root

        while len(heap) > 0:
            new_node = ListNode(heappop(heap))
            current.next = new_node
            current = new_node

        return update_root
