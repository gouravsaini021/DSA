class MinHeap:
    def __init__(self,data=[]):
        self.heap=[]
        for i in data:
            self.insert(i)
    
    def insert(self,val):
        self.heap.append(val)
        self._heapify_up()
    
    def remove(self):
        popped_value=self.heap[0]
        self.heap[0]=self.heap[-1]
        self.heap=self.heap[0:-1]
        self._heapify_down()
        return popped_value
    
    def _heapify_down(self):
        idx=1
        l=2*idx
        r=2*idx+1
        
        while l<len(self.heap) and r<len(self.heap):
            if l<len(self.heap) and self.heap[idx-1]>self.heap[l-1]:
                self.heap[idx-1],self.heap[l-1]=self.heap[l-1],self.heap[idx-1]
                idx=l
            elif r<len(self.heap) and self.heap[idx-1]>self.heap[r-1]:
                self.heap[idx-1],self.heap[r-1]=self.heap[r-1],self.heap[idx-1]
                idx=r
            else:
                break
            l=2*idx
            r=2*idx+1
                
        
    def _heapify_up(self):
        
        node_position=len(self.heap) - 1
        parent_position=(len(self.heap)//2)-1
        
        while parent_position>-1 and self.heap[parent_position] > self.heap[node_position] :
            self.heap[parent_position],self.heap[node_position]=self.heap[node_position],self.heap[parent_position]
            node_position=parent_position 
            parent_position=((parent_position+1)//2)-1