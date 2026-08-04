class Solution {
    /**
     * @param {string[]} strs
     * @return {string}
     */
    longestCommonPrefix(strs) {
        let prefix = strs[0];
            
        for(let str of strs){
            while(!str.startsWith(prefix)){
                prefix = prefix.substring(0,prefix.length-1);
                if(prefix.length==0){
                    return prefix;
                }
                continue;
            }
        }
        return prefix;
    }
}
