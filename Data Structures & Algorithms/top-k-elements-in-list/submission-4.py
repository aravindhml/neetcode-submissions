class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        m = {}

        for i in nums:
            m[i] = m.get(i,0) + 1
        
        
        sorted_dict = sorted(m.items(), key = lambda item: item[1], reverse = True)

        a=[]

        for i,j in sorted_dict:
            a.append(i)

            if len(a) >=k:
                break
        return a
            

        