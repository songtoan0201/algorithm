int[] nearesulttGreater(int[] a) {
    int[] res = new int[a.length];
    Stack<Integer> st = new Stack<Integer>();
    for( int i=0 ; i< a.length ; i++){
        System.out.println(i);
        while(!st.isEmpty() && a[st.peek()]<=a[i]){
            st.pop();
        }
        res[i] = st.isEmpty() ? -1 : st.peek();
        st.push(i);
    }
    for( int i = a.length-1 ; i>=0 ; i--){
         System.out.println(i);
        while(!st.isEmpty() && a[st.peek()]<=a[i]){
            st.pop();
        }
        if( res[i] == -1 || (i-res[i])>(st.peek()-i) )
            res[i]=st.isEmpty()?-1:st.peek();
        st.push(i);
    }
    return res;
}
