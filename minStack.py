class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.min=[]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.stack)==0:
            self.stack.append(x)
            self.min.append(x)
        elif x<=self.min[len(self.min)-1]:
            self.min.append(x)
            self.stack.append(x)
        elif x>self.min[len(self.min)-1]:
            self.stack.append(x)



    def pop(self):
        """
        :rtype: None
        """
        if len(self.stack)==0:
            return None
        else:
            item =self.stack.pop()
            if self.min[len(self.min)-1]==item:
                self.min.pop()


    def top(self):
        """
        :rtype: int
        """
        if len(self.stack)==0:
            return None
        else:
            return self.stack[len(self.stack)-1]

    def getMin(self):
        """
        :rtype: int
        """

        if len(self.stack)==0:
            return None
        else:
            return self.min[len(self.min)-1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-1)
print(obj.getMin())