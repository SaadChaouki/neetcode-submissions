# So we need to create a queue. It's a FIFO so essentially the main problem here
# is with the peek. Everything else is easy.

# The exercise says 2 queues, can we keep swapping them?

class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        popped = self.stack[0]
        self.stack = self.stack[1:]
        return popped
        

    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()