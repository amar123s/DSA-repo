class Solution:
    def partition(self, s: str) -> list[list[str]]:
        def is_pali(sub):
            return sub ==sub[::-1]
        ls=len(s)
        res=[]
        def baku(start,path,res):
            if start==ls:
                res.append(path[:])
                return
            for end in range(start+1,ls+1):
                if is_pali(s[start:end]):
                    path.append(s[start:end])
                    baku(end,path,res)
                    path.pop()
        baku(0,[],res)
        return res

        