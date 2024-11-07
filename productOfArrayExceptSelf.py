class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answer= [1] * n
        left_product,right_product = 1,1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]
        for i in range(n-1,-1,-1):
            answer[i] *= right_product
            right_product *= nums[i]
        return answer  

a = Solution()
print(a.productExceptSelf([1,2,3,4]))