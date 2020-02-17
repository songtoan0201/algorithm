int possibleSums(int[] coins, int[] quantity) {
    HashSet<Integer> seen = new HashSet<Integer>();
    seen.add(0);
    for(int i = 0; i < coins.length; i++) {
        // sum = coins[i];
        HashSet<Integer> cur_sum = new HashSet<Integer>();     
        for(Integer seenValue : seen) {
            for(int j = 1; j <= quantity[i]; j++) {
                cur_sum.add(seenValue + coins[i]*j);
            }
        }
        seen.addAll(cur_sum);
    }
    return seen.size()-1;
}
