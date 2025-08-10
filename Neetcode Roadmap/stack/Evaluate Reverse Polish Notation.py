class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if token in ("+", "-", "*", "/"):
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    # Truncate toward zero
                     stack.append(int(float(a)/b))
            else:
                stack.append(int(token))
        return stack[0]

c = Solution()
print(c.evalRPN(["2", "1", "+", "3", "*"])  )  # Example usage
