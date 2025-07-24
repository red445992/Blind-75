from collections import Counter 

def top_k_frequent(nums,k):
    d = Counter(nums)  # Count the frequency of each element
    
    s = sorted(d.items(),reverse=True) 

    r = [i[0] for i in s[:k]]

    return r

print(top_k_frequent([1,2,2,3,3,3],2)  )# Example usage