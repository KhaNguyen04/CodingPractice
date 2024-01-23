class Solution:
    def calculate(self, s: str) -> int:
        cur=0
        stack=[]
        sign=1
        i=0
        while i<len(s):
            if s[i].isdigit():
                start=i
                while i<len(s) and s[i].isdigit():
                    i+=1
                cur+=(int(s[start:i])*sign)
            elif s[i]=="+":
                sign=1
                i+=1
            elif s[i]=="-":
                sign=-1
                i+=1
            elif s[i]=="(":
                stack.append(cur)
                stack.append(sign)
                cur=0
                sign=1
                i+=1
            elif s[i]==")":
                sign=stack.pop()
                cur=sign*cur+stack.pop()
                i+=1
            else:
                i+=1
        return cur
                