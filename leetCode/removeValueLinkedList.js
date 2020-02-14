function removeKFromList(l, k) {
  if (l == null) return null;
  let sentinel = new ListNode(0);
  sentinel.next = l;
  let cur = l;
  let prev = sentinel;
  while (cur != null) {
    if (cur.value == k) {
      prev.next = cur.next;
    } else {
      prev = cur;
    }
    cur = cur.next;
  }
  return sentinel.next;
}
