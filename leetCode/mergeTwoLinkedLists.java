ListNode<Integer> mergeTwoLinkedLists(ListNode<Integer> l1, ListNode<Integer> l2) {
    ListNode<Integer> tempNode = new ListNode<Integer>(0);
    ListNode runner = tempNode;
    while(l1 != null && l2 != null) {
        if(l1.value <= l2.value) {
            runner.next = l1;
            l1 = l1.next;
        } else {
            runner.next = l2;
            l2 = l2.next;
        } 
        runner = runner.next;
    }
    if(l1 != null) {
        runner.next = l1;
    }
    if(l2 != null) {
        runner.next = l2;
    }

    return tempNode.next;
}
