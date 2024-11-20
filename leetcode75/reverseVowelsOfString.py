class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        vowles = set('aeiouAEIOU')
        i,j = 0,len(s)-1

        while i<j:
            if s[i] not in vowles:
                i += 1
            elif s[j] not in vowles:
                j -= 1
            else:
                s[i],s[j] = s[j],s[i]
                i += 1
                j -= 1
        return "".join(s)
a = Solution()
print(a.reverseVowels('IceCreAm'))