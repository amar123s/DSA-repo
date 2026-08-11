class Solution:
    def toLowerCase(self, s: str) -> str:
        ans=""
        for ch in s:
            if ord(ch)>=65 and ord(ch) <=90:
                ans += chr(ord(ch)+32)

            else:
                ans+=ch
        return ans
        