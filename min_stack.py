
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        #self.min_stack = []
        self.min_val = 1000
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        
        if(len(self.min_stack) == 0 or x <= self.min_stack[-1]):
            self.min_stack.append(x)
        self.stack.append(x)
        """
        if(x <= self.min_val):
            self.stack.append(self.min_val)
            self.min_val = x
        self.stack.append(x)
        print(self.stack)

            
        

    def pop(self):
        """
        :rtype: None
        
        if(self.stack[-1]  == self.min_stack[-1]):
            self.min_stack.pop()    
        self.stack.pop()
        """
        print("pop : " , self.stack)
        if(self.stack.pop() == self.min_val):
            self.min_value = self.stack.pop()
            print("pop : " , self.stack)
        print("final pop : " , self.stack)

        
        
    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_val
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


if __name__ == "__main__":
    obj = MinStack()
    obj.push(-2)
    obj.push(0) 
    obj.push(-3)
    #obj.push(50)
    print(obj.getMin())
    obj.pop()
    print(obj.getMin())
    #obj.pop()
    print(obj)
    #param_3 = obj.top()