class MinStack:
    def __init__(self):
        self.stackArr = []
        self.minArr = []

    def push(self, val: int) -> None:
        self.stackArr.append(val)
        if not self.minArr:
            self.minArr.append(val)
        else:
            self.minArr.append(min(val, self.minArr[-1]))

    def pop(self) -> None:
        self.stackArr.pop()
        self.minArr.pop()

    def top(self) -> int:
        return self.stackArr[-1]

    def getMin(self) -> int:
        return self.minArr[-1]
