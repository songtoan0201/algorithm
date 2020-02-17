boolean containsCloseNums(int[] nums, int k) {
    HashMap seen = new HashMap();
    for(int i = 0; i < nums.length; i++) {
        if(!seen.containsKey(nums[i])) {
            seen.put(nums[i], i);
        } else {
            int index = (int) seen.get(nums[i]);
            if (i - index <= k) 
                return true;
            seen.put(nums[i], i);
        }
    }
    return false;
}
