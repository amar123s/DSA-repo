class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        n=len(s)
        i=0
        j=n-1
        while i<j:
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
        return " ".join(s)

        