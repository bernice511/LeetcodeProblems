class Solution {
    public boolean containsDuplicate(int[] nums) {
     HashMap<Integer, Integer> duplicates = new HashMap();

     for(int num: nums){
        if(duplicates.containsKey(num)){
            return true;
        }
        else{
            duplicates.put(num, 1);
        }
     }
     return false; 
    }
}