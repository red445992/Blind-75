def validparenthesis(s):
    stack = []
    CloseToOpen = {')':'(', '}':'{', ']':'['}

    for i in s:
        if i in CloseToOpen:
            if stack and stack[-1] == CloseToOpen[i]:
                stack.pop()
            else:
                return False
        else:
            stack.append(i)

    return not stack

print(validparenthesis("()"))  # Output: True
print(validparenthesis("()[]{}"))  # Output: True
print(validparenthesis("(]"))  # Output: False
print(validparenthesis("([)]"))  # Output: False
print(validparenthesis("{[]}"))  # Output: True