def productExcpetSelf(nums):
    n = len(nums)
    answer = [1] * n
    l,r=1,1
    for i in range(n):
        answer[i] *= l
        l *= nums[i]
    for i in range(n - 1, -1, -1):
        answer[i] *= r
        r *= nums[i]
    return answer

nums = [1, 2, 3, 4]
result = productExcpetSelf(nums)
print(f"Input: {nums}")
print(f"Output: {result} (represents {result[0]} * {result[1]} * {result[2]} * {result[3]})")