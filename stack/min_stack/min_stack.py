import sys

class MinStack:
    def __init__(self):   
        self.arr = []
        self.minVal = sys.maxsize

    def push(self, val: int) -> None:
        if val < self.minVal:
            self.minVal = val
        self.arr.append(val)

    def pop(self) -> None:
        top = self.arr.pop()
        if self.minVal == top:
            if self.arr:
                self.minVal = min(self.arr)
            else:
                self.minVal = sys.maxsize    

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.minVal