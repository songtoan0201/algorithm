function addTwoHugeNumbers(a, b) {
  if (a.value == 0) return b;
  else if (b.value == 0) return a;
  else if (a.value == 0 && b == 0) return 0;
  let a_reverse = reverseList(a);
  let b_reverse = reverseList(b);
  let run_a = a_reverse;
  let run_b = b_reverse;
  let prev_result = new ListNode(0);
  let prev = prev_result;
  let remainder = 0;
  while (run_a != null || run_b != null || remainder != 0) {
    let tempSum = 0;
    if (run_a != null) {
      tempSum += run_a.value;
      run_a = run_a.next;
    }
    if (run_b != null) {
      tempSum += run_b.value;
      run_b = run_b.next;
    }
    tempSum += remainder;
    remainder = 0;
    if (tempSum > 9999) {
      remainder = 1;
      tempSum -= 10000;
      prev.next = new ListNode(tempSum);
      prev = prev.next;
    } else {
      prev.next = new ListNode(tempSum);
      prev = prev.next;
    }
  }
  let result_reverse = reverseList(prev_result.next);
  return result_reverse;
}

function reverseList(head) {
  let prev = null;
  let cur = head;
  while (cur != null) {
    let temp = cur.next;
    cur.next = prev;
    prev = cur;
    cur = temp;
  }
  return prev;
}
