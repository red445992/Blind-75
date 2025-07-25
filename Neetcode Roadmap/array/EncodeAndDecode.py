def encode(strs):
    return ''.join(f'{len(s)}#{s}' for s in strs)

def decode(s):
    decoded = []
    i = 0
    while i < len(s):
        j = s.index('#', i)
        length = int(s[i:j])
        decoded.append(s[j+1:j+1+length])
        i = j + 1 + length
    return decoded

print(encode(["hello", "world"]))  # Output: "5#hello5#world"
print(decode("5#hello5#world"))  # Output: ["hello", "