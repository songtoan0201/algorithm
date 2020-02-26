int[] traverseTree(Tree<Integer> t) {
    if(t == null) return new int[] {};
    Queue<Tree<Integer>> queue = new LinkedList<Tree<Integer>>();
    List<Integer> result = new ArrayList<Integer>();

    queue.add(t);
    while(!queue.isEmpty()) {  
        Tree<Integer> cur = queue.poll();     
        result.add(cur.value);
        System.out.print(queue.peek());
        if(cur.left != null) {
            queue.add(cur.left);
        }
        if(cur.right != null) {
            queue.add(cur.right);
        }
    }

    return result.stream().mapToInt(Integer::intValue).toArray();
}