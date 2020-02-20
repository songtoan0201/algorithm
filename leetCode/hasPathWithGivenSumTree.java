boolean hasPathWithGivenSum(Tree<Integer> t, int s) {
    //If just one of left or right was null, then it was not a child node and false can be returned safely
    if(t == null) return false;
    System.out.println(t.value);
    //If this is a child AND sum is input, then we have a path
    if(t.left == null && t.right == null) {
        return (s == t.value);
    }
    
    return hasPathWithGivenSum(t.left, s-t.value) || hasPathWithGivenSum(t.right, s-t.value);
}  
