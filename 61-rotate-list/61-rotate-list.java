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
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || head.next == null){
            return head;
        }
        ListNode cur = head;
        int listLen = 1;
        while (cur.next != null){
            cur = cur.next;
            listLen ++;
        }
        
        int rotation = k % listLen;
        if (rotation == 0){
            return head;
        }
        
        // we made a circle
        cur.next = head;
        int roation = k;
        if (k>listLen){
            rotation = k % listLen;
        }
        
        int nodeIdx = listLen - rotation;
        
        cur = head;
        ListNode newHead = head;
        while (nodeIdx != 1){
            nodeIdx --;
            cur = cur.next;
        }
        
        newHead = cur.next;
        cur.next = null;
        return newHead;
        
        
        
    }
}