/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    if(n==0) return head;
    let dummy = head;
    let len = 0;
    while (dummy.next!=null) {
        len++;
        dummy = dummy.next;
    }
    let nth = len-n+1;
    let prev = null;
    dummy = head;
    while(nth-- !=0) {
        prev = dummy;
        dummy = dummy.next;
    }
    if (prev != null) {
        prev.next = dummy.next;
        dummy.next = null;
    }
    else {
        return head.next;
    }
    return head;

};
