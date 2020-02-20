Tree<Integer> restoreBinaryTree(int[] inorder, int[] preorder) {
    int n = preorder.length;
    return dfs(preorder, 0, n, inorder, 0, n);
}
Tree<Integer> dfs(int[] preorder, int sp, int ep, int[] inorder, int si, int ei) {
    if( sp >= ep)
        return null;

    Tree<Integer> root = new Tree<Integer>(preorder[sp]);
    for(int i=si; i<ei; i++) {
        if( inorder[i] == preorder[sp]) {
            root.left = dfs(preorder, sp+1, sp+(i-si)+1, inorder, si, i);
            root.right = dfs(preorder, sp+(i-si)+1, ep, inorder, i+1, ei);
        }
    }
    return root;
}

inorder: [4, 2, 1, 5, 3, 6];
preorder: [1, 2, 4, 3, 5, 6];

//Python
def restoreBinaryTree(inorder, preorder):
    if len(inorder) == 0:
        return None
    tree = Tree(preorder.pop(0))
    pivot = inorder.index(tree.value) // 2
    tree.left = restoreBinaryTree(inorder[:pivot], preorder)
    tree.right = restoreBinaryTree(inorder[pivot + 1:], preorder)
    return tree