/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    /* Since we don't have access to the parent node we'll just copy values of all nodes one node beofre them, that way we'll essentially delete our current node*/
    public void deleteNode(ListNode node) {
        ListNode cur = node;
        ListNode prev = null;
        
        while (cur.next != null) {
            cur.val = cur.next.val;
            prev = cur;
            cur = cur.next;
        }
        prev.next = null;
        
    }
}