boolean isTreeSymmetric(Tree<Integer> root) {
    if(root == null) return true; 
    return isEqual(root.left, root.right);
}
boolean isEqual(Tree<Integer> t1, Tree<Integer> t2) {
    if (t1 == null && t2 == null) return true;
    if (t1 == null || t2 == null) return false;
    return t1.value.equals(t2.value)
        && isEqual(t1.right, t2.left)
        && isEqual(t1.left, t2.right);
}
