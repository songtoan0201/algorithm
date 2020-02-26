int[] nextLarger(int[] a) {
    int [] result = new int[a.length];
    
    Stack<Integer> index = new Stack();
    for(int i = 0; i < a.length; i++){
        while(!index.isEmpty() && a[index.peek()] < a[i]){
            int ind = index.pop();
            result[ind] = a[i];
        }
        index.push(i);
    }
    
    while(!index.isEmpty()){
        result[index.pop()] = -1;
    }
    
    return result;
}

// reverse order

int[] nextLarger(int[] a) {
    int n = a.length;
    int[] result = new int[n];
    
    Stack<Integer> stack = new Stack<>();
    for (int i = n-1; i>= 0; i--) {
       while (!stack.isEmpty() && a[i] >= stack.peek()) {
          stack.pop();
       }
       result[i] = stack.isEmpty() ? -1 : stack.peek();
       stack.push(a[i]);
    }   
    return result;
 }