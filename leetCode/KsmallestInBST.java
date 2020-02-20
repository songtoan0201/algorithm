private static int number = 0;
private static int count = 0;
int kthSmallestInBST(Tree<Integer> t, int k) {
    count = k;
    treeTraversal(t);
    return number;
}

void treeTraversal(Tree<Integer> t) {    
    if(t.left != null) treeTraversal(t.left);
    count--;
    if (count == 0) {
        number = t.value;
        return;
    }
    if(t.right != null) treeTraversal(t.right);
}