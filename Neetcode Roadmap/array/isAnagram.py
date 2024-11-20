class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frq_s = {}
        frq_t = {}

        if len(s) != len(t):
            return False
        
        char_count= {}

        for x in s:
            char_count[x] = char_count.get(x,0)+1
        for x in t:
            if x not in char_count or char_count[x] == 0:
                return False
            char_count[x]-=1
        
        return all(count == 0 for count in char_count.values())


a = Solution()
print(a.isAnagram("racecar","carrace"))