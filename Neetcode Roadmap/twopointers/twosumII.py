def solution(numbers,target):
    left, right = 0, len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        if current_sum == target:
            return [left + 1, right + 1]  # Return 1-based indices
        elif current_sum < target:
            left += 1
        else:
            right -= 1
            
    return []  # If no solution found

print(solution([2, 7, 11, 15], 9))  # Output: [1, 2]