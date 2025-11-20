class Queue():
    def __init__(self):
        self.queue = []
        
    def enqueue(self, element):
        self.queue.append(element)
        
    def is_empty(self):
        return len(self.queue) == 0
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        
    def size(self):
        return len(self.queue)
    
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        