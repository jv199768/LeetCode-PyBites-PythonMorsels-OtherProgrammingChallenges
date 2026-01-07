/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

/**
 * Reverses a singly linked list iteratively
 * @param head - The head node of the linked list to reverse
 * @returns The new head of the reversed linked list
 */
function reverseList(head: ListNode | null): ListNode | null {
    // Handle empty list case
    if (head === null) {
        return head;
    }
  
    // Initialize pointers for reversal
    let previousNode: ListNode | null = null;  // Tracks the previous node in reversed list
    let currentNode: ListNode | null = head;    // Tracks the current node being processed
  
    // Iterate through the list and reverse the links
    while (currentNode !== null) {
        // Store the next node before we change the current node's next pointer
        const nextNode: ListNode | null = currentNode.next;
      
        // Reverse the current node's pointer to point to the previous node
        currentNode.next = previousNode;
      
        // Move pointers forward for next iteration
        previousNode = currentNode;
        currentNode = nextNode;
    }
  
    // Return the new head (which is the last processed node)
    return previousNode;
}
