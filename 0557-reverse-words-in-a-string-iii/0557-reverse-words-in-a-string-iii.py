class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        n=len(s)
        i=0
        j=n-1
        while i <n:
            words= list(s[i])
            j=(len(words))-1
            left=0
            while left <j:
                words[left],words[j]=words[j],words[left]
                left+=1
                j-=1
            s[i]="".join(words)
            i+=1

        return " ".join(s)

        