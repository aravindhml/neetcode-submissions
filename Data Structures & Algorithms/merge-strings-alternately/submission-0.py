class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l,r = 0,0
        out = ['0'] * (len(word1)+len(word2))
        k=0

        while l<len(word1) and r<len(word2):
            out[k] = word1[l]
            l+=1
            k+=1
            out[k] = word2[r]
            r+=1
            k+=1
        
        while l<len(word1):
            out[k] = word1[l]
            l+=1
            k+=1
        
        while r<len(word2):
            out[k] = word2[r]
            r+=1
            k+=1


        
        return "".join(out)

        