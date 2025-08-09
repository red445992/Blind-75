class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        val = min(val,self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.minStack.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]

s = MinStack()
# Example usage
s.push(5)
s.push(2)
s.push(8)
print(s.top())    # Output: 8
print(s.getMin()) # Output: 2
s.pop()
print(s.getMin()) # Output: 5