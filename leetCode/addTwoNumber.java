import java.util.LinkedList;

class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
    }

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode run1 = l1;
        ListNode run2 = l2;
        ListNode result = null;
        int remainder = 0;
        ListNode runner = null;
        while (run1 != null || run2 != null || remainder != 0) {
            int tempSum = 0;
            if (run1 != null) {
                tempSum += run1.val;
                run1 = run1.next;
            }
            if (run2 != null) {
                tempSum += run2.val;
                run2 = run2.next;
            }
            tempSum += remainder;
            remainder = 0;
            if (tempSum >= 10) {
                tempSum = tempSum % 10;
                remainder = 1;
            }
            if (result == null) {
                result = new ListNode(tempSum);
                runner = result;
            } else {
                runner.next = new ListNode(tempSum);
                runner = runner.next;
            }

        }
        return result;
    }
}
