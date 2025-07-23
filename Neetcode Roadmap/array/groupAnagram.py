from collections import defaultdict

def groupAnagram(strs):
    res = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
        res[tuple(count)].append(s)
    return list(res.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagram(strs))