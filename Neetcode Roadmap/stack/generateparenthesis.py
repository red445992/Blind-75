def generateparenthesis(n):
    stack = []
    res = []

    def backtrack(open_count, close_count):
        if open_count == n and close_count == n:
            res.append("".join(stack))
            return
        if open_count < n:
            stack.append("(")
            backtrack(open_count + 1, close_count)
            stack.pop()
        if close_count < open_count:
            stack.append(")")
            backtrack(open_count, close_count + 1)
            stack.pop()

    backtrack(0, 0)
    return res

print(generateparenthesis(3))  # Example usage