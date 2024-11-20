class Solution():
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        res = []
        max_candies = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candies:
                res.append(True)
            else:
                res.append(False)

        return res
a = Solution()
candies = [2,3,5,1,3]
extraCandies = 3
print(a.kidsWithCandies(candies,extraCandies))