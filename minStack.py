"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.

"""


# class MinStack:
#
#     def __init__(self):
#         self.stack = []
#         self.min_val = []
#
#     def push(self, val: int) -> None:
#         self.stack.append(val)
#         if len(self.min_val) == 0:
#             self.min_val.append(val)
#         else:
#             pass
#
#     def pop(self) -> None:
#         self.stack.pop()
#         if len(self.stack) > 0:
#             self.min_val = sorted(self.stack)[0]
#         else:
#             self.min_val = float('inf')
#
#     def top(self) -> int:
#         return self.stack[(len(self.stack) - 1)]
#
#     def getMin(self) -> int:
#         return self.min_val

class MinStack:
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.min:
            if x <= self.min[-1]:
                self.min.append(x)
        else:
            self.min.append(x)

    def pop(self) -> None:
        if self.stack[-1] == self.min[-1]:
            self.min = self.min[:-1]
        self.stack = self.stack[:-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]

s = MinStack()
s.push(0)
s.push(-3)
s.push(-5)

print(s.min)
