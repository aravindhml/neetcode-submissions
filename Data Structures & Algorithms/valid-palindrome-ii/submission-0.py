class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r = 0,len(s)-1

        while l<=r:
            if s[l] !=s[r]:
                return self.isValidPalindrome(l+1,r,s) or self.isValidPalindrome(l,r-1,s)
            
            l+=1
            r-=1

        return True
    


    def isValidPalindrome(self,l, r, s):

        while l<=r:
            if s[l]!=s[r]:
                return False
            
            l=l+1
            r=r-1
        
        return True


        