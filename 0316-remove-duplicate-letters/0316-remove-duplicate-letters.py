class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        seen=set()
        ans=[]
        last={}
        for i in range(len(s)):
            last[s[i]]=i
        for i in range(len(s)):
            ch=s[i]
            if ch in seen:
                continue
            while ans and ans[-1]> ch and last[ans[-1]]>i:
                removed=ans.pop()
                seen.remove(removed)
            ans.append(ch)
            seen.add(ch)
        return "".join(ans)
        