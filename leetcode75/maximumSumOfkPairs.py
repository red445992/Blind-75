class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        l,r = 0,len(nums)-1
        ans = 0
        while(l<r):
            if nums[l]+nums[r] < k:
                l+=1
            elif nums[l]+nums[r]>k:
                r-=1
            else:
                l+=1
                r-=1
                ans+=1
        return ans
a = Solution()
print(a.maxOperations([1,2,3,4],5))