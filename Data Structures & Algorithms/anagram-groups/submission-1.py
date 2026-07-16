class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = []
        for i in range(len(strs)):
            out.append("".join(sorted(strs[i])))
        

        m = {}

        for i in range(len(out)):
            if out[i] in m:
                m[out[i]].append(strs[i])
            else:
                m[out[i]] = [strs[i]]

        return list(m.values())
        