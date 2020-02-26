int[] minimumOnStack(String[] operations) {
    Stack<Integer> stack = new Stack<Integer>();
    List<Integer> result = new ArrayList<Integer>();
    for(String op : operations) {
        if(op.contains("push")) {
            int cur_num = Integer.parseInt(op.split(" ")[1]);
            if(!stack.isEmpty() && cur_num < stack.peek()) {
                stack.push(cur_num);
            } else if (!stack.isEmpty() && cur_num > stack.peek()) {
                stack.push(stack.peek());
            }
            else {
                stack.push(cur_num);
            }
            System.out.println("s:" + stack);
        }
        if(op.contains("pop")) {
            stack.pop();
        }
        if(op.contains("min")) {
            result.add(stack.peek());
        }
    }

    int[] ans = new int[result.size()];
    for (int i = 0; i < result.size(); i++) {
        ans[i] = result.get(i);
    }
    return ans;
}

// Convert list to int[]
// int [] ints = list.stream().mapToInt(Integer::intValue).toArray();