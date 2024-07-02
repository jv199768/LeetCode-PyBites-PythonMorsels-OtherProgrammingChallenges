from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # Helper function to reverse a linked list
        def reverse_list(node):
            prev, current = None, node
            while current:
                next_temp = current.next
                current.next = prev
                prev = current
                current = next_temp
            return prev
      
        # The dummy node is used to handle edge cases smoothly
        dummy = ListNode()
        dummy.next = head
        prev_group = dummy
      
        while head:
            # Check if there is a full group to reverse
            count = 0
            current = head
            while count < k and current:
                current = current.next
                count += 1
          
            # If we have k nodes, proceed to reverse
            if count == k:
                # Detach the k group and reverse it
                k_group_end = head
                for _ in range(k - 1): # Move to the end of the k group
                    k_group_end = k_group_end.next
                next_group = k_group_end.next
                k_group_end.next = None
                new_group_head = reverse_list(head)
              
                # Connect the reversed group back to the list
                prev_group.next = new_group_head
                head.next = next_group
              
                # Move prev_group and head for the next round of reversal
                prev_group = head
                head = next_group
            else:
                # Not enough nodes to fill a k group, so we are done
                break
      
        # Return the new head of the modified list
        return dummy.next


