class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        str3=[]
        while i <len(word1) and i < len(word2):
            str3.append(word1[i])
            str3.append(word2[i])
            i+=1   
        
        str3.extend(word1[i:])
        str3.extend(word2[i:])
        
        return "".join(str3)



       
        