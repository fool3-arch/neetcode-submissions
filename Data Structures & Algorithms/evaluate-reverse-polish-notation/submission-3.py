class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens :
            if i not in "+*-/":
                stack.append(i)
            else:
                if i == '+':
                    x=stack.pop()
                    y=stack.pop()
                    r=int(x)+int(y)   
                elif i=='-':
                    x=stack.pop()
                    y=stack.pop()
                    r=int(y)-int(x)
                elif i=='*':
                    x=stack.pop()
                    y=stack.pop()
                    r=int(x)*int(y)
                else:
                    x=stack.pop()
                    y=stack.pop()
                    r=int(int(y)/int(x))
                stack.append(str(r))
        return int(stack.pop())