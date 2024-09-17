class Stack:
    def __init__(self):
        self.arr = []
        self.length = 0
    
    def push(self,item):
        self.arr.append(item)
        self.length += 1
        
    def pop(self):
        if not self.is_empty():
            self.length -= 1
            return self.arr.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.arr[self.length-1]
        return None
    
    def is_empty(self):
        return self.length == 0
    
    def size(self):
        return self.length
    
    def __str__(self):
        return self.arr.__str__()