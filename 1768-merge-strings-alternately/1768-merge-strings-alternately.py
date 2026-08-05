class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n=list(word1)
        m=list(word2)
        str3=[]
        for i in range(min(len(n),len(m))):
            str3.append(n[i])
            str3.append(m[i])
        
        str3.extend(n[min(len(n),len(m)):])
        str3.extend(m[min(len(n),len(m)):])
        
        return "".join(str3)



       
        