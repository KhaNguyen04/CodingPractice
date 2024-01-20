class Solution:
    def simplifyPath(self, path: str) -> str:
        # /
        res=[]
        i=0
        while i<len(path):
            if path[i]==".":
                start=i
                isName=False
                while i<len(path) and path[i]!="/":
                    if path[i]!=".":
                        isName=True
                    i+=1
                if not isName and i-start<3:
                    if i-start==1:
                        res.pop()
                    elif i-start==2:
                        res.pop()
                        if res: res.pop()
                        if res: res.pop()
                else:
                    res.append(path[start:i])
            elif path[i]=="/":
                while i<len(path) and path[i]=="/":
                    i+=1
                res.append("/")
            else:
                start=i
                while i<len(path) and path[i]!="/":
                    i+=1
                res.append(path[start:i])
        if res and res[-1]=="/": res.pop()
        return "".join(res) if res else "/"