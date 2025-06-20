class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        write = 0
        i = 0

        while i<len(chars):
            char = chars[i]
            count =0
            
            while i<len(chars) and chars[i]==char:
                count+=1
                i+=1

            chars[write] = char
            write +=1

            if count>1:
                for digit in str(count):
                    chars[write] = digit
                    write +=1
                
        return write
a = Solution()
print(a.compress(['a','a','b','b','b','c','c']))