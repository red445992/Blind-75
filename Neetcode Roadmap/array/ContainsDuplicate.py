class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        visited = set()  # Use a set for efficient lookups
        for x in nums:
            if x in visited:  # If the element is already seen
                return True
            visited.add(x)  # Otherwise, add it to the visited set
        return False  # If no duplicates are found, return False
a = Solution()
print(a.hasDuplicate([1, 2, 3, 3]))