function isListPalindrome(l) {
  if (l == null) return true;
  let firstHalfEnd;
  let slow = l;
  let fast = l;
  while (fast.next != null && fast.next.next != null) {
    fast = fast.next.next;
    slow = slow.next;
  }
  firstHalfEnd = slow;
  let secondHalfStart = reverseList(firstHalfEnd.next);

  //Check palindrome
  let l2 = secondHalfStart;
  while (l2 != null) {
    if (l.value != l2.value) return false;
    l = l.next;
    l2 = l2.next;
  }
  firstHalfEnd.next = reverseList(secondHalfStart);
  return true;
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
