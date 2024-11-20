class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.strip().split()
        reverse_words = words[::-1]
        return " ".join(reverse_words)
a = Solution()
print(a.reverseWords("the sky is blue"))