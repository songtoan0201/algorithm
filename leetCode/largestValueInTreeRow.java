int[] largestValuesInTreeRows(Tree<Integer> t) {
    if(t == null) return new int[0];
    Queue<Tree<Integer>> queue = new LinkedList<Tree<Integer>>();
    List<Integer> result = new ArrayList<Integer>();

    queue.add(t);
    
    //while(1){};
    while(!queue.isEmpty()) {  
        Integer max = Integer.MIN_VALUE; 
        int size = queue.size();
        for (int i = 0; i < size; i++) {
            Tree<Integer> cur = queue.poll();
            if (cur.value > max.intValue()) {
                max = cur.value;  
            }
            if(cur.left != null) {
                queue.add(cur.left);
            } 
            if(cur.right != null) {
                queue.add(cur.right);
            }        
        }
        result.add(max);
    }
    

    return result.stream().mapToInt(Integer::intValue).toArray();
}
