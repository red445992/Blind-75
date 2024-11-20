class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sum = 0.00
        for i in range(k):
            sum += nums[i]
        avg = sum/k
        max_avg = avg

        l,r = 0,k
        while r < len(nums):
            sum -= nums[l]
            l+=1

            sum += nums[r]
            r+=1

            avg = float(sum/k)
            max_avg = max(max_avg,avg)
        
        return max_avg

a = Solution()
print(a.findMaxAverage([1,12,-5,-6,50,3],4))