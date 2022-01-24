/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode cur = head;
        ListNode prev = null;
        return recursiveHelper(cur,prev);
        
    }
    public ListNode recursiveHelper(ListNode cur, ListNode prev){
        if (cur == null){
            return prev;
        }
        ListNode next = cur.next;
        cur.next = prev;
        prev = cur;
        return recursiveHelper(next, prev);
        
    }
}