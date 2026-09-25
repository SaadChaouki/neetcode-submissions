# So we need to create a queue. It's a FIFO so essentially the main problem here
# is with the peek. Everything else is easy.

# The exercise says 2 queues, can we keep swapping them?

class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def empty(self) -> bool:
        return self._is_out_stack_empty() and self._is_in_stack_empty()

    def _is_out_stack_empty(self):
        return len(self.out_stack) == 0

    def _is_in_stack_empty(self):
        return len(self.in_stack) == 0

    def _swap(self):
        if self._is_out_stack_empty():
            while not self._is_in_stack_empty():
                self.out_stack.append(self.in_stack.pop())

    def pop(self) -> int:
        self._swap()
        return self.out_stack.pop()

    def peek(self) -> int:
        self._swap()
        return self.out_stack[-1]





# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()