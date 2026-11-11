class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #a, b, next, is operate, then 
        stack=[]
        for i in range(len(tokens)):
            if tokens[i] not in "+-*/":
                stack.append(int(tokens[i]))
            else:
                num1=stack.pop()
                num2=stack.pop()
                if tokens[i]=="+":
                    new_val=num1+num2
                elif tokens[i]=="-":
                    new_val=num2-num1
                elif tokens[i]=="*":
                    new_val=num1*num2
                elif tokens[i]=="/":
                    if num2/num1<0 and num2%num1!=0:
                        new_val=num2//num1+1
                    else:
                        new_val=num2//num1

                stack.append(new_val)
            print(stack)
        return stack[0]

