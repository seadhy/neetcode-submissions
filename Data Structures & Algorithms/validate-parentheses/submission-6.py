class Solution:
    def __init__(self):
        self.opening_parentheses = ['(', '{', '[']
        self.closing_parentheses = [')', '}', ']']

        self.parantheses_set = {')': '(', '}': '{', ']': '['}

    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in self.opening_parentheses:
                stack.append(ch)

            elif ch in self.closing_parentheses:
                if self.parantheses_set[ch] in stack and self.parantheses_set[ch] == stack[-1]:
                    stack.remove(self.parantheses_set[ch])
                else:
                    return False
                
        return True if stack == [] else False