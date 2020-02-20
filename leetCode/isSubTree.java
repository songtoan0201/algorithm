
boolean isSubtree(Tree<Integer> t1, Tree<Integer> t2) {
    return traverse(t1, t2);
}

boolean isEqual(Tree<Integer> t1, Tree<Integer> t2) {
    if (t1 == null && t2 == null) return true;
    if (t1 == null || t2 == null) return false;
    return t1.value.equals(t2.value)
        && isEqual(t1.left, t2.left)
        && isEqual(t1.right, t2.right);
}

boolean traverse(Tree<Integer> t1, Tree<Integer> t2) {
    if (t1 == null && t2 != null) return false;
    if (t2 == null) return true;
    if (t1 == null && t2 == null) return true;
    return isEqual(t1, t2) || traverse(t1.left, t2) || traverse(t1.right, t2);
}