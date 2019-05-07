class TwoSum {
    //this Solution is accepted
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> numbers = new HashMap<Integer,Integer>();
        for(int i=0;i<nums.length;i++){
            if(numbers.containsKey(target-nums[i])){
                int otherIndex = numbers.get(target-nums[i]);
                if(nums[i] > (target-nums[i])){
                    return new int[]{otherIndex, i};
                }else{
                    return new int[]{i, otherIndex};
                }
            }
            numbers.put(nums[i],i);
        }
        return new int[]{0,1};
    }
}
