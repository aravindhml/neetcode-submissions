class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}

        for index, value in enumerate(nums):
            if target - value in m:
                return [m.get(target - value), index]
            m[value] = index
        return None
