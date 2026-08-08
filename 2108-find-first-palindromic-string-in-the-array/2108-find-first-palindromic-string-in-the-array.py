class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        n=len(words)
        for i in range(0,n):
            if words[i] == words[i][::-1]:
                return words[i]
        return ""


        