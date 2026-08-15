class MyQueue:

    def __init__(self):
        self.stk=[]
        
    def push(self, x: int) -> None:
        sec=[]
        while self.stk:
            sec.append(self.stk.pop())
        self.stk.append(x)
        while sec:
            self.stk.append(sec.pop())
        
    def pop(self) -> int:
        if not self.stk:
            return -1
        else:
            return self.stk.pop() 

    def peek(self) -> int:
        if not self.empty():
            return self.stk[-1]
        return -1

    def empty(self) -> bool:
        return len(self.stk)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()