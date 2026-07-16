class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = strs[0]

        for str in strs:
            while not str.startswith(s):
                s = s[:-1]
        
        return s
        