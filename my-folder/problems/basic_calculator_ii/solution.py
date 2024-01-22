class Solution:
    def calculate(self, s: str) -> int:
        exp=[]
        i=0
        while i<len(s):
            if s[i]==" ":
                i+=1
                continue
            if s[i].isdigit():
                start=i
                while i<len(s) and s[i].isdigit():
                    i+=1
                exp.append(int(s[start:i]))
            else:
                exp.append(s[i])
                i+=1
        stack=[]
        stack.append(exp[0])
        for i in range(1,len(exp),2):
            if exp[i]=="*":
                stack[-1]=stack[-1]*exp[i+1]                
            elif exp[i]=="/":
                stack[-1]=stack[-1]//exp[i+1]                
            else:
                stack.append(exp[i])
                stack.append(exp[i+1])
        print(stack)
        res=stack[0]
        for i in range(1,len(stack),2):
            if stack[i]=="+":
                res+=stack[i+1]             
            elif stack[i]=="-":
                res-=stack[i+1]               
        return res

