class Solution {
    public int[] twoSum(int[] nums, int target) {
        int testSum=0;
        int[] newArr= new int[2];
        for(int x=0;x<nums.length-1;x++){
            for(int y=x+1;y<nums.length;y++){
                testSum=nums[x]+nums[y];
                if(testSum == target){
                    newArr[0]=x;
                    newArr[1]=y;
                }else{
                    testSum=0;
                }
            }
        }
        return newArr;
    }
}