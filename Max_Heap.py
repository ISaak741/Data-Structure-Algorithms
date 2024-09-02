class Max_Heap:
    def __init__(self,arr=None):
        self.arr = arr if arr != None else [] 
        self.size = len(self.arr)
        if self.size != 0:
            self.construct()
        
    def construct(self):
        for i in range(1,self.size):
            self.adjust(i)
    
    def adjust(self,i):
        j = i
        while j != 0 and self.arr[j] > self.arr[(j-1) // 2]:
            self.arr[j] , self.arr[(j-1) // 2]  = self.arr[(j-1) // 2] , self.arr[j]
            j = (j-1) // 2
    
    def add(self,val):
        self.arr.append(val)
        self.size = len(self.arr)
        self.adjust(self.size-1)
    
    def delete(self):
        val = self.arr[0]
        if self.size == 1:
            self.arr = []
            self.size = 0
            return val

        self.arr[0] = self.arr.pop()
        self.size = len(self.arr)
        i = 0
        self.heapify(i)
        return val
    
    def heapify(self,i):
        while True:
            l = 2 * i + 1
            r = 2 * i + 2
            largest = i
            if l < self.size and self.arr[largest] < self.arr[l]:
                largest = l
            if r < self.size and self.arr[largest] < self.arr[r]:
                largest = r
            if largest != i:
                self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
                i = largest
            else:
                return
            
    def is_empty(self):
        return self.size == 0
    
    def length(self):
        return self.size
    
    def peek(self):
        return self.arr[0] if not self.is_empty() else None
    
    def __str__(self):
        return str(self.arr)



print(Max_Heap([-5, -10, 15, 0, -1, 3, -8]))

heap = Max_Heap()
heap.add(-5)
heap.add(-10)
heap.add(15)
heap.add(0)
heap.add(-1)
heap.add(3)
heap.add(-8)
print(heap)




