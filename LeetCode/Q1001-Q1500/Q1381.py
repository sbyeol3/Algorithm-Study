class CustomStack:
    
    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize
        

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize :
            self.stack.append(x)
        

    def pop(self) -> int:
        if len(self.stack) == 0 : return -1
        else : return self.stack.pop()
        

    def increment(self, k: int, val: int) -> None:
        length = k if k < len(self.stack) else len(self.stack)
        for i in range(length) :
            self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)