class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            '+' : lambda a,b: a+b,
            '-' : lambda a,b: a-b,
            '/' : lambda a,b: int(a/b),
            '*' : lambda a,b: a*b
        }
        stack = []
        for i in tokens:
            if i in operators:
                n = stack.pop()
                m = stack.pop()
                stack.append(operators[i](m,n))
            else:
                stack.append(int(i))
        return stack.pop()
