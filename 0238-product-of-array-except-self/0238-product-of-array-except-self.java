class Solution {
    public int[] productExceptSelf(int[] nums) {
       int prev = 1;
       int suf = 1;
       int[] answer = new int[nums.length];
       Arrays.fill(answer,1);
       for(int i=0;i<nums.length;i++){
        if(i!=0){
            prev *= nums[i-1];
            answer[i] *= prev;
        }
        if(i!=nums.length-1)
        {
            suf *= nums[nums.length-i-1];
            answer[nums.length-i-1-1] *= suf;
        }
       }

    return answer;
    }
}