def isPalindrome(s: str) -> bool:
        s_new =  "".join(c.lower() for c in s if c.isalnum())
        length = len(s_new)
        left, right = 0, length - 1
        while left < right:
            if s_new[left] != s_new[right]:
                return False
            left += 1
            right -= 1
        return True
s = "was it a car or a cat I saw"
print(isPalindrome(s))