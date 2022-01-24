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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode newHead = new ListNode(0);
        ListNode start = newHead;
        int result = 0;
        while (l1 != null || l2 != null){
            result /= 10;
            if (l1 != null){
                result += l1.val;
                l1 = l1.next;
            }
            if (l2 != null){
                result += l2.val;
                l2 = l2.next;
            }
            newHead.next = new ListNode(result%10);
            newHead = newHead.next;
            
        }
        System.out.println(result);
        if (result/10 == 1){
            newHead.next = new ListNode(1);
            newHead = newHead.next;
        }
        return start.next;
    }
}