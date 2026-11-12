class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix=strs[0]
        for i in range(len(prefix)):
            for words in strs:
                if i == len(words) or words[i]!=prefix[i]:
                    return prefix[:i]
        
        return prefix