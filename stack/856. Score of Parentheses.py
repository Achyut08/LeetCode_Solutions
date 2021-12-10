class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        sum1=0
        stack=[0]
        for i in s:
            if i=='(':
                stack.append(-1)
            else:
                if stack[-1] == -1:
                    stack.pop()
                    stack.append(1)
                else:
                    sum2=0
                    while stack[-1] != -1:
                        sum2 += stack.pop()
                    stack.pop()
                    stack.append(2*sum2)
        while stack:
            sum1 += stack.pop()
        return sum1
                    
                    
                
                    
                
