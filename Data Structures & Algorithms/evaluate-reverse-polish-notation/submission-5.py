class Solution:
    def __init__(self):
        self.operations = ['+', '-', '*', '/']

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in self.operations:
                val2, val1 = stack.pop(), stack.pop()
                res = 0
                match t:
                    case '+':
                        res = val1 + val2
                    case '-':
                        res = val1 - val2
                    case '*':
                        res = val1 * val2
                    case '/':
                        res = val1 / val2
                        
                stack.append(int(res))
            else:
                stack.append(int(t))

        return stack[0]