class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    majorityElement(nums) {
        let m = nums[0];
        let count = 1;

        for(let i =1;i<nums.length;i++){
            if(nums[i]==m){
                count++;
            }
            else{
                count--;
            }
            if (count==0){
                m = nums[i];
                count=1
            }

        }
        return m;

    }
}
