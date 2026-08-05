class MinStack:

    def __init__(self):
        self.stack = []
        self.Min = float('inf')
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.Min: 
            self.Min = val
            self.minstack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.Min:
            self.minstack.pop()
            if self.minstack: 
                self.Min = self.minstack[-1]
            else: 
                self.Min = float('inf')
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.Min
