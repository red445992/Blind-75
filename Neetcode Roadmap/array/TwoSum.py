def two_Sum(num,target):
    dict = {}
    for i,n in enumerate(num):
        diff = target - n
        if diff in dict:
            return [dict[diff],i]
        dict[n] = i

a = [2,7,11,15]
target = 9
print(two_Sum(a,target))