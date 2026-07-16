class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count = 0
        m = nums[0]

        for i in nums:
            if count ==0:
                m = i
            
            if m == i:
                count+=1
            else:
                count-=1
        
        return m
        